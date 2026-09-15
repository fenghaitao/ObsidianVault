---
title: "summary-20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker.md"]
last_updated: 2026-09-14
---

## Core Summary

Marc Brooker, an AWS Distinguished Engineer, argues that hands-on proximity to running systems — especially ~15 years of on-call and reading roughly 3,000 postmortems/COEs — is what produces real engineering judgment and reveals which problems actually matter. He explains that great postmortems push past the proximal cause through layered "whys" into concrete fixes, and that caches carry a metastable failure mode best avoided by design choices like complete materialized views and D SQL's multi-version concurrency control.

On the future, Brooker predicts the changing economics of AI/agentic development will shift software careers toward finding important problems and understanding customer/business context, and he urges both junior and senior engineers to stay hands-on rather than coasting on titles.

## Key Points

- The direction of your work matters more than its volume: impact comes from shipping the right thing, found by going broad across customer signals, technical trends (faster networks/storage, multi-core, GPUs), and larger world trends.
- Customer excitement about serverless/containers plus the technical trend of block storage becoming the durability layer collided to produce Aurora Serverless and Aurora D SQL, with S3 as the underlying object store.
- Brooker stayed on-call ~15 years because on-call and deeply analyzing postmortems/COEs is where he learned distributed systems in practice; AWS runs a broad weekly meeting to review COEs across the company.
- A great postmortem first verifies what actually happened (or exposes gaps in logging/metrics/observability), then steps through layered "whys," and yields concrete action items at the code, testing, and organizational levels before surfacing cross-incident patterns.
- Two failure modes of weak postmortem culture: insufficient focus on outcomes (standards can intentionally vary by area), and normalization of "operational heroics" — a heroic break-fix cycle that never addresses root causes.
- Caches exploit temporal/spatial locality but have a metastable failure mode (cache full vs. empty/wrong); D SQL's storage tier is a "complete cache" holding every row, and Brooker prefers complete materialized views or scalable backends (e.g., DynamoDB) over caching.
- D SQL avoids misbehaving-client, lock-holding outages via no pessimistic locking: multi-version concurrency control (per-row version histories) plus commit-time optimistic checks, so readers never block writers and vice versa; the storage overhead for old row versions is typically under ~10%.
- On AI, software has been supply-constrained and its economics are changing; careers will span a craft/hobby tier, a shrinking "old way" (analog-electronics analogy), and the mainstream (agentic/AI/specification-driven development).
- Juniors should learn to find problems that matter and understand customers/business early; seniors must get hands-on and use the new tools, or their opinions become "fiction."
- Writing scales expertise's impact in space and time and forces mental clarity; the "Four Hobbies and Apparent Expertise" 2x2 (doing vs. discussing × hobby vs. gear) suggests a ~75/25 practitioner/communicator balance, and long-term it's better to be underrated than overrated.
- Book picks: Martin Kleppmann's Designing Data-Intensive Applications, Hennessy & Patterson's computer architecture, and quantitative systems design; old foundational work (Erlang's telephony queueing) still has leverage.
- Admires Al Vermeulen (early AWS/S3 contributor, ex-Amazon CTO) for working deeply at every level; advice to his younger self: be bolder about changing teams/organizations (~4 vs. an optimal ~5–6).

## Related

- [[Marc Brooker]] — the guest
- [[AWS]] — his employer for ~two decades
- [[Amazon Aurora]] — the database work he led
- [[Amazon S3]] — the object store behind D SQL
- [[AWS Lambda]] — where serverless customer signals began
- [[Amazon DynamoDB]] — scalable backend he names over caching
- [[Al Vermeulen]] — the engineer he admires
- [[Martin Kleppmann]] — author he recommends
- [[Postmortems]] — the learning practice central to the episode
- [[Metastable Failures]] — the cache failure mode
- [[Caching]] — the pattern he urges avoiding
- [[On-Call]] — where his distributed-systems knowledge came from
- [[Multi-Version Concurrency Control]] — the D SQL mechanism
- [[Four Hobbies and Apparent Expertise]] — his 2x2 framework
- [[AI and Software Engineering]] — his view of the field's future
- [[Software Engineering]] — the changing practice
- [[Distributed Systems]] — the systems he reasons about
- [[Career Growth]] — junior/senior advice
- [[Writing as Leverage]] — his writing philosophy
