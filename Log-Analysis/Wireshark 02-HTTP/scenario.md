# Scenario: Clear-Text HTTP Request Analysis in an Isolated Network

## Background
A SOC analyst is investigating internal network traffic to understand how unencrypted HTTP communication appears at the packet level. The analyst has been asked to analyze a suspected web request sent from an internal endpoint to a local web service.

Understanding HTTP request structure is critical for detecting credential leakage, malicious downloads, and suspicious web activity.

## Environment
- Client Host: Windows 10 Pro VM (192.168.56.101)
- Web Server: Kali Linux VM (192.168.56.102)
- Network Type: Host-Only (VM-only, isolated)
- Web Service: Python HTTP Server on TCP port 8080
- Capture Tool: Wireshark

## Objective
To capture and analyze an HTTP request transmitted in clear text and document its network and application-layer characteristics.

## Assumptions
- Traffic is generated intentionally for lab purposes
- No encryption (HTTPS) is in use
- No real credentials or production data are involved

## Analyst Tasks
- Identify HTTP request packets
- Analyze TCP and HTTP headers
- Confirm client-server roles
- Document findings in a structured investigation report

