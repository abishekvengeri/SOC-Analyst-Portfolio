import requests

class ThreatIntel:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.abuseipdb.com/api/v2/check'

    def check_ip(self, ip_address):
        """Queries AbuseIPDB for an IP's reputation score."""
        querystring = {
            'ipAddress': ip_address,
            'maxAgeInDays': '90'
        }
        headers = {
            'Accept': 'application/json',
            'Key': self.api_key
        }

        try:
            response = requests.get(self.base_url, headers=headers, params=querystring)
            if response.status_code == 200:
                data = response.json()
                return data['data']['abuseConfidenceScore']
            else:
                return 0
        except Exception as e:
            print(f"[!] API Error: {e}")
            return 0
