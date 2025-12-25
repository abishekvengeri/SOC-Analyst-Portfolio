# Executive Summary – Web Reconnaissance Detection

An external actor attempted to probe the organization’s web server as part of a reconnaissance phase. The scanning activity was detected automatically by Wazuh and classified as high-risk due to repeated access attempts to invalid endpoints and unsupported HTTP methods.

Key Findings:
- Over 400+ abnormal HTTP requests were detected.
- Requests targeted sensitive paths (/.git/, /HNAP1, /sdk).
- Automated tools were used, indicated by the User-Agent string.
- Wazuh mapped the activity to MITRE ATT&CK Technique T1595.002.

Business Impact:
Early recon detection reduces the risk of successful exploitation attempts and allows security teams to block or investigate the originating IP before further escalation.

Recommended Actions:
- Block the offending IP at the firewall or WAF.
- Enable rate-limiting for public web endpoints.
- Review Apache hardening policies and disable unnecessary HTTP methods.

