---
title: "Caching"
type: concept
tags: [distributed-systems, performance, databases, reliability]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker.md"]
last_updated: 2026-09-14
---

## Definition

Caching exploits temporal and spatial locality to make systems faster, but in distributed systems it introduces a metastable failure mode where an empty or wrong cache leaves the back end unable to handle the un-cached traffic.

## Key Information

- Brooker "prefers to see the teams around me avoiding caching where possible," while stopping short of an absolute rule.
- Preferred alternatives: a complete materialized view of slow-moving data (pull it fully into memory and make copies), a scalable backend (DynamoDB or similar) while pushing your database vendor on scale, or a "complete cache" that holds every row (D SQL's storage tier).
- Aurora warms failover targets by having the leader continuously tell them what to cache, so a failover doesn't start cold.

## Related

- [[summary-20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker]] — source summary
- [[Marc Brooker]] — the source of the warning
- [[Metastable Failures]] — the downside of caches
- [[Amazon DynamoDB]] — a scalable backend alternative
- [[Amazon Aurora]] — warm-cache failover design
- [[Multi-Version Concurrency Control]] — the lock-free alternative design
