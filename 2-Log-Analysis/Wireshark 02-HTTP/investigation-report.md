# Investigation Report: HTTP Request Analysis

## Executive Summary
This investigation analyzed an HTTP request captured in an isolated virtual lab environment. The packet analysis confirms that a Windows client transmitted a clear-text HTTP request to a local web server over TCP port 8080. The observed traffic aligns with normal HTTP request behavior and highlights the visibility of unencrypted application-layer data.

---

## Scope
- Protocol: HTTP over TCP
- Client IP: 192.168.56.101
- Server IP: 192.168.56.102
- Destination Port: 8080
- Capture Environment: Isolated Host-Only virtual network

---

## Methodology
- Traffic was captured using Wireshark on the Kali Linux VM.
- Display filter `http` was applied to isolate HTTP traffic.
- Packet headers across Ethernet, IP, TCP, and HTTP layers were analyzed.

---

## Timeline of Observed Event

| Frame | Time (UTC) | Direction | Description |
|-----|----------|----------|------------|
| 92 | 14:53:32.304898 | Client → Server | HTTP request transmitted |

---

## Packet Analysis Findings

### Network Layer Observations
- Source IP: 192.168.56.101
- Destination IP: 192.168.56.102
- TTL: 128 (consistent with Windows OS behavior)
- No fragmentation observed

---

### Transport Layer Observations
- Source Port: 62935 (ephemeral)
- Destination Port: 8080
- TCP Payload Length: 448 bytes
- Connection State: ESTABLISHED
- No retransmissions or resets observed

---

### Application Layer Observations (HTTP)
- Protocol: HTTP (clear text)
- Request transmitted without encryption
- Full visibility into HTTP headers
- No authentication headers observed

This packet represents a standard HTTP request issued by a client to retrieve web content.

---

## Security Observations

| Observation | Security Impact |
|-----------|---------------|
| Clear-text HTTP | Application data visible to packet capture |
| No encryption | Susceptible to interception |
| Internal service | Potential lateral visibility risk |

---

## Impact Assessment
The observed traffic is legitimate; however, the use of clear-text HTTP exposes application-layer data to any entity capable of packet capture on the network.

---

## MITRE ATT&CK Mapping
- Not applicable
- Activity represents standard protocol communication

---

## Conclusion
The analysis confirms that the client transmitted an HTTP request in clear text to a local web service. This lab demonstrates how HTTP traffic can be fully inspected at the packet level and serves as a baseline for detecting insecure web communication.

---

## Recommendations
- Enforce HTTPS where sensitive data is involved
- Monitor HTTP traffic for credential leakage
- Use this baseline to detect malicious web requests or downloads

