# Investigation Workflow – Suspicious Network Beaconing

## 1. Alert Trigger
This alert fires when a process repeatedly connects to the same external IP or domain over short, regular intervals.  
This behavior is commonly associated with malware communicating with a Command-and-Control (C2) server.

## 2. Initial Validation
1. Confirm Sysmon Event ID 3 is the source.
2. Extract:
   - ProcessName
   - Destination IP and port
   - Frequency of connections
   - Time intervals between connections

## 3. Enrichment Steps
- Check destination IP/domain reputation via:
  - VirusTotal
  - OTX
  - AbuseIPDB
- Check whether the process making connections is legitimate:
  - Normal: chrome.exe, system services
  - Suspicious: powershell.exe, mshta.exe, wscript.exe, random EXEs
- Compare with historical logs:
  - Has this host contacted this IP before?
  - Is the process known to make outbound requests?

## 4. Key Questions During Investigation
- Does the process normally make network connections?
- Are the connection intervals consistent (e.g., every 30 seconds)?
- Is the destination IP associated with malware or anonymizing services?
- Is lateral movement happening before or after the beacon?

## 5. Escalation Criteria
Escalate to Tier 2 if:
- Destination IP is malicious or unknown
- Process is unusual (wscript, powershell, random binary)
- Beaconing is consistent (same interval)
- Multiple hosts connect to the same IP

## 6. Recommended Response Actions
- Isolate the endpoint if beaconing appears malicious
- Capture memory and run forensic tools (Volatility, ProcDump)
- Block outbound connections to the suspicious IP/domain
- Identify whether any payloads were downloaded
- Reset credentials for the affected user if lateral movement is suspected

## 7. MITRE Techniques
- **T1071 – Application Layer C2**
- **T1105 – File Transfer (C2)**
- **T1095 – Non-Application Layer Protocol**

