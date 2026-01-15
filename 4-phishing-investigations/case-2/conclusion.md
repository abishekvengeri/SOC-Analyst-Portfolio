# Conclusion

The domain echallaxzc[.]vip was confirmed to be part of phishing infrastructure based on:

- newly registered domain lifecycle
- rapid suspension status (clientHold)
- consistent NXDOMAIN results across public DNS resolvers (takedown evidence)
- threat intelligence classification as phishing/fraud
- historical IP attribution to cloud hosting infrastructure
- infrastructure pivoting to ASN AS132203 (Tencent Cloud / QCloud / ACEVILLE)
- identification of multiple related domains (echalla*/echallan*) resolving to the same IP (101.33.78.145)

## Final Assessment
This is a phishing campaign cluster using bulk-registered domains and shared cloud hosting.
The infrastructure indicates a short-lived operation designed to rotate domains quickly
to bypass detection and blocking.

## Recommended Defensive Actions
- Block:
  - echallaxzc[.]vip
  - all related domains from related-domains.txt
  - IP 101.33.78.145 (if permitted)
- Monitor:
  - DNS reactivation of currently dead domains in the cluster
- User awareness:
  - Do not click unknown links
  - Verify all login requests through official domains only

