# Investigation Workflow – Suspicious PowerShell Activity

## 1. Alert Trigger
This alert fires when:
- PowerShell runs with encoded or obfuscated commands
- PowerShell generates outbound network connections
- PowerShell is launched by an unusual parent (e.g., WINWORD.exe)

## 2. Initial Validation
1. Confirm the alert was generated from Sysmon EventID 1 or 3.
2. Extract:
   - Full command line
   - Parent process
   - Destination IP address (if network activity)
   - User account involved

## 3. Enrichment Steps
- Check the destination IP/domain using:
  - VirusTotal
  - OTX
  - AbuseIPDB
- Verify if the PowerShell command is:
  - Legitimate admin automation
  - A known script used within the company
- Check if similar activity happened on other hosts.

## 4. Key Questions for Investigation
- Is the PowerShell command intentionally encoded?
- Does the command download content from the internet?
- Is the parent process suspicious?
- Is the user expected to run PowerShell?
- Are there follow-up events (e.g., file writes, registry changes)?

## 5. Escalation Criteria
Escalate to Tier 2 if:
- PowerShell connects to unknown or suspicious external IPs
- EncodedCommand contains base64 payloads or IEX (Invoke-Expression)
- PowerShell was launched by Office apps (e.g., Excel, Word → strongly suspicious)
- The destination IP is malicious according to TI

## 6. Recommended Actions
- Suspend or isolate the endpoint if malicious behavior continues
- Decode the base64 command to understand intent
- Block outbound traffic to suspicious IPs
- Check if persistence mechanisms were added
- Reset affected user passwords if compromised

## 7. MITRE Mapping
- **T1059.001 – PowerShell Execution**
- **T1105 – Ingress Tool Transfer**
- **T1055 – Process Injection** (possible follow-up)

