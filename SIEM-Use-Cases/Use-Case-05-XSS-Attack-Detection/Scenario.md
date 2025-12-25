# Use Case 05 – XSS Attack Detection in Apache Web Logs

This use case focuses on detecting Cross-Site Scripting (XSS) attempts targeting a web application hosted on an Apache server. 
Apache access logs were forwarded to Splunk Enterprise using the Splunk Universal Forwarder.

XSS payloads commonly include HTML or JavaScript elements such as:
- <script>
- <img onerror=...>
- references to .js files

In this lab, I created a detection query to identify suspicious URI patterns, added the results to the SOC Web Monitoring dashboard under "XSS Attempts", and generated a summary report showing which IP addresses generated the most suspicious traffic.

