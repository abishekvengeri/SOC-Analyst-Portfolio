# SIEM Use Case 2: Suspicious PowerShell Activity Detection

## 1. Description
PowerShell is a common tool abused by attackers for execution, lateral movement, reconnaissance, and payload delivery.  
This use case detects suspicious PowerShell behavior including encoded commands, downloads, and abnormal parent-child process relationships.

## 2. Log Source
- Sysmon Logs
- Event ID 1 (Process Create)
- Event ID 3 (Network Connection)
- Event ID 4104 (PowerShell Script Block Logging, if enabled)

## 3. Attack Indicators
- PowerShell launched with `-EncodedCommand`
- PowerShell connecting to external IPs/domains
- PowerShell launched by unusual parent processes (e.g., WINWORD.exe, excel.exe)
- PowerShell executing base64-encoded or obfuscated scripts

## 4. Detection Goal
Identify early-stage attacker activity such as:
- Obfuscated command execution
- Download cradle activity
- Command-and-control communication

## 5. MITRE ATT&CK Mappings
- **T1059.001 – PowerShell**
- **T1105 – Ingress Tool Transfer**
- **T1047 – WMI Execution** (if chained)

## 6. Expected Alerts
- Any encoded PowerShell execution
- PowerShell making outbound connections to unknown hosts
- PowerShell spawned by Microsoft Office or scripting engines

