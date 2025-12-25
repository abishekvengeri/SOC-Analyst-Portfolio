# IOC Enrichment Scripts

Files:
- ioc_enrichment_enhanced.py : main enrichment script
- requirements.txt : Python dependencies

How to run (recommended):
1. Create and activate venv:
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Set API keys (optional but recommended for enrichment):
   export VT_API_KEY="your_virustotal_api_key"
   export OTX_API_KEY="your_otx_api_key"
   export ABUSEIPDB_API_KEY="your_abuseipdb_api_key"

4. Run script:
   python3 ioc_enrichment_enhanced.py

Output:
- ../reports/enrichment/enrichment_results.json
- ../reports/enrichment/<ioc>.json (per-indicator file)

