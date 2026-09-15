---
title: "PostgreSQL"
type: entity
tags: [database, open-source, relational, SQL]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker.md"]
last_updated: 2026-09-14
---

## Definition

PostgreSQL (Postgres; transcribed in the episode as "Postgress"/"Postcrest") is the open-source relational database created by Michael Stonebraker's team, known for its extensible type system.

## Key Information

- Engineered with an extendable type system so users could add efficient custom data types (also called abstract data types or stored procedures) — the main point of Postgres.
- Also supported inheritance (wanted by AI researchers at the time) and time travel, which was later removed because the implementation "sucked."
- Stonebraker sees Postgres as the right low-end "one-size-fits-all" default — free, huge community, easy to find talent — but it lacks a column store and multi-node support, so it isn't competitive on sizable data warehouses.
- Postgres replaced MySQL as the preferred open-source relational database after Oracle acquired MySQL.

## Related

- [[summary-20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker]] — source summary
- [[Michael Stonebraker]] — the creator
- [[Ingres]] — the predecessor system
- [[MySQL]] — the database it displaced as open-source default
- [[Oracle]] — the acquisition that pushed users to Postgres
- [[Databases]] — the broader field
- [[One Size Does Not Fit All]] — where Postgres is the low-end default
