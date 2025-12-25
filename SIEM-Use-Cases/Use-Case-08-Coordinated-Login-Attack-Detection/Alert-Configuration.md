# Coordinated Login Attack Detection – Alert Configuration

**Alert Name:** Coordinated Login Attack Detection  
**Description:** Detects login paths targeted by multiple unique IP addresses in a short time frame.  
**Type:** Scheduled Alert  
**Permissions:** Shared in App (search)

---

## Search Used
index=main sourcetype=access_combined
| stats dc(clientip) as unique_ips, count by uri_path
| where unique_ips > 2 AND count > 5

---

## Schedule
Cron:  
0,15,30,45 * * * *  
(Runs every 15 minutes)

Time Range:  
Last 15 minutes

---

## Trigger Condition
Number of results > 0  
Trigger: Once per scheduled run

---

## Trigger Action
Custom Script Action: **log_alert**

This action sends:
- uri_path  
- unique_ips  
- count  

to the logging script configured on the Splunk Forwarder.

---

## Included Screenshots
- coordinated_alert_configuration.png  
- alert_action_configuration.png

