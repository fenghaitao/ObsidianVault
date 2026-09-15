---
title: "Eventual Consistency"
type: concept
tags: [distributed-systems, databases, concurrency, consistency]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker.md"]
last_updated: 2026-09-14
---

## Definition

Eventual consistency is a concurrency-control model where replicas update asynchronously and converge later. Google pushed it from on high, and Mike Stonebraker (with the database community) rejected it for sacrificing correctness.

## Key Information

- Google's motivation: a distributed commit across east/west replicas costs extra round trips, so update asynchronously and let replicas "eventually settle out."
- Failure mode: two warehouses simultaneously sell the last widget → inventory −1, violating the integrity constraint (stock > −1); only acceptable if overselling is allowed (e.g., Amazon's 24-hour shipping), which most enterprises can't tolerate.
- Google later "completely abandoned" eventual consistency (and MapReduce) when Spanner shipped a conventional transactional system, per Jeff Dean.
- Stonebraker frames it as "performance versus data integrity" — if you don't care about your data, you'll deal with bad things happening.

## Related

- [[summary-20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker]] — source summary
- [[Michael Stonebraker]] — who rejected it
- [[Google]] — who pushed it
- [[Jeff Dean]] — credited with ending it
- [[Google Spanner]] — the transactional replacement
- [[MapReduce]] — the other Google approach he disputed
- [[Distributed Systems]] — the field of the trade-off
