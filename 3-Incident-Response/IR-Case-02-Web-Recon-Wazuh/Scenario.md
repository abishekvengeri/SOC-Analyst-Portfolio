# IR Case 02 – Web Reconnaissance Detection Using Wazuh

This case simulates a reconnaissance phase performed against an Apache web server using the Nmap Scripting Engine (NSE). The goal was to generate unusual HTTP requests and error responses that Wazuh could detect, classify, and map to MITRE ATT&CK techniques.

The attack was executed from a Kali machine against an Ubuntu server running Apache2 with the Wazuh agent installed. This test validates Wazuh's capability to recognize early attacker behaviors, such as directory probing and method enumeration.

