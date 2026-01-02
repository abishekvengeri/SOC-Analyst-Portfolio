# Analysis Notes

The behavior observed aligns with early-stage reconnaissance:

- Enumeration of directories and hidden paths
- Probing for .git directories and SDK endpoints
- Use of uncommon HTTP verbs (PROPFIND, OPTIONS)
- Automated scanning pattern identified by error codes and frequency

Wazuh demonstrated strong detection capabilities by:
- Parsing Apache logs consistently
- Alerting with rule levels 4, 5, and 10 based on severity
- Applying MITRE Technique T1595.002 automatically
- Highlighting the originating IP for triage

