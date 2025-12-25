# Investigation Report: DNS Tunneling Inspection

## Executive Summary
This investigation analyzed DNS traffic captured in an isolated lab environment. The analysis identified DNS queries and corresponding responses that exhibit characteristics consistent with DNS tunneling techniques, including endpoint-initiated queries and non-successful DNS responses. These findings demonstrate how DNS can be abused for covert communication.

---

## Scope
- Protocol: DNS over UDP
- Client IP: 192.168.56.101
- DNS Server IP: 192.168.56.102
- Capture Environment: Isolated Host-Only virtual network

---

## Methodology
- Network traffic was captured using Wireshark on the Kali Linux VM.
- Display filter `dns` was applied to isolate DNS packets.
- DNS queries were correlated with responses using transaction IDs and frame references.
- DNS flags, response codes, and transport behavior were analyzed.

---

## Timeline of Events

| Frame | Time (UTC) | Direction | Description |
|------|-----------|----------|------------|
| 104 | 04:18:10.324718 | Client → Server | DNS standard query |
| 105 | 04:18:10.324772 | Server → Client | DNS response (REFUSED) |

---

## Packet Analysis Findings

### DNS Query (Frame 104)
- Source IP: 192.168.56.101
- Destination IP: 192.168.56.102
- Protocol: UDP
- Destination Port: 53
- Transaction ID: 0x0002
- Questions: 1

The query originated from an endpoint and targeted an internal DNS server.

---

### DNS Response (Frame 105)
- Source IP: 192.168.56.102
- Destination IP: 192.168.56.101
- Response Code: **REFUSED**
- Flags: `0x8185`
- Answer Records: 0
- Response Time: 0.000054330 seconds

The DNS server refused the request, which is a common response pattern observed in DNS tunneling scenarios.

---

## Indicators of Suspicious DNS Activity

| Indicator | Observation |
|----------|------------|
| Endpoint-initiated DNS queries | Present |
| DNS over UDP | Present |
| Non-successful DNS responses | REFUSED observed |
| Clear-text protocol | Present |
| Internal DNS misuse | Possible |

---

## MITRE ATT&CK Mapping

| Technique ID | Technique Name |
|-------------|----------------|
| T1071.004 | Application Layer Protocol: DNS |
| T1048.003 | Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol |

---

## Impact Assessment
DNS tunneling enables attackers to bypass traditional security controls and covertly transmit data. Even when DNS queries fail, the query structure itself can be leveraged to transfer encoded data.

---

## Conclusion
The analyzed DNS traffic demonstrates a complete DNS query-response exchange exhibiting characteristics consistent with DNS tunneling techniques. The presence of REFUSED responses does not negate tunneling risk; instead, it reinforces the need for behavioral DNS inspection.

---

## Recommendations
- Monitor DNS query length and entropy
- Alert on repeated non-successful DNS responses
- Log DNS activity centrally
- Implement anomaly-based DNS detection controls

