---
title: "Postmortems"
type: concept
tags: [incidents, operations, learning, reliability, AWS]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker.md"]
last_updated: 2026-09-14
---

## Definition

A postmortem (called a "Correction of Errors," or COE, at Amazon) is a written analysis of an incident that digs past the proximal cause through layered "whys" to produce fixes at multiple levels and to surface recurring patterns across incidents.

## Key Information

- Marc Brooker read roughly 3,000–4,000 industry postmortems and Amazon COEs over his career.
- AWS holds a broad weekly meeting where engineers and senior leaders across the company review COEs and apply the lessons; Brooker calls this mechanism a "core, almost causal" factor in AWS's success — a "fundamental learning exercise."
- A great postmortem first verifies what actually happened (if you can't, that itself teaches you about logging/metrics/observability/simulation gaps), then steps through the "whys" at multiple levels, and produces concrete action items at the code, testing, and social/team-process levels before surfacing cross-incident patterns.
- Avoid two failure modes: insufficient focus on outcomes (standards can intentionally vary by area — e.g., durability gets the highest bar), and normalization of "operational heroics" (a heroic break-fix cycle that never fixes root causes).
- Rote on-call ticket closing should be automated; deep experts' time belongs on the unexpected, with lessons communicated broadly.

## Related

- [[summary-20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker]] — source summary
- [[Marc Brooker]] — the source of this framing
- [[On-Call]] — where postmortem material originates
- [[Caching]] — a recurring design lesson from postmortems
- [[Metastable Failures]] — an underlying cause across major postmortems
- [[AWS]] — where the weekly COE review runs
