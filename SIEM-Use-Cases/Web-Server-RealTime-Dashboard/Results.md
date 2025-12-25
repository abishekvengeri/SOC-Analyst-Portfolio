# Results Summary

- Dashboard built and tested with live Apache traffic forwarded from the Ubuntu VM.
- The Top Client IPs panel identified both normal traffic and a few high-volume IPs that merited observation.
- The 404 Errors Over Time panel successfully highlighted short bursts of 404s consistent with automated probing during the test period.
- Admin Path Access panel showed targeted requests; these were investigated and classified as (a) benign crawler or (b) suspicious probing depending on user-agent, frequency, and source IP reputation.
- The dashboard video demonstrates real-time behavior and how an analyst can triage an indicator directly from the dashboard.

Recommendations:
- Add enrichment for client IPs (GeoIP, ASN, and TI hits) for faster triage.
- Add thresholds and alerts (example: >50 404s from a single IP in 10 minutes) to trigger SOC investigations automatically.
- Consider firewall or WAF block rules for confirmed malicious IPs.

