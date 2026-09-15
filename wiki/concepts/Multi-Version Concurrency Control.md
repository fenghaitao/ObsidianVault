---
title: "Multi-Version Concurrency Control"
type: concept
tags: [databases, concurrency, transactions, distributed-systems]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker.md"]
last_updated: 2026-09-14
---

## Definition

Multi-version concurrency control (MVCC) stores a history of versions per database row so that a reader can read an old version without blocking writers, enabling lock-free reads.

## Key Information

- Aurora D SQL stores a version history per row; reads use MVCC so "a reader of a piece of data" never blocks writers and a writer never blocks readers.
- Combined with commit-time optimistic checks, D SQL has no pessimistic locking; writers can still prevent other writers from committing by changing data, which is inherent to the chosen isolation level.
- The overhead of keeping old versions is surprisingly small — usually under ~10% for online workloads — because write traffic concentrates on relatively few rows.

## Related

- [[summary-20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker]] — source summary
- [[Amazon Aurora]] — where D SQL uses MVCC
- [[Caching]] — the blocking problem MVCC avoids
- [[Databases]] — the broader field
- [[Marc Brooker]] — describes the mechanism
