# SOC Investigation Report
## Incident: Sysmon Activity Analysis — Lab Simulation

### 1. Executive Summary
On [Lab Date], Sysmon logs from host **DESKTOP-0S2K0MN** were collected and analyzed to validate endpoint visibility and to demonstrate detection of standard suspicious behaviors (process creation, encoded PowerShell, network calls, file and registry modifications). All observed events align with controlled lab actions and show no indications of malicious compromise.

---

### 2. Data Sources
- `sysmon-activity.csv` — processed Sysmon event export (converted from EVTX for analysis)
- Sysmon configuration: SwiftOnSecurity community config (applied prior to simulation)

---

### 3. Key Findings
**Host:** DESKTOP-0S2K0MN  
**Primary Observations:**
- **Process Creation (Event ID 1):** Multiple interactive processes started (examples: Notepad, Calculator, Paint) consistent with manual activity during the lab.
- **Network Connections (Event ID 3):** Outbound HTTP(S) connection attempts initiated by PowerShell/curl to external domains (used to simulate web requests).
- **File Creation (Event ID 11):** A test file `C:\Users\Public\sysmon_test.txt` was created as part of the lab steps.
- **Registry Modification (Event ID 13):** A test registry key was added under `HKCU\Software\TestKey`.
- **Encoded PowerShell Execution:** An encoded PowerShell command was executed (encoded command string observed in the command-line field). In some runs it generated an error; in others it executed a benign echo command. Sysmon captured the full command line for visibility.

No indicators of:
- Lateral movement (no remote SMB/NTLM authentication or suspicious network logon types observed).
- Persistence mechanisms (no suspicious autorun entries, scheduled tasks, or service installs observed in this dataset).
- Data exfiltration attempts (no large or unusual outbound connections identified in the sample).

---

### 4. Analysis & Interpretation
The event sequence and attributes (ProcessName, CommandLine, TimeCreated, and origin host) show expected behavior for the controlled test run. The encoded PowerShell event is noteworthy for demonstration purposes — encoded commands are high-fidelity detections because they often indicate obfuscated scripts, but in this lab they were intentionally executed to validate detection coverage.

Because the recorded network calls and processes were launched interactively from the host and were limited to benign test actions, the evidence points to **controlled lab activity** rather than an adversary operation.

---

### 5. Impact Assessment
- **Risk Level:** Low (lab-generated, no compromise).
- **Affected Systems:** DESKTOP-0S2K0MN only (no evidence of spread or network compromise).
- **User Impact:** None identified.
- **Business Impact:** None (test environment).

---

### 6. Recommendations
1. **Retain Event Context** — keep full command-line and parent process context (Sysmon config is correctly capturing these fields). This is critical for future investigations.
2. **Alert Tuning** — create or validate detection rules for:
   - Encoded PowerShell/ScriptBlock usage (alert on suspicious base64 or IEX usage).
   - Unknown process spawning from common hosts (e.g., unexpected svchost child processes with unusual command lines).
   - File creation in common public directories when combined with suspicious network activity.
3. **Hunting Query Examples** (Splunk / Elastic / Sigma-style):
   - Search for `EventID=1` where `CommandLine` contains `-EncodedCommand` or `IEX`.
   - Search for `EventID=3` for outbound connections originating from non-standard processes.
4. **Follow-Up Actions**:
   - For production systems: correlate Sysmon events with firewall logs to identify suspicious external endpoints.
   - For repeated encoded PowerShell in production: escalate for deeper forensic analysis and possible rollback.

---

### 7. Conclusion
The Sysmon dataset for this lab confirms that endpoint telemetry is functioning and capturing high-value fields (command line, parent process, network connection data). The observed encoded PowerShell and test activities demonstrate proper visibility; no malicious activity was observed in this controlled test dataset.


