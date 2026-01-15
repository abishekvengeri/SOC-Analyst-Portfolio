# Case 1 – Phishing Investigation (delhoseoca[.]net)

## Summary
This case documents the investigation of a suspicious phishing link reported via email.  
The goal of the investigation was to validate whether the domain was malicious and to identify any associated infrastructure indicators (domain lifecycle, DNS status, historical hosting, and cloud provider attribution).

All indicators are provided in a **defanged format** to prevent accidental access.

---

## Initial Indicator
- Reported URL: `hxxps://delhoseoca[.]net/in`

---

## Key Findings

### Domain Registration & Lifecycle
- Domain: `delhoseoca[.]net`
- Creation Date: **2025-10-14**
- Registrar: **NameMart Pte. Ltd.**
- Status: **clientHold** (domain suspended)

The domain was registered recently and suspended shortly after, which is consistent with phishing infrastructure.

---

### DNS / Takedown Evidence
- DNS status observed: **NXDOMAIN**
- Interpretation: DNS records were removed (domain taken down after abuse reports)

This suggests a short-lived phishing operation (register → attack → takedown).

---

### Historical Hosting & Infrastructure Attribution
Historical records showed the domain previously resolved to:

- Historical IP: `43.155.136.247`
- ASN: `AS132203`
- Provider: **ACEVILLE PTE. LTD. (Tencent Cloud / QCloud)**
- WHOIS country field: **KR (South Korea)**
- Abuse contact: `abuse@tencent.com`

This indicates the phishing content was hosted on temporary cloud infrastructure, commonly used in short-lived phishing campaigns.

---

## Files Included
- `investigation.md` – Step-by-step technical investigation notes
- `iocs.txt` – Extracted Indicators of Compromise (IOCs)
- `conclusion.md` – Final assessment and recommended actions

---

## Responsible Use
This investigation was conducted for **defensive security learning and documentation**.
No phishing pages were opened in a normal browser and no unauthorized access was performed.
All shared indicators are defanged to avoid misuse.
