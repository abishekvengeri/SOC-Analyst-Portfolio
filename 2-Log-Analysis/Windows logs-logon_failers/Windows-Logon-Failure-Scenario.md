# Scenario: Windows Logon Failure Investigation (Event ID 4625)

## 1. Scenario Description
A Windows workstation has reported multiple failed login attempts within a short period of time. This could indicate:
- A brute-force attack
- A user mistyping credentials repeatedly
- A malware attempting authentication
- Unauthorized access attempt

As a SOC Analyst, your task is to determine:
- The source of the failed attempts
- Whether it is intentional or malicious
- Whether the account is at risk

---

## 2. What Logs Will Be Collected
We will collect the following logs from a Windows machine:
- Security Event Logs (EVTX)
- Event ID: 4625 (Failed logon)
- Event ID: 4776 (Credential validation)
- Event ID: 1102 (Log cleared — if present)

---

## 3. Questions to Answer (Your Investigation Goals)
- Which account is being targeted?
- What is the source IP?
- How many repeated failures?
- What time did the attempts occur?
- Does the pattern look like brute force?
- Is there successful login later (Event ID 4624)?
- Is it a local or network logon?

---

## 4. Expected Output
You will produce:
- A CSV file of the logs (exported from Windows)
- A short investigation report (in `/reports`)
- Any parsing scripts (if used)

---

## 5. Tools You Will Use
- Windows Event Viewer
- PowerShell (Get-WinEvent / Get-EventLog)
- EVTX to CSV converter (if needed)
- Basic log analysis techniques

---

## 6. What This Lab Demonstrates
This lab demonstrates:
- Understanding of core Windows security logs
- SOC investigation methodology
- Ability to extract and interpret event logs
- Ability to identify suspicious authentication patterns

