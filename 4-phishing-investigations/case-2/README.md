# Case 2 – Phishing Campaign Investigation (echallaxzc[.]vip Cluster)

## Summary
This case documents the investigation of a phishing URL reported via email. The investigation focused on domain lifecycle, DNS takedown evidence, historical IP attribution, hosting/ASN analysis, and campaign correlation using related domains.

All indicators are shared in a **defanged format** to prevent accidental access.

---

## Initial Indicator
- URL: `hxxps://echallaxzc[.]vip/in`

---

## Key Findings
- The domain was **newly registered** (2025-12-15).
- Domain status showed **clientHold**, indicating registrar suspension.
- DNS checks using public resolvers confirmed **NXDOMAIN** (takedown evidence).
- Historical infrastructure revealed hosting IP:
  - `101.33.78.145`
- Hosting attribution:
  - ASN: `AS132203`
  - Provider: ACEVILLE PTE. LTD. (Tencent Cloud / QCloud)
  - Abuse contact: `abuse@tencent.com`
- Multiple related domains were identified with the same naming pattern (`echalla*`, `echallan*`) and shared infrastructure.

---

## Evidence Files
- `overview.md` – High-level overview of this case
- `investigation.md` – Step-by-step investigation notes
- `iocs.txt` – Extracted Indicators of Compromise (IOCs)
- `related-domains.txt` – Related domains identified during infrastructure pivoting
- `conclusion.md` – Final assessment and recommended actions

---

## Responsible Use
This investigation is for **defensive/security education purposes only**.
No phishing content was accessed through a normal browser and no interaction with victim systems occurred.
