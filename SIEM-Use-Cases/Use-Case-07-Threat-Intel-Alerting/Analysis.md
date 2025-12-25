# Analysis Notes

## Purpose of the Alert
Threat intelligence becomes much more valuable when automated alerting is enabled. 
This alert allows SOC analysts to be notified anytime a High or Medium severity IP from the TI feed appears in live web traffic.

## How It Works
The alert enriches Apache logs using the threat_intel lookup and filters for High or Medium severity indicators. These are the most actionable threats and typically require immediate triage.

## Testing
To validate the alert:
- I generated requests from the IPs listed in the mock threat feed.
- The alert triggered correctly and displayed the results in the Triggered Alerts panel.
- The output included client IP, URI accessed, status codes, and the corresponding threat description.

This confirms that Splunk is able to correlate logs with threat intelligence and notify analysts reliably.

