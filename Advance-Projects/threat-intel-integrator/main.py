import requests
import os
from dotenv import load_dotenv

# Load the secret .env file
load_dotenv()

# Get the key from the environment
API_KEY = os.getenv("API_KEY")

print("--- Threat Intel Integrator ---")

# Check if the key loaded correctly
if not API_KEY:
    print("Error: API Key not found. Please check your .env file.")
    exit()

ip_address = input("Enter an IP address to scan: ")

url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"

headers = {
    "x-apikey": API_KEY
}

print(f"\nScanning {ip_address}...")
response = requests.get(url, headers=headers)

if response.status_code == 200:
    result = response.json()
    attributes = result['data']['attributes']

    country = attributes.get('country', 'Unknown')
    stats = attributes['last_analysis_stats']

    print(f"Country: {country}")
    print(f"Malicious: {stats['malicious']}")
    print(f"Suspicious: {stats['suspicious']}")
    print(f"Harmless:  {stats['harmless']}")
    
    if stats['malicious'] > 0:
        print("\nWARNING: This IP is dangerous!")
    else:
        print("\nThis IP looks clean.")

elif response.status_code == 404:
    print("Error: IP address not found in database.")
else:
    print("Error:", response.status_code)
