# SIEM Use Case 1: Failed Logon Brute Force Detection

## 1. Description
This use case detects repeated failed logon attempts from the same source within a short time period.  
This is a common brute-force attack pattern seen across Windows environments.

## 2. Log Source
- Windows Security Logs
- Event ID: 4625 (Failed logon)
- Event ID: 4624 (Success, used for correlation)

## 3. Attack Indicators
- Multiple failed logons targeting the same account
- Failures coming from the same source IP
- High frequency in a short time window

## 4. Detection Goal
Identify brute-force attempts before the attacker successfully authenticates.

## 5. MITRE ATT&CK Mapping
- **Technique:** T1110 – Brute Force

## 6. Expected Alerts
Alerts should trigger when:
- 5 or more failed logons occur from the same IP within 1 minute  
OR  
- Any account experiences abnormal failed logon volume compared to baseline

