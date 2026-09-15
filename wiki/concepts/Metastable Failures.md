---
title: "Metastable Failures"
type: concept
tags: [distributed-systems, reliability, caching, failure-modes]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker.md"]
last_updated: 2026-09-14
---

## Definition

A metastable failure is a failure mode where a system switches into a stable "down" state from which it cannot recover on its own — for example, an empty or wrong-data cache whose back end then saturates and can never refill the cache.

## Key Information

- Caches have two modes: full-with-the-right-data (fast, healthy) and empty/wrong-data (slow, often down because the back end can't handle the un-cached traffic).
- The "down" state is stable — contention saturates the database or network so the cache can't be refilled, and the system won't come back on its own.
- Brooker says these are not common (you might go years without one), but they underlie a majority of the biggest, most impactful industry postmortems — larger-scale, longer-recovery, more complex, often requiring a painful "turn it off and on again."
- Mitigations: D SQL's storage tier is a "complete cache" containing every row; Aurora warms failover targets continuously; prefer complete materialized views or scalable backends over caches.

## Related

- [[summary-20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker]] — source summary
- [[Marc Brooker]] — describes the mode
- [[Caching]] — the trigger
- [[Postmortems]] — where the mode keeps appearing
- [[State Machine]] — the related notion of switching between states
- [[Distributed Systems]] — the context
