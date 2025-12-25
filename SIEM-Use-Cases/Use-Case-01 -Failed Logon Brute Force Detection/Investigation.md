# Investigation Workflow – Failed Logon Brute Force

## 1. Alert Trigger
Alert fires when:
- 5+ failed logons from the same IP within 1 minute, OR
- An account shows abnormal failed logon volume

## 2. Initial Steps
1. Verify the alert is genuine by checking:
   - Source IP
   - Target username
   - Timestamps of failed attempts
2. Check if the username exists in Active Directory.
3. Compare activity to the user’s baseline behavior.

## 3. Enrichment
- Look up the source IP in:
  - Firewall logs
  - VPN logs
  - Threat intelligence databases
- Check whether the account is:
  - Disabled
  - Admin-level
  - Service account

## 4. Key Questions
- Is the source IP internal or external?
- Is the user currently active at this time?
- Are there successful logon events (4624) after the failures?
- Does the pattern look scripted or human?

## 5. Escalation Conditions
Escalate to Tier 2 if:
- The source IP is external
- A successful login occurs after failures
- Password spray pattern detected
- The account is privileged (Domain Admin, Helpdesk Admin, etc.)

## 6. Recommended Actions
- Temporarily lock the affected account
- Block the source IP if malicious
- Notify the user or IT support
- Reset account password if compromise is suspected

## 7. MITRE Mapping
- **T1110 – Brute Force**

