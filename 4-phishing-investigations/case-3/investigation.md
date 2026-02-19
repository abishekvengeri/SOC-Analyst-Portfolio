# Investigation Details

## 1) WHOIS Analysis

Domain: priavahuen.icu
Creation Date: 2026-01-30
Registrar: Gname.com Pte. Ltd.
Domain Status: serverHold
Nameservers:
- A4.SHARE-DNS.COM
- B4.SHARE-DNS.NET

Assessment:
Newly registered domain with registry-level suspension (serverHold).

---

## 2) DNS Verification

dig @8.8.8.8 priavahuen.icu A

Result: NXDOMAIN

Interpretation:
Domain does not resolve to an IP address.
DNS removal consistent with phishing takedown.

---

## 3) HTTP Verification

curl -Ivk https://priavahuen.icu/i

Result:
Could not resolve host

Confirms DNS non-resolution and inactive status.

---

## 4) Impersonation Analysis

The domain visually mimics the official Parivahan portal:

Official: parivahan.gov.in  
Suspicious: priavahuen.icu

This is a classic typosquatting technique.

---

## 5) Threat Assessment

Indicators suggest:
- Short-lived phishing deployment
- Brand impersonation
- Registry-level suspension after abuse reporting
