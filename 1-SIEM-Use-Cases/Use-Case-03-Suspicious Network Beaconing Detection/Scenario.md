# SIEM Use Case 3: Suspicious Network Beaconing Detection

## 1. Description
Command-and-Control (C2) malware often generates consistent outbound connections to a single IP or domain, usually in fixed intervals.  
This use case detects beaconing behavior by analyzing repeated network connections.

## 2. Log Source
- Sysmon Event ID 3 (Network Connections)
- Firewall logs (optional)
- Proxy logs (optional)

## 3. Beaconing Indicators
- Repeated connections from the same process to the same destination
- Regular time intervals (e.g., every 30 seconds)
- Destination IP not previously contacted by the environment
- Non-standard processes establishing outbound connections

## 4. Detection Goal
Identify possible malware communicating with a C2 server.

## 5. MITRE ATT&CK Mapping
- **T1071 – Application Layer Protocol**
- **T1105 – Ingress Tool Transfer**
- **T1095 – Non-Application Layer Protocol**

## 6. Expected Alerts
- Outbound traffic from unexpected processes
- Network connections with repeating patterns
- Communication with suspicious IPs/domains

