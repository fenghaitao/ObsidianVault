---
title: "Query Optimizer"
type: concept
tags: [databases, SQL, algorithms, performance]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker.md"]
last_updated: 2026-09-14
---

## Definition

The query optimizer is the database component that decides how to execute a SQL query. Mike Stonebraker calls it the hardest part of a database to implement.

## Key Information

- "What was the hardest part of that implementation? Query optimizer. It's tough. It's just algorithmically difficult."
- "If you ask most any senior database programmer what's the hardest part, they'll still say the optimizer."
- Stonebraker's text-to-SQL approach for heterogeneous sources (SQL, CAD, text) ultimately does a join "with what amounts to a query optimizer."

## Related

- [[summary-20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker]] — source summary
- [[Michael Stonebraker]] — the source of the claim
- [[Databases]] — the component's home
- [[Text-to-SQL]] — where he reuses the optimizer
- [[PostgreSQL]] — a database with its own optimizer
