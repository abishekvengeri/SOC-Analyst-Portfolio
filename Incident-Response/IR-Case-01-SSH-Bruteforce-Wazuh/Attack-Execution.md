# Attack Execution

A brute-force attack was simulated using Hydra from a Kali Linux machine targeting the Ubuntu server’s SSH service.

Command used:
hydra -l soc -P /usr/share/wordlists/rockyou.txt ssh://192.168.x.x

Hydra attempted thousands of login combinations against user 'soc'. The repeated authentication failures were logged in /var/log/auth.log and journald.

Wazuh agent installed on the Ubuntu server captured these events and forwarded them to the Wazuh Manager.

