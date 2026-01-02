# Scenario: Network Reconnaissance and Port Scanning Detection

## Background
A Security Operations Center (SOC) analyst detected unusual TCP connection attempts originating from an internal host. Network reconnaissance, particularly port scanning, is commonly used by attackers to identify exposed services before exploitation.

The analyst must inspect packet-level network traffic to determine whether the observed activity is consistent with reconnaissance behavior.

## Environment
- Attacker Host: Kali Linux VM (192.168.56.102)
- Victim Host: Windows 10 Pro VM (192.168.56.101)
- Network Type: Host-Only (isolated VM environment)
- Tool Used: Nmap (TCP SYN scan)
- Capture Tool: Wireshark
- Capture Location: Victim VM (Windows)

## Objective
To capture and analyze reconnaissance traffic and identify indicators of TCP SYN scanning used for service discovery.

## Assumptions
- Traffic is generated intentionally for lab purposes
- No exploitation or payload delivery occurs
- No production systems or internet traffic are involved

## Analyst Tasks
- Capture TCP traffic during a scan
- Identify SYN-only probe packets
- Identify SYN-ACK responses from open ports
- Document reconnaissance indicators and findings

