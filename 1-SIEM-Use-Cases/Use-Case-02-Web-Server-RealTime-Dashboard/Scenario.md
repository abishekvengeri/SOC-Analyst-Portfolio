# Real-time Web Traffic Monitoring – SOC Dashboard

This exercise demonstrates building a real-time monitoring dashboard in Splunk Enterprise to help SOC analysts detect suspicious activity on an Apache web server.

Setup:
- Apache web server on an Ubuntu VM
- Splunk Universal Forwarder installed on the same Ubuntu VM forwarding `access.log` (sourcetype `access_combined`) to Splunk Enterprise
- Splunk Enterprise running and configured to receive forwarded data

Objective:
- Visualize top client IP addresses in real time
- Show 404 error spikes over time
- Highlight access to administrative paths (for example /admin and /wp-admin)
- Provide SOC analysts with an at-a-glance dashboard to detect reconnaissance and targeted probing

Artifacts included:
- SPL queries used to build the dashboard
- Dashboard export (XML) ready for import
- Screenshots of the running dashboard panels
- A short video demonstrating the dashboard in action

