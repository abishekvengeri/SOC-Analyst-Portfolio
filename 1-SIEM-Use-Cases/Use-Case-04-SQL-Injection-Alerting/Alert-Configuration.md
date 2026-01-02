# SQL Injection Alert Configuration

**Alert Title:** SQL Injection Alert  
**Description:** Detects SQL injection attempts in Apache access logs based on URI patterns such as 'id=', 'query=', and 'search='.

**Search Used:**  
index=main sourcetype=access_combined uri="*id=*" OR uri="*query=*" OR uri="*search=*" 
| table _time, clientip, uri, status
| eval attack_type="SQL Injection"

**Alert Type:** Scheduled  
**Schedule:** Run every 5 minutes  
**Time Range:** Last 5 minutes  
**Trigger Condition:** Number of Results > 0  
**Permissions:** Shared in App  
**Alert Actions:** Display in Triggered Alerts

The alert triggers whenever suspicious SQL injection-like query parameters appear in Apache access logs. A screenshot of the alert configuration and a screenshot of the triggered alert are included in the Screenshots folder.

