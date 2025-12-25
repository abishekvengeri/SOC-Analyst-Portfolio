# IOC Triage & Enrichment Playbook  
### SOC Analyst Operational Workflow  
### Author: [Your Name]

---

## 1. Purpose
This playbook defines the standard workflow for SOC Analysts (Tier 1 & Tier 2) to process and enrich Indicators of Compromise (IOCs).  
It provides a repeatable and structured method to determine the threat level of an IOC and guide appropriate SOC response actions.

---

## 2. Types of IOCs Covered
This playbook applies to the following IOC categories:

- **IP Addresses**
- **Domains / URLs**
- **File Hashes (MD5, SHA1, SHA256)**
- **Email addresses**
- **Registry key indicators** (less common, but possible)
- **Process names** (behavioral IOCs)

---

# 3. IOC Triage Workflow (Diagram)

                     START
                       |
            Receive IOC from sources:
      - SIEM Alert (e.g., beaconing, failed logons)
      - EDR Detection (malware, script execution)
      - Firewall / Proxy Logs
      - Threat Intelligence Feeds
      - External Notifications / CERT Advisories
                       |
                       v
            Identify IOC Type (IP, Domain, Hash)
                       |
                       v
             Perform Basic Validation
    ------------------------------------------------
    |   Is IOC formatted correctly?                |
    |   Is IOC internal or external?               |
    |   Does SOC already know about this IOC?      |
    ------------------------------------------------
                       |
                       v
          Run Threat Intelligence Enrichment
      (VirusTotal, OTX, AbuseIPDB, ipinfo.io, WHOIS)
                       |
                       v
          Determine IOC Severity / Classification
    ------------------------------------------------------------------
    |  • Benign: Known good, trusted, clean data                      |
    |  • Low: No major threat intel associations                      |
    |  • Medium: Suspicious behavior or one OSINT flag                |
    |  • High: Confirmed malicious, many TI hits, malware association |
    ------------------------------------------------------------------
                       |
                       v
                Decide SOC Response Action
    -------------------------------------------------------------------
    | High   → Block, isolate host, escalate to Tier 2/IR team        |
    | Medium → Monitor, correlate logs, check for follow-up activity  |
    | Low    → Document, watch for repeated indicators                 |
    | Benign → Mark as false positive and close                        |
    -------------------------------------------------------------------
                       |
                       v
                        END

---

# 4. Enrichment Sources Used

### ⭐ External OSINT Platforms
| Platform | Primary Use |
|----------|-------------|
| **VirusTotal** | Malware detection, URL/domain/IP reputation |
| **AlienVault OTX** | Community IOC sharing, pulses, malware campaigns |
| **AbuseIPDB** | IP abuse checks, scanning behavior, botnet activity |
| **ipinfo.io** | ASN, geolocation, hosting provider |
| **WHOIS / Domain Age** | Domain age, registrar, suspicious new domains |

### ⭐ Internal SOC Data Sources
| Source | Purpose |
|--------|---------|
| SIEM Historical Logs | Check past activity of IOC |
| EDR Telemetry | Check for malware or suspicious behavior |
| DNS Logs | Check frequency of domain requests |
| Proxy Logs | Check URL categorization and access patterns |
| Firewall Logs | Detect inbound/outbound attempts |

---

# 5. IOC Severity Classification

### 📌 **Benign IOC**
- Known good services (Google, Microsoft, Cloudflare)
- No OSINT flags
- No suspicious activity in internal logs

### ⚪ **Low Severity IOC**
- No malicious reputation
- Rarely observed but not harmful  
- Belongs to common hosting providers  
- No related alerts or events  

### 🟡 **Medium Severity IOC**
- Appears on 1–2 OSINT feeds  
- Occasionally contacted by internal hosts  
- Not clearly malicious but suspicious  
- Requires monitoring  

### 🔴 **High Severity IOC**
- Multiple OSINT hits confirming malware activity  
- Known C2 domain / IP  
- Related to phishing, ransomware, or trojans  
- Multiple internal hosts communicating with it  
- Requires **immediate escalation**

---

# 6. Escalation Guidelines

### 🚨 Escalate to Tier 2 If:
- IOC is associated with ransomware, C2, phishing, or APT infrastructure  
- IOC is contacted by multiple internal hosts  
- IOC appears in EDR logs with suspicious processes (PowerShell, wscript, mshta)  
- IOC leads to successful authentication attempts  
- IOC has high risk in VirusTotal / OTX  

### ⚠️ Remain Tier 1 If:
- IOC is clean according to all enrichment sources  
- Traffic is minimal and not persistent  
- IOC belongs to legitimate cloud or CDN providers  

---

# 7. Recommended Automated SOC Actions
These actions may be integrated into SIEM/SOAR:

### Automated Tasks
- Auto-enrich new IOCs upon detection  
- Auto-block known high-risk IPs/domains  
- Auto-isolate host if repeated beaconing occurs  
- Submit hashes to VirusTotal automatically  
- Send alerts when an IOC appears in multiple logs  

### Manual Analyst Tasks
- Decode suspicious scripts  
- Correlate logs across SIEM, EDR, DNS  
- Notify system owners if needed  

---

# 8. Example Use Case Applications

### Use Case A — Suspicious PowerShell
- IOC: External malicious IP  
- Enrichment shows C2 reputation  
- Process: powershell.exe contacting IP  
➡️ **Escalate — Possible malware beaconing**

### Use Case B — Failed Logon Brute Force
- IOC: IP with scanning/recon reputation  
➡️ Medium severity → Monitor + firewall review

### Use Case C — Malware Hash
- Hash matches EICAR / test malware  
➡️ Used for training → Low severity  

---

# 9. How SOC Analysts Use This Playbook
This playbook is referenced whenever:

- A SIEM alert includes an unknown IP/domain  
- An EDR detection references a malware hash  
- Firewall logs show repeated scanning  
- Threat intelligence feeds deliver new IOCs  

It ensures that all analysts follow the same structured, evidence-based approach.

---

# 10. Final Notes
This playbook is suitable for:

- SOC Tier 1  
- SOC Tier 2  
- Threat Intelligence Teams  
- Incident Response Teams  

It provides a professional, repeatable IOC triage workflow aligned with real-world SOC operations.

---



