# Sysmon Logs – Processed CSV File

This folder contains the Sysmon log data used for the endpoint monitoring and threat detection analysis in Folder 2 of the SOC Analyst Portfolio.

## Included File
- **sysmon-activity.csv** – A processed CSV file containing Sysmon event data (such as process creation, network connections, registry modifications, and DNS queries).  
  The CSV was generated from a Windows Sysmon log export and converted for easier analysis.

## Event Types Included
The CSV contains Sysmon events generated through:
- Process execution (Event ID 1)  
- Network connections (Event ID 3)  
- File creation (Event ID 11)  
- Registry modifications (Event ID 13)  
- DNS queries (Event ID 22)  
- Encoded PowerShell execution (suspicious activity)

