# Scenario: DNS Tunneling Inspection in an Isolated Network

## Background
A SOC analyst is investigating unusual DNS activity originating from an internal endpoint. DNS tunneling is a known technique used by attackers to exfiltrate data or establish command-and-control channels by embedding data within DNS queries.

The analyst must inspect DNS request and response packets to determine whether the observed traffic exhibits tunneling-related characteristics.

## Environment
- Endpoint Host: Windows 10 Pro VM (192.168.56.101)
- DNS Server: Kali Linux VM (192.168.56.102)
- Network Type: Host-Only (isolated virtual network)
- Capture Tool: Wireshark
- Protocol: DNS over UDP

## Objective
To analyze DNS queries and responses and identify indicators consistent with DNS tunneling behavior.

## Assumptions
- Traffic is generated intentionally for lab purposes
- No external internet access is available
- No real domains or production data are involved

## Analyst Tasks
- Capture DNS traffic at the packet level
- Correlate DNS queries with responses
- Analyze DNS flags, response codes, and query structure
- Document findings in an investigation report

