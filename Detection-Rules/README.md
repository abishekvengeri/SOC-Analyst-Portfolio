# Detection Rules

This folder contains detection engineering work created as part of the SOC Analyst Portfolio.  
Each rule demonstrates how to detect suspicious or malicious activity using different SIEM and analytics languages.

## Structure
- **sigma/** — Sigma rules (portable detection format, SIEM-agnostic)
- **splunk/** — SPL-based detection rules for Splunk
- **eql/** — Elastic Query Language rules for Elastic/ELK

## Current Rules Included
### 1. Encoded PowerShell Execution  
**Purpose:** Detect PowerShell launched with encoded or obfuscated commands.  
This is often used by attackers to hide malicious scripts.

### Coverage:
- **MITRE ATT&CK**: T1059.001 — PowerShell  
- **Sysmon Event ID:** 1 (Process Creation)

### Logic Summary:
- Trigger when `powershell.exe` or `pwsh.exe` is started AND  
- The command line contains any of:
  - `-EncodedCommand`
  - `-enc`
  - `IEX`
  - long base64 strings (obfuscation technique)

### Use Cases:
- Detect obfuscated malicious scripts  
- Detect suspicious lateral movement commands  
- Catch malware loaders that use encoded payloads  
- Identify unusual administrator activity

## Notes
These rules are designed for beginner-to-intermediate SOC analysts and match the lab scenarios generated in Folder 2 (Sysmon Analysis).

