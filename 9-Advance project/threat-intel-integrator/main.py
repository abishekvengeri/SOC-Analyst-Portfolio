import requests
import os
import time
import csv
from dotenv import load_dotenv

# Securely load credentials
load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("[-] Error: API_KEY not found. Check .env file.")
    exit()

# NEW: An upgraded function that handles IPs, Domains, AND Hashes!
def scan_ioc(target, ioc_type):
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
    print(f"\nScanning {type_name}: {target}...")
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        result = response.json()
        stats = result['data']['attributes']['last_analysis_stats']
        
        print(f"Malicious:  {stats['malicious']} | Suspicious: {stats['suspicious']} | Harmless: {stats['harmless']}")
        
        if stats['malicious'] > 0:
            print(f"[!] WARNING: This {type_name} is flagged as dangerous!")
        else:
            print(f"[+] This {type_name} looks clean.")
            
        # Return a dictionary of the results for the CSV file
        return {
            'IOC': target,
            'Type': type_name,
            'Malicious': stats['malicious'],
            'Suspicious': stats['suspicious'],
            'Harmless': stats['harmless']
        }
            
    elif response.status_code in [204, 429]:
        print("[-] API Rate limit exceeded. We are scanning too fast!")
        return None
    else:
        print(f"[-] Error: Connection failed with status code {response.status_code}")
        return None

# --- Main Menu UI ---
print("\n--- Threat Intel Integrator v3.0 (Enterprise Edition) ---")
print("What do you want to investigate?")
print("1. IP Address")
print("2. Domain (e.g., evil.com)")
print("3. File Hash (SHA-256)")
ioc_choice = input("Select an option (1, 2, or 3): ")

print("\nHow do you want to scan?")
print("1. Scan a single target")
print("2. Bulk scan from a text file (Generates CSV Report)")
scan_mode = input("Select an option (1 or 2): ")

# --- Execution Logic ---
if scan_mode == '1':
    target = input("\nEnter the target to scan: ")
    scan_ioc(target, ioc_choice)

elif scan_mode == '2':
    filename = input("\nEnter the filename (e.g., ips.txt): ")
    scan_results = [] # A list to hold all our spreadsheet data
    
    try:
        with open(filename, 'r') as file:
            targets = file.readlines()
            
            for target in targets:
                clean_target = target.strip()
                if clean_target:
                    # Run the scan and save the returned data
                    data = scan_ioc(clean_target, ioc_choice)
                    if data:
                        scan_results.append(data)
                    
                    print("[*] Waiting 16 seconds to respect API rate limits...")
                    time.sleep(16) 
                    
        print("\n[+] Bulk scan complete!")
        
        # NEW: Write all the collected data into a CSV incident report!
        if scan_results:
            csv_file = 'incident_report.csv'
            with open(csv_file, 'w', newline='') as csvfile:
                fieldnames = ['IOC', 'Type', 'Malicious', 'Suspicious', 'Harmless']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(scan_results)
                
            print(f"[+] Success! Evidence report saved to {csv_file}")
            
    except FileNotFoundError:
        print(f"\n[-] Error: Could not find the file '{filename}'.")
else:
    print("\n[-] Invalid option. Please run the script again.")
