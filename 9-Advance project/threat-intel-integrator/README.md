# Threat Intel Integrator

A Python-based security automation tool designed to streamline Open-Source Intelligence (OSINT) gathering. This script integrates with the VirusTotal API to quickly analyze IP addresses, replacing the manual process of querying threat databases with an automated, terminal-based Threat Intelligence Report.

## Features
* **Automated Threat Scanning:** Instantly queries the VirusTotal database for IP reputation and vendor analysis.
* **Data Parsing:** Extracts raw JSON telemetry and formats it into a clean, readable analyst report detailing Malicious, Suspicious, and Harmless flags.
* **Interactive CLI:** Prompts the user dynamically at runtime to input target IP addresses.
* **Secure Credential Management:** Implements `python-dotenv` to securely load API keys from environment variables, ensuring credentials are never hardcoded into the source code.

## Prerequisites
* Python 3.x
* A free [VirusTotal API Key](https://www.virustotal.com/)

## Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/threat-intel-integrator.git
   cd threat-intel-integrator
   ```

2. **Create and activate a virtual environment:**
   This ensures dependencies are isolated from your host system.
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key:**
   * Create a hidden file named `.env` in the root directory of the project.
   * Add your VirusTotal API key to the file exactly like this (no quotation marks):
     `API_KEY=your_actual_api_key_here`

## Usage
Activate your virtual environment (if not already active) and run the main script. The program will prompt you to enter the IP address you wish to analyze.

```bash
python3 main.py
```

## Example Output (Real-World Phishing IP Analysis)
```text
--- Threat Intel Integrator ---
Enter an IP address to scan: 43.155.136.247

Scanning IP: 43.155.136.247...

--- THREAT INTELLIGENCE REPORT ---
Target IP:  43.155.136.247
Country:    KR
Malicious:  4
Suspicious: 0
Harmless:   56

[!] WARNING: This IP is flagged as dangerous!
```

## Author
* **Abishek** - *Student & Aspiring SOC Analyst*
