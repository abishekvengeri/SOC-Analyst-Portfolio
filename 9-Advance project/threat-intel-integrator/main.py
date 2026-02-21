import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("[-] Error: API_KEY not found. Check .env file.")
    exit()

def scan_ip(ip_address):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"
    headers = {"x-apikey": API_KEY}
    
    print(f"\nScanning IP: {ip_address}...")
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        result = response.json()
        stats = result['data']['attributes']['last_analysis_stats']
        country = result['data']['attributes'].get('country', 'Unknown')
        
        print(f"Country:    {country}")
        print(f"Malicious:  {stats['malicious']} | Suspicious: {stats['suspicious']} | Harmless: {stats['harmless']}")
        
        if stats['malicious'] > 0:
            print("[!] WARNING: This IP is flagged as dangerous!")
        else:
            print("[+] This IP looks clean.")
            
    elif response.status_code == 204 or response.status_code == 429:
        print("[-] API Rate limit exceeded. We are scanning too fast!")
    else:
        print(f"[-] Error: Connection failed with status code {response.status_code}")

print("\n--- Threat Intel Integrator v2.0 ---")
print("1. Scan a single IP")
print("2. Scan a list of IPs from a file")

choice = input("\nSelect an option (1 or 2): ")

if choice == '1':
    ip = input("Enter an IP address to scan: ")
    scan_ip(ip)

elif choice == '2':
    filename = input("Enter the filename (e.g., ips.txt): ")
    try:
        with open(filename, 'r') as file:
            ip_list = file.readlines()
            for ip in ip_list:
                clean_ip = ip.strip()
                if clean_ip:
                    scan_ip(clean_ip)
                    print("\n[*] Waiting 16 seconds to respect API rate limits...")
                    time.sleep(16) 
        print("\n[+] Bulk scan complete!")
    except FileNotFoundError:
        print(f"\n[-] Error: Could not find the file '{filename}'.")
else:
    print("\n[-] Invalid option. Please run the script again.")
