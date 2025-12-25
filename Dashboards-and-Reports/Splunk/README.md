# Splunk Dashboards – SOC Analyst Portfolio

This folder contains professional Splunk dashboards and saved searches designed for security monitoring, alerting, and incident analysis.

## 📄 What’s Included

### 1. exports/
Contains Splunk dashboard export files (XML) that can be imported into any Splunk environment.

### 2. screenshots/
High-quality screenshots of each dashboard, including:
- SOC Overview Dashboard  
- Authentication Monitoring  
- Sysmon Process Execution  
- Network Beaconing  
- Threat Intelligence Dashboard  

### 3. queries/
All SPL queries used to build the dashboards, each with comments explaining:
- What the query detects  
- Why it matters  
- Which MITRE techniques it maps to  

### 4. SOC-Weekly-Report.md
A professional weekly SOC summary that demonstrates reporting capability.

---

## 📥 How To Import Dashboards (Splunk)

1. Go to **Splunk > Dashboards**  
2. Click **Import Dashboard**  
3. Upload any XML files from **exports/**  
4. Ensure these data sources exist:
   - `index=wineventlog`  
   - `index=sysmon`  
   - `index=network`  
   - `index=firewall`  
5. Refresh dashboard and run saved searches

---

## 🧠 About This Section

These dashboards are designed to demonstrate:
- Real SOC data analysis  
- SIEM visualization skills  
- Ability to detect malicious behavior  
- Ability to communicate findings visually  

This is one of the strongest parts of the SOC portfolio.

