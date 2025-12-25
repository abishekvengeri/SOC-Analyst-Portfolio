# MITRE ATT&CK Mapping

Wazuh correctly mapped the detection to the following MITRE technique:

| Tactic          | Technique Name         | Technique ID |
|-----------------|------------------------|--------------|
| Reconnaissance  | Vulnerability Scanning | T1595.002    |

Reasoning:
- Repeated GET/POST/PROPFIND attempts to invalid paths
- Automated probing using the Nmap Scripting Engine user-agent
- High volume of 4xx/5xx responses indicating enumeration attempts

The MITRE dashboard confirmed the mapping for the agent.

