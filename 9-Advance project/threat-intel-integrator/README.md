#  Custom Threat Intelligence Platform (TIP)

A full-stack Python web application built with Flask that aggregates threat intelligence feeds into a centralized SOC dashboard. This platform automates the triage of Indicators of Compromise (IOCs) by cross-referencing multiple industry-standard databases simultaneously and logging the history for historical tracking.

##  Features
* **Multi-Source Aggregation:** Simultaneously queries the **VirusTotal API v3** (Malware/Domains) and the **AbuseIPDB API** (Malicious IPs) to provide a unified threat verdict.
* **Web Dashboard:** Sleek, dark-mode UI built with HTML/Bootstrap for rapid SOC triage.
* **Persistent Database Logging:** Integrated **SQLite3** database automatically logs every scanned IOC, its threat scores, and a timestamp for historical tracking.
* **Multi-IOC Support:** Dynamically routes requests based on IOC type (IP Address, Domain, or SHA-256 Hash).
* **Secure Credential Management:** Utilizes `python-dotenv` to isolate and protect API keys.

##  Technology Stack
* **Backend:** Python 3.x, Flask
* **Database:** SQLite3
* **Frontend:** HTML5, Bootstrap 5 (CSS)
* **APIs:** VirusTotal REST API v3, AbuseIPDB API v2
* **Environment:** Linux (Zorin OS / Ubuntu)

##  Installation & Setup

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
pip install -r requirements.txt
```

**4. Initialize the Local Database:**
```bash
python3 setup_db.py
```

**5. Configure your API Keys:**
Create a hidden `.env` file in the root directory:
```bash
touch .env
```
Add your API keys inside the file:
```text
API_KEY=your_virustotal_key_here
ABUSEIPDB_API_KEY=your_abuseipdb_key_here
```

##  Usage

Start the Flask web server:
```bash
python3 app.py
```
Open your web browser and navigate to **`http://127.0.0.1:5000`**. 

Select your IOC type, enter the target (e.g., an IP address like `8.8.8.8`), and click Scan. The platform will dynamically fetch the aggregated intelligence and log the investigation into the local database history table.
