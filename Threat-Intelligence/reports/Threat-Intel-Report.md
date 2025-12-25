# Threat Intelligence Report  
### IOC Enrichment & Analysis Summary  
### Prepared by: [Your Name]  
### Date: [Insert Date]

---

## 1. Executive Summary
This report provides analysis and enrichment of sample Indicators of Compromise (IOCs) including IP addresses, domains, and file hashes.  
The goal is to demonstrate IOC triage and threat intelligence workflows for SOC operations.  
All IOCs used in this report are safe, non-malicious examples for portfolio demonstration.

---

## 2. IOC List
The following IOCs were analyzed:

### IP Addresses
- **8.8.8.8**  
- **185.244.25.117**  
- **103.144.74.52**

### Domains
- **malicious-domain-example.com**  
- **test-malware.net**

### File Hashes (SHA256)
- **44d88612fea8a8f36de82e1278abb02f**  
- **eicar_test_file_signature**

---

## 3. Enrichment Summary
Using open-source TI platforms (ipinfo.io, OTX, VirusTotal), basic context was gathered.

### 3.1 IP: 8.8.8.8
- **Classification:** Clean  
- **Owner:** Google LLC  
- **Type:** Public DNS  
- **Risk:** Low  
- **Notes:** Common false positive in many alerts.

### 3.2 IP: 185.244.25.117
- **Status:** Suspicious (based on public reputation feeds)  
- **Observed Associations:**
  - Flagged on several free OSINT feeds for scanning behavior  
- **Risk:** Medium  
- **SOC Action:** Monitor for repeated connections.

### 3.3 IP: 103.144.74.52
- **Status:** Unknown / Not enough OSINT**
- **Risk:** Medium  
- **SOC Action:** Correlate with internal logs before escalation.

### 3.4 Domains (Simulated)
#### malicious-domain-example.com
- **Status:** Simulated malicious domain for training  
- **Risk:** High  
- **MITRE Mapping:**  
  - T1071 (C2 Communication)  
  - T1105 (Remote File Transfer)

#### test-malware.net
- **Status:** Simulated malware distribution test domain  
- **Risk:** High  
- **Notes:** Used in lab examples only.

### 3.5 File Hashes
#### 44d88612fea8a8f36de82e1278abb02f
- **Classification:** EICAR test malware  
- **Purpose:** For testing AV/SOC detection  
- **Risk:** Medium (lab-only)

#### eicar_test_file_signature
- Map to EICAR test malware  
- Safe test file used for validating security tools  

---

## 4. Threat Assessment
| IOC Type | Count | High Risk | Medium Risk | Low Risk |
|----------|-------|-----------|-------------|----------|
| IP       | 3     | 0         | 2           | 1        |
| Domains  | 2     | 2         | 0           | 0        |
| Hashes   | 2     | 1 (EICAR) | 1           | 0        |

**Overall Threat Score:** *Medium*

Domains represent the most significant risk category, followed by untrusted external IP traffic.

---

## 5. MITRE ATT&CK Techniques Observed
| Technique | Description |
|----------|-------------|
| T1071 | Application Layer C2 Communication |
| T1105 | Remote File Transfer |
| T1049 | Network Reconnaissance (via scanning IPs) |

---

## 6. Recommendations
1. **Block access** to all high-risk domains.  
2. **Monitor outbound connections** to 185.244.25.117 and 103.144.74.52.  
3. **Alert on any endpoint** that executes files matching known malware test signatures.  
4. **Enable Threat Intelligence integration** in SIEM for continuous enrichment.  
5. **Add detections** for:
   - DNS queries to suspicious domains  
   - Outbound network connections to unknown IP ranges  
6. **Schedule recurring IOC reviews** every 24 hours.

---

## 7. Conclusion
The IOC enrichment process revealed several simulated malicious domains and medium-risk IP addresses.  
This demonstrates how a SOC analyst uses TI platforms to:

- Validate alerts  
- Prioritize threats  
- Create actionable detections  
- Support incident response  

This report serves as a formal example of SOC-level threat intelligence procedures.

