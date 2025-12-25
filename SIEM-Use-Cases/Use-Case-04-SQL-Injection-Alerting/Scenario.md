# Use Case 04 – SQL Injection Alerting in Splunk

This use case focuses on creating a Splunk alert that automatically detects SQL injection attempts in Apache web server logs.

Apache access logs from an Ubuntu VM were forwarded to Splunk Enterprise. 
SQL injection attempts usually involve suspicious query parameters such as "id=", "query=", or "search=" in the URI.

In this lab, I created a detection search, converted it into a scheduled alert, and tested the alert trigger by generating SQL injection-like payloads. The alert was configured to run every 5 minutes and trigger whenever suspicious patterns were detected.

