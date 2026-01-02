# Use Case 07 – Threat Intelligence Alerting in Splunk

This use case focuses on creating an automated Splunk alert that detects when IP addresses from a threat intelligence lookup table appear in Apache web logs.

The threat feed (threat_intel.csv) contains indicators labeled as High, Medium, or Low threat. 
This alert specifically monitors for High and Medium severity IPs, as these are most relevant for SOC triage.

The alert runs every 5 minutes, checks for matches from the last 5 minutes, and triggers when any malicious IP is observed. The triggered results appear in Splunk's Triggered Alerts section.

