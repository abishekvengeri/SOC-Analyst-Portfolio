# Investigation Details

## 1) Initial Phishing Indicator
Reported phishing URL:
- hxxps://echallaxzc[.]vip/in


## 2) Domain Registration (WHOIS)
Domain: echallaxzc.vip

Key findings:
- Creation Date: 2025-12-15T17:05:00Z
- Registrar: Domain International Services Limited (wdomain.com)
- Domain Status: clientHold (suspended)
- Name Servers:
  - ns1.domainnamedns.com
  - ns2.domainnamedns.com

Assessment:
- Newly registered domain + fast suspension is consistent with phishing infrastructure.


## 3) DNS Resolution (Live Check)
Public DNS resolver checks:

- dig @8.8.8.8 echallaxzc.vip A  -> NXDOMAIN
- dig @1.1.1.1 echallaxzc.vip A  -> NXDOMAIN

Interpretation:
- The domain does not currently exist in DNS (likely taken down).
- The NXDOMAIN result was consistent across public resolvers, confirming this was not a local DNS issue.


## 4) Threat Intelligence Confirmation
Threat intelligence categorization indicated:
- Category: Phishing and Other Frauds
- Intel visibility window:
  - First Submission: 2025-12-16 04:49:10 UTC
  - Last Submission: 2025-12-16 06:21:02 UTC

This short activity window matches typical phishing domain lifecycle:
register -> attack -> report -> takedown


## 5) Historical DNS / Hosting
Historical serving IP address observed:
- 101.33.78.145

HTTP behavior observed (intel source):
- Final URL: https://echallaxzc.vip/
- Status Code: 404
- Server fingerprint:
  - Server: GoFrame HTTP Server
  - Via: 1.1 Caddy

Note:
- A 404 response does not indicate benign behavior.
  Many phishing kits only serve content when conditions match (victim geo, UA, referrer, session).


## 6) Infrastructure Pivot (IP -> ASN -> Provider)
WHOIS for 101.33.78.145 indicated:

- ASN: AS132203
- Provider: ACEVILLE PTE. LTD. (Tencent Cloud / QCloud)
- Region/Country (WHOIS field): KR (South Korea)
- Abuse contact: abuse@tencent.com

Assessment:
- Hosting on cloud infrastructure is commonly used for short-lived phishing campaigns.
- Infrastructure reuse may indicate repeat attacker deployment pattern.


## 7) Related Domain Cluster (Campaign Evidence)
By pivoting on infrastructure / passive DNS data, multiple related domains were identified.
DNS check using Google public resolver (8.8.8.8) confirmed several were alive and pointing
to the same hosting IP.

Alive domains (resolved to 101.33.78.145):
- echallann.vip
- echallaoc.cc
- echallaov.icu
- echallanu.vip
- echallanzs.vip

Dead/not resolving at time of check:
- echalp.vip
- echallanr.vip
- echallanm.vip
- echalu.vip
- echallanv.vip

Conclusion:
- This naming pattern (echalla*/echallan*) and shared hosting strongly indicates
  a phishing campaign using bulk domain registration and infrastructure reuse.

