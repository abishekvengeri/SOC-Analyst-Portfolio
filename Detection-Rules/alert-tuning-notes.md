# Alert Tuning Notes – Encoded PowerShell

## Why Tune This Alert?
Encoded PowerShell is a high-quality detection signal.  
However, **not all encoded commands are malicious**.

## Common False Positives
1. Automation scripts created by system administrators  
2. Deployment tools (SCCM, Intune, custom installers)  
3. Internal IT scripts that use encoding for formatting or whitespace handling  
4. Pen-testing labs (training environments)

## Tuning Recommendations
- Allowlist known admin tools and automation systems  
- Filter out commands issued by:
  - SYSTEM
  - Trusted service accounts
- Add thresholds:
  - More than 2 encoded commands in 5 minutes  
  - Unusual parent process (e.g., WINWORD.exe → suspicious)
- Correlate with:
  - Network connections (Event ID 3)
  - File creations (Event ID 11)
  - Registry persistence attempts (Event ID 13)
  - DNS queries to suspicious domains (Event ID 22)

## High-Risk Indicators
Trigger escalation if you see:
- Encoded command + downloading file  
- Encoded command + writing to startup folders  
- Encoded command launched by:
  - Excel  
  - Word  
  - wscript  
  - mshta  
  - svchost (rare, suspicious)

## SOC Action
1. Review the full PowerShell command line  
2. Identify the user account and parent process  
3. Check for related logs (network, registry, file writes)  
4. Ask system owner whether activity was intentional  
5. Escalate if:
   - No explanation provided  
   - Lateral movement indicators appear  
   - Persistence mechanisms follow the event

