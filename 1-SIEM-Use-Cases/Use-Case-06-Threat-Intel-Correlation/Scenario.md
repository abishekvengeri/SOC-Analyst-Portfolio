# Use Case 06 – Threat Intelligence Correlation in Splunk

This lab focuses on integrating a mock threat intelligence (TI) feed into Splunk and correlating it with Apache web server logs. The goal is to detect malicious or suspicious IP addresses by enriching incoming log data with external threat context.

The Apache access logs were forwarded from an Ubuntu VM. 
A custom threat feed called `threat_intel.csv` was created with fields:
- ip_address
- threat_level
- description

Example entries included High, Medium, and Low severity indicators such as botnet IPs and phishing sources.

The threat feed was uploaded as a lookup table and mapped to the `clientip` field in Apache logs. A dashboard panel was added to the "SOC Web Monitoring" dashboard to highlight any matches in real time.

