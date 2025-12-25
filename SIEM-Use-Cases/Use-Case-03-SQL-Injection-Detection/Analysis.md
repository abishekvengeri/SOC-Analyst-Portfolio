# Analysis Notes

## Objective
The goal was to detect SQL injection attempts by identifying unusual query parameters commonly abused in SQL payloads. These requests often appear during reconnaissance or active exploitation attempts.

## Method
I created a detection query targeting specific URI patterns such as:
- id=
- query=
- search=

These parameters are often manipulated during SQL attacks. 
The first search listed the events along with timestamps, client IPs, URIs, and HTTP status codes. 
The second search summarized the activity to highlight the most aggressive sources.

## Dashboard Panel
I added a panel titled “SQL Injection Attempts” to the SOC Web Monitoring dashboard. 
This panel provides a quick view of suspicious query patterns and shows how often they occur and which IP addresses generated them.

## Report
I saved the summary search as a scheduled report called “SQL Injection Analysis.” 
The report presents the data as a table that can be used for further triage or escalation.

