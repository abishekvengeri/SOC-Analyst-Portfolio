# Detection Summary

Wazuh successfully detected multiple reconnaissance indicators from the Apache access logs.

Wazuh Agent:
- Agent name: soc
- Log source: /var/log/apache2/access.log
- Decoder used: web-accesslog

Example parsed alert:
{
  "rule.id": "31151",
  "rule.level": 10,
  "rule.groups": ["web", "accesslog", "web_scan", "recon"],
  "rule.description": "Multiple web server 400 error codes from same source ip.",
  "rule.mitre.id": "T1595.002",
  "data.srcip": "192.168.1.x",
  "data.protocol": "PROPFIND",
  "data.url": "/"
}

Rules triggered:
- 31101 – Web server 400 error (Level 5)
- 31121 – Web server 501 error (Level 4)
- 31151 – Multiple error codes from same IP (Level 10)

Rule 31151 was the most critical, marking automated scanning activity.

