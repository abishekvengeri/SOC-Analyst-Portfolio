# Incident Report – Failed Logon Brute Force Attempt

## 1. Summary
A brute-force pattern was detected involving multiple failed logon attempts targeting one or more user accounts. The activity originated from a single IP address and occurred within a short time window.

## 2. Affected System(s)
- Windows Domain / Workstation
- Authentication Service (Event ID 4625 logs)

## 3. Timeline
- Several 4625 events occurred between [first_time] and [last_time]
- No successful login (4624) was observed afterward

## 4. Observations
- Repeated failures against the same username
- Same source IP involved in all attempts
- Frequency suggests an automated or scripted attack

## 5. Analysis
The behavior matches known brute-force attack patterns.  
No legitimate business process produces this level of failed logon activity in such a short period.

## 6. Impact
- No confirmed unauthorized access
- No data exposure observed
- Account remains locked or unaffected

## 7. Response Actions Taken
- Account status reviewed
- Source IP checked against threat intelligence feeds
- No escalation required based on results

## 8. Recommendations
- Implement lockout threshold policies if not already in place
- Monitor for similar activity in the next 24 hours
- Educate users on password hygiene
- Ensure MFA is enabled for all external access

## 9. Conclusion
A brute-force attempt was detected and contained. No further malicious activity associated with this alert has been observed.

