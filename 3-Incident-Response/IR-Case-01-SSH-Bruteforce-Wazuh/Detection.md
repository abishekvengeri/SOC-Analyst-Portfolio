# Detection Summary

Wazuh successfully detected and classified the brute-force activity. The following rules fired:

| Rule ID | Level | Description                               | Trigger Count | Source IP      |
|---------|--------|--------------------------------------------|----------------|-----------------|
| 5760    | 5      | sshd: authentication failed               | 3900+          | 192.168.x.x     |
| 5758    | 8      | Maximum authentication attempts exceeded  | 700+           | 192.168.x.x     |

Key points:
- Rule 5760 captures individual failed SSH login attempts.
- Rule 5758 escalates severity when too many failures occur in a short time window.
- Events appeared in the Wazuh Dashboard under the sshd and authentication_failed rule groups.
- Logs were parsed from both /var/log/auth.log and journald.

Screenshots included:
- task2-ssh-bruteforce-alerts.png
- task2-mitre-filter.png

