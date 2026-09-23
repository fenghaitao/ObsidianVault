---
title: "FMEA (Failure Mode and Effects Analysis)"
type: concept
tags: [reliability, risk, threat-modeling, Dropbox]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling.md"]
last_updated: 2026-09-22
---
## Definition
FMEA (Failure Mode and Effects Analysis) is a threat-modeling/pre-mortem process that inventories every possible failure, its likelihood, and severity, then designs around those failure modes. Dropbox used it to harden Magic Pocket.
## Key Information
- Cowling describes it as a big spreadsheet where you write down "every bad thing that could possibly happen" and how bad it would be — including existential risks like a data-center fire or someone dying.
- It functioned as "almost a pre-mortem" to catalog potential failure modes and design protections against the unknowns.
- Outputs included the right amount of buffer capacity, designs to prevent congestion collapse and memory spikes, and protections against unexpected capacity losses (e.g., two delivery trucks crashing in one week).
- Cowling relishes this "rubber hits the road" firefighting work.
- Physical unknowns also appeared: two server-delivery trucks crashed in one week, costing more than two weeks — ultimately around six weeks — of lost capacity, absorbed with buffer planning rather than deleting user data.
- A fine-grained cataloged failure mode: sizing each rack's power (amps) against access patterns via the PDU circuit breaker, where a bad hardware batch could trigger extra re-replication and run racks "really hot."
## Related
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[Dropbox]] — the company that used it
- [[Congestion Collapse]] — one of the failure modes cataloged
- [[summary-20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling]] — source summary
