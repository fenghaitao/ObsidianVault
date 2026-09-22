---
title: "Granola"
type: entity
tags: [project, distributed-systems, transactions, thesis]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md"]
last_updated: 2026-09-22
---
## Definition
Granola is James Cowling's PhD work at MIT: an algorithm for distributed transaction coordination focused on "one-shot" (or "independent") transactions that could commit atomically across shards without two-phase commit/two-phase locking.
## Key Information
- Pre-dated Google's Spanner and was cited in the Spanner paper, though Spanner subsequently overshadowed it.
- Key idea: for independent transactions where participants run as pure functions over independent state, all that's needed is to serialize them by efficiently exchanging timestamps and choosing the maximum — avoiding the coordination/blocking costs of two-phase commit.
- Motivated by the belief that performance comes from eliminating points of coordination, not raw hardware speed.
- Built and benchmarked in an era before cloud was easy: used a rack of servers at MIT and the communal PlanetLab testbed, sleeping by his desk to catch free nodes.
- Part of Cowling's broader interest in "how to design simple models/APIs for complex problems" and large-scale transactional systems.
## Related
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[James Cowling]] — author
- [[Google Spanner]] — the system that superseded it
- [[Two-Phase Commit]] — the approach it avoids
- [[Distributed Systems]] — the field
- [[Transactions]] — the abstraction it coordinates
