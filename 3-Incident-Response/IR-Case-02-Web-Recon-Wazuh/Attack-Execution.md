# Attack Execution

The reconnaissance scan was performed using Nmap with multiple HTTP NSE scripts:

Command used:
nmap -p 80 --script http-enum,http-methods,http-errors,http-headers 192.168.x.x

Purpose:
- Trigger 404, 405, and 501 HTTP responses
- Force Apache to log uncommon methods (PROPFIND, OPTIONS, etc.)
- Simulate directory enumeration and probing commonly seen during recon

Examples of generated log entries:
- PROPFIND / HTTP/1.1" 405 521 "-"
- GET /.git/HEAD" 404 453 "-"
- POST /sdk" 404 453 "-"
- GET /HNAP1" 404 453 "-"

