# Analysis Notes

## Purpose of the Alert
The goal of this alert is to automatically detect SQL injection attempts in real time. Instead of manually searching the logs, the alert monitors the data continuously and highlights suspicious requests as soon as they appear.

## Why These Parameters?
Attackers often include parameters like "id=", "query=", or "search=" when they try to manipulate backend SQL queries. These patterns are simple but effective indicators of reconnaissance or attempted exploitation.

## Alert Behavior
I configured the alert to:
- run every 5 minutes
- look back at the previous 5 minutes of activity
- trigger if the search returns any results

This ensures that any suspicious activity is captured quickly.

## Testing the Alert
I generated sample SQL injection-like requests from the browser and command line. The alert successfully triggered, and the activity appeared in the "Triggered Alerts" section in Splunk Enterprise.

This confirmed that the alert configuration was working correctly.

