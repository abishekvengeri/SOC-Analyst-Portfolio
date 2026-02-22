import requests
import os
import time
import csv
from dotenv import load_dotenv

# Securely load both credentials!
load_dotenv()
API_KEY = os.getenv("API_KEY")
ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")

if not API_KEY:
    print("[-] Error: API_KEY not found. Check .env file.")
    exit()

def scan_ioc(target, ioc_type):
    # --- 1. VIRUSTOTAL LOGIC (Scans Everything) ---
    vt_malicious = 0
    vt_suspicious = 0
    vt_harmless = 0
    type_name = "Unknown"

    if ioc_type == '1': # IP Address
        url = f"https://www.virustotal.com/api/v3/ip_addresses/{target}"
        type_name = "IP"
    elif ioc_type == '2': # Domain
        url = f"https://www.virustotal.com/api/v3/domains/{target}"
        type_name = "Domain"
    elif ioc_type == '3': # File Hash
        url = f"https://www.virustotal.com/api/v3/files/{target}"
        type_name = "Hash"
    else:
        return None

    headers = {"x-apikey": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        result = response.json()
        stats = result['data']['attributes']['last_analysis_stats']
        vt_malicious = stats['malicious']
        vt_suspicious = stats['suspicious']
        vt_harmless = stats['harmless']
            
    # --- 2. ABUSEIPDB LOGIC (Only scans IP addresses) ---
    abuse_score = "N/A" # Default to N/A if it's a domain or hash
    
    if ioc_type == '1' and ABUSEIPDB_API_KEY:
        abuse_url = 'https://api.abuseipdb.com/api/v2/check'
        querystring = {'ipAddress': target, 'maxAgeInDays': '90'}
        abuse_headers = {
            'Accept': 'application/json',
            'Key': ABUSEIPDB_API_KEY
        }
        abuse_response = requests.get(abuse_url, headers=abuse_headers, params=querystring)
        
        if abuse_response.status_code == 200:
            abuse_data = abuse_response.json()
            # AbuseIPDB returns a percentage (0 to 100) of how confident they are it's malicious
            abuse_score = f"{abuse_data['data']['abuseConfidenceScore']}%"

    # --- 3. RETURN COMBINED INTELLIGENCE ---
    return {
        'IOC': target,
        'Type': type_name,
        'Malicious': vt_malicious,
        'Suspicious': vt_suspicious,
        'Harmless': vt_harmless,
        'AbuseScore': abuse_score  # NEW: Sending this to the web dashboard!
    }


if __name__ == '__main__':
    print("\n--- Threat Intel Integrator (Multi-Source CLI) ---")
    print("Run 'python3 app.py' to use the Web Dashboard instead!")
    target = input("\nEnter an IP to test the multi-source engine: ")
    data = scan_ioc(target, '1')
    print(f"\nResults for {target}:")
    print(f"VirusTotal Malicious: {data['Malicious']}")
    print(f"AbuseIPDB Confidence: {data['AbuseScore']}")
