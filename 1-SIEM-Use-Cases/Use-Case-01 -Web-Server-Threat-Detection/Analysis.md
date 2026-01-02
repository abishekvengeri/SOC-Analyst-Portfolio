# Analysis Notes

## 1. 404 Error Activity
The first search focused on identifying which IP addresses generated the most 404 responses. 
High volumes of 404s usually suggest enumeration attempts where someone is trying to find valid directories or files by guessing paths.

During the search, I looked at:
- the client IP sending the requests
- which paths were being checked
- how frequently the errors occurred

This helped me understand whether the behavior was normal traffic or potential scanning.

## 2. Admin Path Requests
The second search looked for direct attempts to reach administrative pages such as /admin or /wp-admin. 
These locations are common targets when attackers try to find login portals or attempt CMS-related attacks.

This search made it clear which IPs were trying to access these sensitive paths, and how often the requests appeared. 
This type of activity usually indicates reconnaissance before a brute-force attack or vulnerability exploitation.

