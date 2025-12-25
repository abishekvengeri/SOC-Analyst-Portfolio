# Threat Intelligence Alert Configuration

**Alert Name:** High/Medium Threat IP Alert  
**Description:** Alert for detecting high or medium threat IPs from threat_intel.csv in Apache access logs.

This alert is designed to automatically notify the SOC when known malicious or suspicious IP addresses are observed in live web traffic. The alert uses a lookup-based correlation search and triggers when any High or Medium threat-level indicators appear.

---

## Search Used
index=main sourcetype=access_combined
| lookup threat_intel ip_address AS clientip OUTPUT threat_level, description
| where threat_level="High" OR threat_level="Medium"
| table _time, clientip, uri, status, threat_level, description
| sort - _time

---

## Alert Type
Scheduled Alert

---

## Scheduling
- **Run every:** 5 minutes  
- **Time range:** Last 15 minutes  

This ensures the alert captures any IPs from the threat feed that appear in recent activity.

---

## Trigger Conditions
- **Trigger when:** Number of results > 0  
- **Trigger mode:** Once per scheduled run  

The alert fires only when a High or Medium threat-level IP is detected.

---

## Permissions
- **Shared in App:** search  
- Visible to all roles within the app as read-only  
- Writable by admin  

---

## Trigger Actions
- Add to **Triggered Alerts** in Splunk Web

This allows analysts to review alert details directly through Splunk’s alert management interface.

---

## Testing
After configuring the alert, I generated simulated traffic from IPs included in the threat_intel.csv file.  
The alert successfully triggered and appeared in the Triggered Alerts panel with the enrichment fields included.

Screenshots are provided in the Screenshots folder:
- `ti_alert_configuration.png`
- `ti_alert_triggered.png`

