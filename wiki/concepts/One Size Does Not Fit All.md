---
title: "One Size Does Not Fit All"
type: concept
tags: [databases, architecture, design, trade-offs]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker.md"]
last_updated: 2026-09-14
---

## Definition

One Size Does Not Fit All is Mike Stonebraker's thesis (from a 2004 paper, with a talk behind it) that a single general-purpose database design is suboptimal, and that specialized engines each beat it by an order of magnitude for their workload.

## Key Information

- Stream processing (StreamBase), column stores for data warehouses (Vertica), and row stores are "wildly different implementations" with "no resemblance to each other," each an order of magnitude faster when architected for its workload.
- Still true today: ClickHouse (column store) and Pinecone (vector) specialize successfully, and a common parser can sit on top of multiple implementations.
- Postgres hasn't added a column store or multi-node support, so it's not competitive on sizable data warehouses.
- The exception: at the low end, Postgres is the right "one size fits all" default until you need ~a million transactions/second or a petabyte-scale warehouse.

## Related

- [[summary-20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker]] — source summary
- [[Michael Stonebraker]] — the thesis's author
- [[PostgreSQL]] — the low-end default
- [[StreamBase]] — the stream engine example
- [[Vertica]] — the column-store example
- [[Databases]] — the field it critiques
