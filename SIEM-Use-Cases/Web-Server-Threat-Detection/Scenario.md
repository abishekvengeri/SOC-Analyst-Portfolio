# Web Server Threat Detection – Apache Log Monitoring

This lab focuses on monitoring Apache web server logs to identify early signs of suspicious activity. 
I set up a Splunk Universal Forwarder on an Ubuntu Desktop VM and configured it to send Apache access logs to Splunk Enterprise installed on my Windows machine.

The goal of the exercise was to practice detecting basic reconnaissance behavior, specifically:
- repeated 404 errors, which often point to directory or file probing
- requests to admin paths such as /admin or /wp-admin, which attackers frequently target when looking for login pages or misconfigured admin panels

This scenario simulates a simple SOC investigation where the analyst reviews web server activity and identifies patterns that could indicate an attacker scanning the site.

