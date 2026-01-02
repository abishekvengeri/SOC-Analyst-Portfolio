# Scenario: TCP Three-Way Handshake Analysis in an Isolated Lab Environment

## Background
A Security Operations Center (SOC) analyst is tasked with analyzing raw packet captures collected from an isolated virtual lab. The purpose of this scenario is to observe and document the complete TCP three-way handshake used to establish a reliable network connection between two hosts.

Understanding baseline TCP behavior is critical before analyzing abnormal or malicious network activity such as port scans, SYN floods, or session hijacking.

## Environment
- Client Host: Windows 10 Pro VM (192.168.56.101)
- Server Host: Kali Linux VM (192.168.56.102)
- Network Type: Host-Only (VM-only, no internet access)
- Service: Netcat listener on TCP port 4444
- Capture Tool: Wireshark

## Objective
To capture and analyze the full TCP three-way handshake (SYN, SYN-ACK, ACK) and document each stage of the connection establishment process.

## Assumptions
- Traffic is intentionally generated for lab purposes
- Packet capture was started before the connection attempt
- No production systems or real credentials are involved

## Analyst Tasks
- Isolate TCP handshake packets using display filters
- Identify client and server roles
- Analyze TCP flags, sequence numbers, and options
- Document findings in a structured investigation report

