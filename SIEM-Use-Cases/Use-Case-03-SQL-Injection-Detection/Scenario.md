# Use Case 03 – SQL Injection Detection in Apache Web Logs

This lab simulates SQL injection attempts against an Apache web server and shows how Splunk can be used to detect and analyze these events. 
The Apache logs were forwarded from an Ubuntu VM using the Splunk Universal Forwarder and indexed in Splunk Enterprise.

SQL injection attempts often include suspicious query strings such as:
- id= 
- query=
- search=
- or other parameters used to manipulate database queries

In this exercise, I created a search to detect these patterns, added a dashboard panel to visualize the attacks, and generated a report summarizing the findings.

