# Analysis Notes

## Dashboard purpose
This dashboard gives SOC analysts quick visibility into web traffic patterns that often precede attacks: scanning, probing, and targeted admin access attempts. It is intended to be open on the SOC console for near-real-time awareness.

## What each panel reveals
- Top Client IPs: identifies IPs generating the most requests. Unusual spikes can indicate a bot or scanning source.
- 404 Errors Over Time: repeated 404 spikes suggest automated probing where attackers try many paths to find a valid endpoint.
- Admin Path Access: direct hits to `/admin` or `/wp-admin` are a high-priority signal; these are common entry points for CMS attacks.
- Live Events: shows recent requests for quick triage and drilldown.

## How to triage an alert from this dashboard
1. If a client IP appears in Top Client IPs with a high request rate, click through to see URI patterns.
2. If the 404 chart shows sudden spikes, identify the IPs responsible and check for repeated patterns.
3. For any admin path access, verify if the request is legitimate (internal IP, known crawler) or suspicious (external, uncommon UA, repeated attempts).
4. Correlate with other sources: firewall logs, GeoIP, and threat intelligence for the client IP.

## Quick hunting queries
- List recent requests from a suspicious IP:
  `index=main sourcetype=access_combined clientip=<ip> | table _time uri_path status useragent`
- Check for brute-force-like patterns on admin path:
  `index=main sourcetype=access_combined uri_path IN ("/admin*", "/wp-admin*") | stats count by clientip | sort - count`

