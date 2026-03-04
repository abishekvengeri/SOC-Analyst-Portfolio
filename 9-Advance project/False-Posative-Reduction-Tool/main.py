import os
import pandas as pd
from dotenv import load_dotenv
from modules.ingestor import CowrieIngestor
from modules.analyzer import AlertAnalyzer
from modules.enrichment import ThreatIntel
from modules.risk_engine import RiskScorer

# --- SECRET MANAGEMENT ---
# Load variables from .env file
load_dotenv()
API_KEY = os.getenv("ABUSEIPDB_API_KEY")

def main():
    # --- CONFIGURATION ---
    RAW_DATA = "data/raw"
    PROCESSED_DATA = "data/processed"
    CLEAN_CSV = os.path.join(PROCESSED_DATA, "cleaned_alerts.csv")

    # Ensure processed directory exists
    if not os.path.exists(PROCESSED_DATA):
        os.makedirs(PROCESSED_DATA)

    print("\n" + "="*50)
    print("   CLAIRVOYANT FALSE POSITIVE REDUCTION TOOL")
    print("="*50)
    
    # 1. PHASE 1: DATA INGESTION & NOISE FILTERING
    print(f"[*] Phase 1: Ingesting raw logs from {RAW_DATA}...")
    ingestor = CowrieIngestor(RAW_DATA, PROCESSED_DATA)
    raw_df = ingestor.load_all_logs()
    
    if raw_df.empty:
        print("[-] No data found to process. Exiting.")
        return

    high_value_df = ingestor.filter_noise(raw_df)
    # Save as CSV for the Analyzer to pick up
    high_value_df.to_csv(CLEAN_CSV, index=False)
    print(f"[+] Noise Filtered: {len(raw_df)} raw events -> {len(high_value_df)} actionable alerts.")

    # 2. PHASE 2: CORRELATION & BEHAVIORAL ANALYSIS
    print("\n[*] Phase 2: Correlating alerts into incidents...")
    analyzer = AlertAnalyzer(CLEAN_CSV)
    
    # Group by IP and calculate Aggression Score
    attackers = analyzer.group_by_attacker()
    # Track unique IPs that achieved a successful login
    breached_ips = analyzer.find_successful_breaches()['src_ip'].unique()
    
    print(f"[+] Identified {len(attackers)} unique attacker IPs.")

    # 3. PHASE 3: THREAT INTEL ENRICHMENT & RISK SCORING
    print(f"[*] Phase 3: Enriching and Scoring top 10 threats...")
    
    if not API_KEY:
        print("[!] Warning: No API Key found in .env. Reputation checks will be skipped.")

    intel = ThreatIntel(API_KEY)
    scorer = RiskScorer()
    
    results = []

    # Iterate through top 10 attackers by Aggression Score
    for rank, (ip, row) in enumerate(attackers.head(10).iterrows(), 1):
        # A. Reputation Check
        abuse_score = intel.check_ip(ip) if API_KEY else 0
        
        # B. Outcome Check
        has_breached = ip in breached_ips
        
        # C. Final Decision Logic
        final_risk = scorer.calculate_final_score(has_breached, rank, abuse_score)
        
        results.append({
            'IP': ip,
            'Actions': row['total_actions'],
            'Users_Targeted': row['username'],
            'Breached': "YES" if has_breached else "NO",
            'Abuse_Score': f"{abuse_score}%",
            'PRIORITY_SCORE': final_risk
        })

    # 4. PHASE 4: THE SOC ANALYST DASHBOARD
    final_report = pd.DataFrame(results).sort_values(by='PRIORITY_SCORE', ascending=False)
    
    print("\n" + "="*85)
    print("                          SOC ANALYST PRIORITY DASHBOARD")
    print("="*85)
    print(final_report.to_string(index=False))
    print("="*85)
    
    # Identify the top threat for the analyst
    top_threat = final_report.iloc[0]['IP']
    print(f"\n[!] HIGH FIDELITY RECOMMENDATION: Investigate IP {top_threat} immediately.")
    print(f"[*] Total reduction in analyst workload: {round((1 - (10/len(raw_df))) * 100, 2)}%")
    print("\n[*] Clairvoyant Tool execution complete.")

if __name__ == "__main__":
    main()
