---
title: "Databases"
type: concept
tags: [databases, relational, distributed-systems, SQL]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260916 - Creator of Postgres (Turing Award)： ＂One Size Fits None＂, Leveraging GPUs, Difficult Implementations.md"]
last_updated: 2026-09-23
---

## Definition

Databases are systems for storing, querying, and managing structured data. Mike Stonebraker's career spans relational systems (Ingres, Postgres) and specialized engines (StreamBase, Vertica, DBOS), while Marc Brooker works on serverless SQL at AWS.

## Key Information

- Stonebraker's arc: Ingres (relational, 1972) → Postgres (extensible type system) → StreamBase (streams), Vertica (column store), DBOS (database as OS/programming runtime).
- The query optimizer is the hardest part of a database to implement.
- Referential integrity is an integrity constraint (e.g., inventory > −1) that permissive concurrency models like eventual consistency can violate.
- Marc Brooker: relational databases were still operationally "serverful" relative to serverless/containers; the current trend is block storage becoming the default durability layer, and Aurora D SQL uses MVCC plus commit-time optimistic checks to avoid lock-holding outages.
- Stonebraker (September 2026) on GPUs for databases: GPUs are SIMD, "the anathema of indexing" — B-tree lookups serialize — and a GPU bolted onto a CPU often bottlenecks on the connecting bus.

## Related

- [[summary-20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker]] — source summary
- [[Michael Stonebraker]] — the database pioneer
- [[PostgreSQL]] — his extensible relational system
- [[Ingres]] — his first system
- [[Query Optimizer]] — the hard part
- [[One Size Does Not Fit All]] — his core thesis
- [[Eventual Consistency]] — the rejected concurrency model
- [[summary-20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker]] — source summary
- [[Marc Brooker]] — on serverless SQL trends
- [[Multi-Version Concurrency Control]] — the D SQL mechanism
- [[Amazon Aurora]] — AWS's serverless SQL database
