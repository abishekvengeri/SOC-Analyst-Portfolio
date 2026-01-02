# Analysis Notes

## Purpose of the Detection
Cross-Site Scripting (XSS) attacks occur when attackers inject JavaScript or HTML elements into a request with the intention of executing code in a victim’s browser. 
XSS attempts often appear directly in log files through suspicious URI strings.

The goal of this detection is to highlight these suspicious URI patterns early, before a malicious redirect or injection impacts users.

## What was Detected
The query captured requests containing:
- JavaScript <script> tags
- <img> tags with onerror handlers
- attempts to load external .js resources

These indicators match common patterns used during XSS probing and exploitation.

## Dashboard Panel
A dashboard panel titled “XSS Attempts” was added to the SOC Web Monitoring dashboard. This provides a quick overview of:
- when XSS-like payloads appear
- which IP addresses generated them
- how frequently the patterns occur

## Report
A summary search was saved as a table-based report titled **“XSS Analysis.”** 
The report shows counts grouped by client IP and URI, making it useful for follow-up investigation or correlation with other logs.

