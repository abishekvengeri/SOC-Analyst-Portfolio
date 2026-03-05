import os
import pandas as pd
from dotenv import load_dotenv
from modules.ingestor import CowrieIngestor
from modules.analyzer import AlertAnalyzer
from modules.enrichment import ThreatIntel
from modules.risk_engine import RiskScorer
from modules.notifier import TelegramNotifier  # <-- NEW IMPORT

# --- SECRET MANAGEMENT ---
load_dotenv()
API_KEY = os.getenv("ABUSEIPDB_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") # <-- NEW
TELEGRAM_CHAT = os.getenv("TELEGRAM_CHAT_ID")    # <-- NEW

def main():
    RAW_DATA = "data/raw"
    PROCESSED_DATA = "data/processed"
    CLEAN_CSV = os.path.join(PROCESSED_DATA, "cleaned_alerts.csv")

    if not os.path.exists(PROCESSED_DATA):
        os.makedirs(PROCESSED_DATA)

    print("\n" + "="*50)
    print("   FALSE POSITIVE REDUCTION TOOL")
    print("="*50)
    
    # 1. PHASE 1: INGESTION
    print(f"[*] Phase 1: Ingesting raw logs from {RAW_DATA}...")
    ingestor = CowrieIngestor(RAW_DATA, PROCESSED_DATA)
    raw_df = ingestor.load_all_logs()
    
    if raw_df.empty: return

    high_value_df = ingestor.filter_noise(raw_df)
    high_value_df.to_csv(CLEAN_CSV, index=False)
    print(f"[+] Noise Filtered: {len(raw_df)} raw events -> {len(high_value_df)} actionable alerts.")

    # 2. PHASE 2: ANALYSIS
    print("\n[*] Phase 2: Correlating alerts into incidents...")
    analyzer = AlertAnalyzer(CLEAN_CSV)
    attackers = analyzer.group_by_attacker()
    breached_ips = analyzer.find_successful_breaches()['src_ip'].unique()
    
    # 3. PHASE 3 & 4: SCORING AND NOTIFICATION
    print(f"[*] Phase 3 & 4: Enriching, Scoring, and Monitoring top threats...")
    
    intel = ThreatIntel(API_KEY)
    scorer = RiskScorer()
    
    # Initialize the Notifier if credentials exist
    notifier = None
    if TELEGRAM_TOKEN and TELEGRAM_CHAT:
        notifier = TelegramNotifier(TELEGRAM_TOKEN, TELEGRAM_CHAT)
    else:
        print("[!] Warning: Telegram credentials missing. Mobile alerts disabled.")
    
    results = []

    for rank, (ip, row) in enumerate(attackers.head(10).iterrows(), 1):
        abuse_score = intel.check_ip(ip) if API_KEY else 0
        has_breached = ip in breached_ips
        final_risk = scorer.calculate_final_score(has_breached, rank, abuse_score)
        
        # --- THE RESPONDER TRIGGER ---
        # If the risk is over 80, fire a Telegram alert!
        if final_risk >= 80 and notifier:
            notifier.send_alert(ip, final_risk, row['total_actions'], row['username'], abuse_score)
        
        results.append({
            'IP': ip,
            'Actions': row['total_actions'],
            'Users_Targeted': row['username'],
            'Breached': "YES" if has_breached else "NO",
            'Abuse_Score': f"{abuse_score}%",
            'PRIORITY_SCORE': final_risk
        })

    # OUTPUT DASHBOARD
    final_report = pd.DataFrame(results).sort_values(by='PRIORITY_SCORE', ascending=False)
    print("\n" + "="*85)
    print("                          SOC ANALYST PRIORITY DASHBOARD")
    print("="*85)
    print(final_report.to_string(index=False))
    print("="*85)
    print("\n[*] Tool execution complete.")

if __name__ == "__main__":
    main()
