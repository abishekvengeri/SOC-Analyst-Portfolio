#!/usr/bin/env python3
"""
IOC Enrichment - Enhanced
Reads IOCs from ../ioc-datasets/sample-iocs.txt and enriches them using:
 - ipinfo.io (basic; no API key required for summary)
 - VirusTotal v3 (API key via env: VT_API_KEY)
 - AlienVault OTX (API key via env: OTX_API_KEY) - optional
 - AbuseIPDB (API key via env: ABUSEIPDB_API_KEY) - optional

Outputs:
 - JSON files per IOC in ../reports/enrichment/
 - Combined JSON summary at ../reports/enrichment/enrichment_results.json

Usage:
    export VT_API_KEY="your_vt_key"
    export OTX_API_KEY="your_otx_key"
    export ABUSEIPDB_API_KEY="your_abuseipdb_key"
    python3 ioc_enrichment_enhanced.py
"""

import os
import time
import json
import argparse
import requests
from urllib.parse import quote_plus

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IOC_FILE = os.path.join(BASE_DIR, "ioc-datasets", "sample-iocs.txt")
OUT_DIR = os.path.join(BASE_DIR, "reports", "enrichment")
os.makedirs(OUT_DIR, exist_ok=True)

# API keys from environment
VT_API_KEY = os.getenv("VT_API_KEY")
OTX_API_KEY = os.getenv("OTX_API_KEY")
ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")

HEADERS = {
    "User-Agent": "IOC-Enrichment-Tool/1.0"
}

def save_json(obj, filename):
    with open(filename, "w") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)

def enrich_ipinfo(ioc):
    """Use ipinfo.io for quick IP context (no key required for basics)."""
    out = {"ipinfo": None}
    try:
        r = requests.get(f"https://ipinfo.io/{ioc}/json", headers=HEADERS, timeout=15)
        if r.ok:
            out["ipinfo"] = r.json()
        else:
            out["ipinfo_error"] = r.text
    except Exception as e:
        out["ipinfo_error"] = str(e)
    return out

def enrich_virustotal(ioc, ioc_type):
    """VirusTotal v3 endpoints. Requires VT_API_KEY."""
    if not VT_API_KEY:
        return {"vt_error": "VT_API_KEY not set"}
    headers = {"x-apikey": VT_API_KEY, **HEADERS}
    try:
        if ioc_type == "ip":
            url = f"https://www.virustotal.com/api/v3/ip_addresses/{ioc}"
        elif ioc_type == "domain":
            url = f"https://www.virustotal.com/api/v3/domains/{quote_plus(ioc)}"
        elif ioc_type == "hash":
            url = f"https://www.virustotal.com/api/v3/files/{ioc}"
        else:
            return {"vt_error": "unsupported ioc_type"}
        r = requests.get(url, headers=headers, timeout=20)
        if r.ok:
            return {"virustotal": r.json()}
        else:
            return {"vt_error": f"{r.status_code} {r.text}"}
    except Exception as e:
        return {"vt_error": str(e)}

def enrich_otx(ioc, ioc_type):
    """AlienVault OTX - basic general endpoint"""
    if not OTX_API_KEY:
        return {"otx_error": "OTX_API_KEY not set"}
    try:
        if ioc_type == "ip":
            url = f"https://otx.alienvault.com/api/v1/indicators/IPv4/{ioc}/general"
        elif ioc_type == "domain":
            url = f"https://otx.alienvault.com/api/v1/indicators/domain/{ioc}/general"
        elif ioc_type == "hash":
            url = f"https://otx.alienvault.com/api/v1/indicators/file/{ioc}/general"
        else:
            return {"otx_error": "unsupported ioc_type"}
        headers = {"X-OTX-API-KEY": OTX_API_KEY, **HEADERS}
        r = requests.get(url, headers=headers, timeout=20)
        if r.ok:
            return {"otx": r.json()}
        else:
            return {"otx_error": f"{r.status_code} {r.text}"}
    except Exception as e:
        return {"otx_error": str(e)}

def enrich_abuseipdb(ioc):
    """AbuseIPDB check for IP reputation (requires API key)."""
    if not ABUSEIPDB_API_KEY:
        return {"abuseipdb_error": "ABUSEIPDB_API_KEY not set"}
    try:
        url = "https://api.abuseipdb.com/api/v2/check"
        headers = {
            "Key": ABUSEIPDB_API_KEY,
            "Accept": "application/json",
            **HEADERS
        }
        params = {"ipAddress": ioc, "maxAgeInDays": 90}
        r = requests.get(url, headers=headers, params=params, timeout=20)
        if r.ok:
            return {"abuseipdb": r.json()}
        else:
            return {"abuseipdb_error": f"{r.status_code} {r.text}"}
    except Exception as e:
        return {"abuseipdb_error": str(e)}

def detect_ioc_type(ioc):
    # crude detection
    if ioc.count(".") == 3 and all(p.isdigit() for p in ioc.split(".") if p):
        return "ip"
    if any(ch in ioc for ch in [":", "/"]) or "." in ioc and not all(p.isalnum() for p in ioc.split(".")):
        # still treat dot-containing strings without all-alnum as domain
        return "domain"
    # heuristic for hash
    if len(ioc) in (32, 40, 64) and all(c in "0123456789abcdefABCDEF" for c in ioc):
        return "hash"
    # fallback
    if "." in ioc:
        return "domain"
    return "unknown"

def enrich_ioc(ioc):
    ioc = ioc.strip()
    ioc_type = detect_ioc_type(ioc)
    result = {
        "ioc": ioc,
        "type": ioc_type,
        "enriched": {},
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }

    # ipinfo for basic context
    try:
        if ioc_type == "ip":
            result["enriched"].update(enrich_ipinfo(ioc))
        else:
            result["enriched"]["ipinfo_skipped"] = "not an IP"
    except Exception as e:
        result["enriched"]["ipinfo_error"] = str(e)

    # VirusTotal
    try:
        vt = enrich_virustotal(ioc, ioc_type)
        result["enriched"].update(vt)
    except Exception as e:
        result["enriched"]["vt_error"] = str(e)

    # OTX
    try:
        otx = enrich_otx(ioc, ioc_type)
        result["enriched"].update(otx)
    except Exception as e:
        result["enriched"]["otx_error"] = str(e)

    # AbuseIPDB (only for IPs)
    if ioc_type == "ip":
        try:
            abuse = enrich_abuseipdb(ioc)
            result["enriched"].update(abuse)
        except Exception as e:
            result["enriched"]["abuseipdb_error"] = str(e)

    return result

def main():
    print("IOC Enrichment - Enhanced")
    print("Output ->", OUT_DIR)
    results = []
    if not os.path.exists(IOC_FILE):
        print("IOC file not found:", IOC_FILE)
        return

    with open(IOC_FILE) as f:
        lines = [l.strip() for l in f if l.strip() and not l.startswith("#")]

    # Rate limit safe defaults
    for i, ioc in enumerate(lines, 1):
        print(f"[{i}/{len(lines)}] Processing: {ioc}")
        try:
            r = enrich_ioc(ioc)
            results.append(r)
            # save per-ioc
            fn = os.path.join(OUT_DIR, f"{ioc.replace('/', '_')}.json")
            save_json(r, fn)
        except Exception as e:
            print("Error enriching", ioc, e)
        # friendly pause to avoid hammering public APIs
        time.sleep(1.5)

    # save combined summary
    out_file = os.path.join(OUT_DIR, "enrichment_results.json")
    save_json(results, out_file)
    print("Completed. Summary saved to:", out_file)

if __name__ == "__main__":
    main()

