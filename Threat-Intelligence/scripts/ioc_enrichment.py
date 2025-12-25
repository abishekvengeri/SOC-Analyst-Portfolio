import requests
import json

def enrich_ip(ip):
    print(f"\n[+] Enriching IP: {ip}")

    try:
        # Public API example from ipinfo.io (no API key needed for basic info)
        resp = requests.get(f"https://ipinfo.io/{ip}/json")
        if resp.status_code == 200:
            data = resp.json()
            print(json.dumps(data, indent=4))
        else:
            print("Could not fetch details for this IP.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("IOC Enrichment Tool (Basic Version)")
    file_path = "sample-iocs.txt"
    
    with open("../ioc-datasets/sample-iocs.txt") as f:
        for line in f:
            ioc = line.strip()
            if not ioc or ioc.startswith("#"):
                continue
            
            # Detect type
            if ioc.replace(".", "").isdigit() or ioc.count(".") == 3:
                enrich_ip(ioc)
            else:
                print(f"\n[+] Skipping unsupported IOC: {ioc}")

if __name__ == "__main__":
    main()

