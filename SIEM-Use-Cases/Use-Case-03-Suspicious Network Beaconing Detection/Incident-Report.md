# Incident Report – Suspicious Network Beaconing

## 1. Summary
A beaconing pattern was detected from a single host, indicating repeated outbound connections to the same external IP address.  
This behavior is commonly associated with malware attempting to maintain communication with a Command-and-Control (C2) server.

## 2. Affected System
- Host: DESKTOP-0S2K0MN (example)
- Log Source: Sysmon (Event ID 3)
- Process Involved: [ProcessName]

## 3. Timeline
- Multiple outbound connections observed within short time intervals
- The destination IP remained constant
- Frequency suggested automated communication rather than user activity

## 4. Observations
- Beaconing detected in 30-second intervals (typical C2 pattern)
- Process generating connections was not commonly associated with network traffic
- Destination IP/domain reputation: [Pending TI lookup]

## 5. Analysis
The repeated outbound network traffic pattern is highly indicative of beaconing.  
Common reasons include:
- Malware checking in with a remote server
- Backdoor communication
- Reconnaissance scripts gathering environment data

No additional malicious activity was identified in this dataset, but the pattern must be treated seriously in a real environment.

## 6. Impact Assessment
- No confirmed payload downloads
- No lateral movement observed
- Potential compromise cannot be ruled out without deeper forensic analysis

## 7. Response Actions
- Performed TI lookup on destination IP
- Investigated process lineage through Sysmon logs
- Determined that this is controlled lab activity for portfolio generation

## 8. Recommendations
- Implement firewall block for suspicious IP/domains
- Enable additional monitoring such as DNS logging
- Consider EDR solutions that detect C2 behavior
- Perform deeper analysis if seen in production environment

## 9. Conclusion
Beaconing-like activity was detected, consistent with simulated C2 behavior.  
In a real environment, this would warrant escalation and possible containment.  
For this lab, it represents expected test activity and confirms SIEM detection capability.

