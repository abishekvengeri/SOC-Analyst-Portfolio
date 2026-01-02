# Custom Script Used for Automated Alert Action

A custom script was created on the Ubuntu VM to log details of coordinated login attacks detected by Splunk.

## File Location
/usr/local/bin/log_alert.sh

## Script Contents
#!/bin/bash
LOG_FILE="/var/log/alerts.log"
TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M:%S UTC")
URI_PATH=$1
UNIQUE_IPS=$2
COUNT=$3
echo "[$TIMESTAMP] Alert for URI: $URI_PATH, Unique IPs: $UNIQUE_IPS, Failed Attempts: $COUNT" >> "$LOG_FILE"

## Permissions
sudo chmod +x /usr/local/bin/log_alert.sh

---

# Alert Action Configuration in Splunk

The script was added as a custom alert action by editing:

/opt/splunkforwarder/etc/apps/search/local/alert_actions.conf

## Entry Added
[log_alert]
is_custom = 1
label = Log Alert
icon_path = alert_icon.png
entity = [script]
command = /usr/local/bin/log_alert.sh $result.uri_path$ $result.unique_ips$ $result.count$

This allows Splunk to execute the script automatically whenever the alert fires.

