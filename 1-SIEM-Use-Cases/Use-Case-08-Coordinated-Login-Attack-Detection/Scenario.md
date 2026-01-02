# Use Case 08 – Coordinated Login Attack Detection with Custom Alert Action

This use case focuses on detecting coordinated login attacks against a web application and automating a response using a custom script. The goal is to identify situations where multiple unique IP addresses are attempting to access the same URI path within a short time window.

To achieve this, I created a Splunk alert that monitors Apache access logs and triggers when both conditions are met:
- more than 2 unique IPs target the same URI path
- more than 5 total attempts occur within the time range

A custom script was added as a custom alert action. When the alert fires, Splunk calls the script and logs the event to a local file on the Ubuntu VM for further analysis or integration with other tools.

This lab demonstrates automated detection and response using Splunk.

