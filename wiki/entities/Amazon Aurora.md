---
title: "Amazon Aurora"
type: entity
tags: [product, database, AWS, relational]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker.md"]
last_updated: 2026-09-14
---

## Definition

Amazon Aurora is AWS's relational database product family; Aurora Serverless brings serverless scaling, and Aurora D SQL ("D SQL") is a serverless SQL database built with S3 as the durability layer and designed so misbehaving clients cannot hold locks and cause outages.

## Key Information

- Brooker joined Aurora after hearing customers wanted relational data that fit serverless/container workloads; the team built Aurora Serverless and then "the sequel" (D SQL).
- The database trend of block storage becoming the default durability layer shaped D SQL: it makes the S3 object store the underlying durability layer and builds an architecture on top for the latency/interface an online database needs.
- D SQL has no pessimistic locking — reads use multi-version concurrency control (per-row version histories), and commits use optimistic checks, so readers never block writers and vice versa.
- The storage overhead of keeping old row versions is typically under ~10% for online workloads because writes are concentrated.
- The Aurora leader continuously tells potential failover targets what to cache so a failover target's cache is already warm.

## Related

- [[summary-20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker]] — source summary
- [[Marc Brooker]] — led the Aurora Serverless and D SQL work
- [[AWS]] — the provider
- [[Amazon S3]] — the durability layer under D SQL
- [[Multi-Version Concurrency Control]] — the D SQL concurrency mechanism
- [[Caching]] — the warm-failover-cache design
- [[Databases]] — the broader field
