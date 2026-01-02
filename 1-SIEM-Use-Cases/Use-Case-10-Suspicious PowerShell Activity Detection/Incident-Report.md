# Incident Report – Suspicious PowerShell Activity

## 1. Summary
A suspicious PowerShell execution event was detected involving encoded or obfuscated command execution.  
Such behavior is commonly used by threat actors to hide their activity or perform malicious tasks such as downloading payloads, command execution, or establishing persistence.

## 2. Affected System
- Host: DESKTOP-0S2K0MN (from lab example)
- Log Source: Sysmon (Event ID 1 and/or 3)

## 3. Timeline
- PowerShell started with encoded or unusual command line
- A network connection was made shortly after (if applicable)
- No follow-up malicious persistence observed in this lab dataset

## 4. Observations
- PowerShell command line contained encoded content (`-EncodedCommand`)
- PowerShell initiated outbound HTTP/HTTPS traffic
- No legitimate automation tools were identified using encoded commands
- Parent process was normal (in this test case), but encoding is still suspicious

## 5. Analysis
The use of `-EncodedCommand` indicates an attempt to obfuscate script content.  
While PowerShell is widely used by administrators, encoded commands combined with network activity are known indicators of:
- Malware loaders
- Reconnaissance scripts
- Lateral movement preparation
- Data exfiltration techniques

Based on the available logs, the activity appears to be part of a controlled lab test rather than an ongoing attack.

## 6. Impact Assessment
- No confirmed compromise
- No persistence or follow-up malicious artifacts detected
- No user accounts impacted

## 7. Response Actions Taken
- Decoded the PowerShell command for analysis
- Verified the destination IP/domain reputation
- Confirmed that the activity matches expected lab behavior

## 8. Recommendations
- Enable PowerShell Script Block Logging (Event ID 4104)
- Restrict PowerShell usage to admin-only where possible
- Add detections for Office spawning PowerShell
- Continue monitoring for repeat encoded PowerShell activity

## 9. Conclusion
PowerShell executed with encoded commands and outbound network activity, which is a known malicious pattern.  
However, in this dataset, it corresponds to controlled lab simulations.  
No malicious compromise was identified.

