#  Threat Intelligence Integrator

An automated, Python-based Open-Source Intelligence (OSINT) utility designed to accelerate Tier-1 Security Operations Center (SOC) triage workflows. 

This tool integrates with the **VirusTotal API v3** to dynamically analyze Indicators of Compromise (IOCs) and generate structured incident reports, replacing slow manual analysis with automated bulk processing.

##  Enterprise Features
* **Multi-IOC Routing:** Dynamically scans IP Addresses, Domains, and SHA-256 File Hashes.
* **Bulk Automated Scanning:** Ingests `.txt` files containing dozens of IOCs for hands-free analysis.
* **API Rate-Limiting Engine:** Built-in sleep logic (16-second intervals) perfectly bypasses free-tier API restrictions (4 requests/min) to prevent crashes or connection bans.
* **Automated Evidence Generation:** Automatically parses nested JSON telemetry and exports structured `incident_report.csv` spreadsheets for SIEM ingestion or Jira ticketing.
* **Secure Credential Management:** Utilizes `python-dotenv` to keep API keys completely hidden from source code.

##  Technology Stack
* **Language:** Python 3.x
* **Libraries:** `requests`, `python-dotenv`, `csv`, `time`, `os`
* **API:** VirusTotal REST API v3
* **Environment:** Linux (Zorin OS / Ubuntu)

## Installation & Setup

**1. Clone the repository and navigate to the directory:**
```bash
git clone [https://github.com/abishekvengeri/SOC-Analyst-Portfolio.git](https://github.com/abishekvengeri/SOC-Analyst-Portfolio.git)
cd "SOC-Analyst-Portfolio/9-Advance project/threat-intel-integrator"
```

**2. Create and activate a Python Virtual Environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install required dependencies:**
```bash
pip install requests python-dotenv
```

**4. Configure your API Key:**
Create a hidden `.env` file in the root directory and add your VirusTotal API key:
```bash
touch .env
```
Inside the `.env` file, add the following line:
```text
API_KEY=your_actual_api_key_here
```

##  Usage

Run the main script from your terminal:
```bash
python3 main.py
```

### Option 1: Single Target Investigation
Select the IOC type (IP, Domain, or Hash) and input a single target. The tool will instantly parse the telemetry and return a clean terminal report.

### Option 2: Bulk Automated Triage (Generates CSV)
1. Create a text file (e.g., `ips.txt` or `domains.txt`) with one IOC per line.
2. Run the script and select the Bulk Scan option.
3. The tool will automate the scans, manage the rate limits, and output an `incident_report.csv` file into your directory containing the Malicious, Suspicious, and Harmless vendor flags.

##  Example Output (CSV Report)
| IOC | Type | Malicious | Suspicious | Harmless |
| :--- | :--- | :--- | :--- | :--- |
| 43.155.136.247 | IP | 4 | 0 | 56 |
| evil-phishing-site.com | Domain | 8 | 2 | 40 |
| 8.8.8.8 | IP | 0 | 0 | 60 |

