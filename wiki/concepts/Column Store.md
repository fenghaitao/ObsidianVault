---
title: "Column Store"
type: concept
tags: [databases, storage, data-warehouse]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260916 - Creator of Postgres (Turing Award)： ＂One Size Fits None＂, Leveraging GPUs, Difficult Implementations.md"]
last_updated: 2026-09-23
---

## Definition

A column store is a database storage layout that organizes data by column rather than by row, specialized for data-warehouse workloads; Mike Stonebraker says a column store "looks nothing like a row store" and is an order of magnitude faster for analytics.

## Key Information

- Stonebraker's 2004 work on column stores for data warehouses was popularized by Vertica.
- A column store "looks nothing like a row store" and was an order of magnitude faster for its workload.
- Still true today: ClickHouse is a column store.
- Postgres has not implemented a column store, leaving it not competitive on sizable data warehouses.

## Related

- [[summary-20260916 - Creator of Postgres (Turing Award)： ＂One Size Fits None＂, Leveraging GPUs, Difficult Implementations]] — source summary
- [[Michael Stonebraker]] — pioneer of the approach
- [[Vertica]] — the column-store database that popularized it
- [[ClickHouse]] — a modern column store
- [[PostgreSQL]] — which lacks one
- [[One Size Does Not Fit All]] — the thesis it illustrates
- [[Databases]] — the field
