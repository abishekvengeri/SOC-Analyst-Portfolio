# Folder 2 – Sysmon Analysis

This section contains Sysmon installation steps, configuration details, and attack simulations used for endpoint detection.

## Sysmon Setup Summary
- Sysmon downloaded from Microsoft Sysinternals
- Configuration: SwiftOnSecurity sysmonconfig.xml
- Installed using:
  Sysmon64.exe -accepteula -i sysmonconfig.xml

## Next Steps
- Generate suspicious activity logs
- Analyze Event IDs (1, 3, 7, 11, etc.)
- Create reports based on observed Sysmon data
