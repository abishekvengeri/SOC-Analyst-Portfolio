# SOC Investigation Report  
## Incident: Multiple Failed Logon Attempts (Event ID 4625)

### 1. Overview
The Security Operations Center identified multiple failed logon events on the workstation **DESKTOP-0S2K0MN**. These events were captured in the Windows Security log as **Event ID 4625**. The purpose of this investigation is to understand the cause, determine if the activity is suspicious, and assess whether any further action is needed.

---

### 2. Key Findings

**• Source of Attempts:**  
All failed logins originated from the local machine itself (IP: 127.0.0.1).

**• Target Username:**  
The logs show `TargetUserName: -`, indicating that an invalid or non-existent username was entered.

**• Status & Error Codes:**  
- Status: **0xC000006D** → Bad username or authentication failure  
- SubStatus: **0xC0000380** → Username does not exist  
- FailureReason: **%%2304** → Invalid account information  

**• Logon Type:**  
LogonType **2** → Interactive login (attempts made physically at the machine, not remotely).

**• Frequency:**  
Several repeated failed attempts occurred within a short time window.

**• Process Information:**  
Authentication attempt was processed by `svchost.exe`, which is normal for Windows logon handling.

---

### 3. Analysis
The combination of:
- Local source IP (127.0.0.1)  
- Invalid username  
- Interactive logon type (2)  
- Repeated failures in quick succession  

suggests the activity is not coming from an external threat or lateral movement attempt. This pattern is typically seen when a user repeatedly enters the wrong login name or a misconfigured application or service attempts authentication.

There is **no evidence of brute-force behavior from the network**, and no successful login was observed after the failed attempts.

---

### 4. Impact Assessment
- **Risk Level:** Low  
- **Affected Account:** No valid domain or local user accounts were targeted.  
- **System Impact:** No unauthorized access occurred.  

There is no indication of compromised credentials or malicious remote activity.

---

### 5. Recommendations
1. Confirm with the user whether they attempted to log in during the recorded timeframe.  
2. Review the workstation for any applications or scripts that might be trying invalid logins.  
3. Continue monitoring for recurring 4625 events or failed logins originating from non-local IP addresses.  
4. If similar events appear with **valid usernames** or **network logon types (3 or 10)**, escalate for further investigation.

---

### 6. Conclusion
The failed logon attempts observed on **DESKTOP-0S2K0MN** appear to be non-malicious and most likely caused by incorrect username entry during interactive login. No signs of external attack, brute-force activity, or account compromise were detected.


