---
title: "CVSS"
type: concept
tags: [security, scoring, vulnerability, standards]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - State of the Claw — Peter Steinberger.md"]
last_updated: 2026-06-26
---

## Definition
CVSS (Common Vulnerability Scoring System) is a standardized framework for rating the severity of security vulnerabilities on a scale of 0 to 10. It has been criticized for producing scores that don't reflect practical risk, especially when applied to vulnerabilities in permissive subsystems that aren't actually used.

## Key Information
- Peter Steinberger gave a concrete example: a CVSS 10 (maximum severity) issue in OpenClaw where an iPhone app with read-only permission could break the system to get write permission
- "In all practical ways it is not even an incident" because the permissive model it exploits isn't used by anyone — "nobody's even using that"
- "The rules of how you create the CVSS numbers don't contribute to [practical risk] at all. And I try to play by the rules. So it is a 10 out of 10."
- "The world is going crazy over incidents that in all practical ways will not affect people"
- CVSS scores don't account for: whether the vulnerable feature is actually used, whether the default/recommended setup is vulnerable, or whether exploitation requires actively fighting the recommended configuration
- Belgium's cybersecurity agency issued an alert about an OpenClaw RCE that was actually a feature requiring a non-default, non-recommended setup
- The scoring system incentivizes sensationalism: researchers get "credits" for high-severity findings regardless of practical impact

## Related
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — source
- [[OpenClaw]] — project affected by misleading CVSS scores
- [[PeterSteinberger]] — critic of CVSS practical applicability
- [[AI-Generated Security Reports]] — related problem of inflated severity claims
