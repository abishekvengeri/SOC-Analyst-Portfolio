# Investigation Report: TCP Three-Way Handshake Analysis

## Executive Summary
This investigation analyzed a complete TCP three-way handshake captured in an isolated virtual lab environment. The analysis confirms successful connection establishment between a Windows 10 client and a Kali Linux server. All observed packets align with standard TCP protocol behavior, and no anomalies were detected.

---

## Scope
- Protocol: TCP
- Client IP: 192.168.56.101
- Server IP: 192.168.56.102
- Destination Port: 4444
- Capture Environment: Isolated Host-Only virtual network

---

## Methodology
- Network traffic was captured using Wireshark on the Kali Linux VM.
- Display filters `tcp` and `tcp.flags.syn == 1` were applied to isolate handshake packets.
- A single TCP stream was analyzed to ensure packet correlation.
- TCP flags, sequence numbers, acknowledgment numbers, and options were examined.

---

## Timeline of Events

| Frame | Time (s) | Direction | Event |
|------|---------|---------|------|
| 31 | 233.454229458 | Client → Server | TCP SYN |
| 40 | 78.241526123 | Server → Client | TCP SYN-ACK |
| 4 | 22.275198980 | Client → Server | TCP ACK |

---

## Packet Analysis Findings

### 1. SYN Packet (Connection Initiation)
- Source IP: 192.168.56.101
- Destination IP: 192.168.56.102
- Source Port: 50294 (ephemeral)
- Destination Port: 4444
- TCP Flags: SYN
- Sequence Number: 0
- Window Size: 64240

**TCP Options Observed**
- MSS: 1460
- Window Scaling: Enabled (Scale = 256)
- SACK Permitted

This packet represents the client’s request to initiate a TCP connection.

---

### 2. SYN-ACK Packet (Server Acknowledgment)
- Source IP: 192.168.56.102
- Destination IP: 192.168.56.101
- Source Port: 4444
- Destination Port: 55406
- TCP Flags: SYN, ACK
- Sequence Number: 0
- Acknowledgment Number: 1
- Window Size: 64240

**TCP Options Observed**
- MSS: 1460
- SACK Permitted
- Window Scaling Enabled

This packet confirms that the server received the client’s SYN and is willing to establish the connection.

---

### 3. ACK Packet (Handshake Completion)
- Source IP: 192.168.56.101
- Destination IP: 192.168.56.102
- Source Port: 55202
- Destination Port: 4444
- TCP Flags: ACK
- Sequence Number: 1
- Acknowledgment Number: 1
- Window Size: 2102272

This packet completes the TCP three-way handshake, transitioning the connection state to **ESTABLISHED**.

---

## Indicators Observed

| Indicator | Observation |
|--------|------------|
| TCP SYN | Present |
| TCP SYN-ACK | Present |
| TCP ACK | Present |
| TCP Reset | Not observed |
| Retransmissions | Not observed |
| Malformed Packets | Not observed |

---

## Impact Assessment
The observed traffic represents normal TCP connection establishment behavior. No indicators of scanning, denial-of-service activity, or protocol abuse were identified.

---

## MITRE ATT&CK Mapping
- Not applicable
- Activity represents standard network protocol operation

---

## Conclusion
The TCP three-way handshake was successfully captured and analyzed. All three handshake stages were observed and validated, confirming reliable connection establishment between the client and server. This analysis serves as a baseline reference for identifying abnormal TCP behavior in future investigations.

---

## Recommendations
- Use this capture as a baseline for detecting SYN floods and failed connection attempts
- Compare future anomalous TCP traffic against this handshake behavior
- Extend analysis to include TCP teardown (FIN/ACK sequence)

