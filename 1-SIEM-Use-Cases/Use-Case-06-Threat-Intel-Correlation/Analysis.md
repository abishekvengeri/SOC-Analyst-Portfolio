# Analysis Notes

## Objective
This use case demonstrates how a SOC analyst can integrate threat intelligence feeds into Splunk to enrich log data. Correlating Apache logs with known malicious IPs helps identify higher-risk activity quickly.

## Lookup Configuration
The file-based lookup `threat_intel.csv` was uploaded through Splunk’s Lookup Manager and configured as:
- Lookup definition name: threat_intel
- Permissions: Read for all apps, Write for admin

This allowed Splunk to match incoming client IPs against known malicious indicators.

## Detection
The search successfully enriched Apache logs with:
- threat_level (High, Medium, Low)
- description (botnet activity, phishing source, suspicious behavior)

The correlation revealed IPs from the threat feed when they appeared in live traffic.

## Dashboard Panel
A dashboard panel titled “Threat Intel Alerts” was added to the SOC Web Monitoring dashboard. It highlights High and Medium risk IPs and displays their associated activity.

This allows SOC analysts to focus on potentially harmful connections without manually reviewing raw logs.

