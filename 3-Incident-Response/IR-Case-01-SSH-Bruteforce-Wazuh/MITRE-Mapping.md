# MITRE ATT&CK Mapping

Wazuh automatically tagged the detection with the following MITRE techniques:

| Technique ID | Name                        | Tactic             |
|--------------|------------------------------|--------------------|
| T1110        | Brute Force                  | Credential Access  |
| T1110.001    | Password Guessing            | Credential Access  |
| T1021.004    | Remote Services: SSH         | Lateral Movement   |

Reasoning:
- T1110 & T1110.001: triggered by repeated invalid password attempts.
- T1021.004: SSH was the attack vector used for lateral movement attempts.

The MITRE view in the Wazuh dashboard confirmed these mappings.

