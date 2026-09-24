---
title: "ClickHouse"
type: entity
tags: [database, column-store, olap]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260916 - Creator of Postgres (Turing Award)： ＂One Size Fits None＂, Leveraging GPUs, Difficult Implementations.md"]
last_updated: 2026-09-23
---

## Definition

ClickHouse is an open-source column-store database that Michael Stonebraker cites as a modern example of a specialized engine beating a one-size-fits-all system.

## Key Information

- Stonebraker names ClickHouse as a column store, evidence that the "one size fits none" thesis still holds for specialized engines.
- It is offered as a contrast to Postgres, which has not implemented a column store and so is not competitive on sizable data warehouses.

## Related

- [[summary-20260916 - Creator of Postgres (Turing Award)： ＂One Size Fits None＂, Leveraging GPUs, Difficult Implementations]] — source summary
- [[Michael Stonebraker]] — cites it as a column store
- [[Column Store]] — its storage layout
- [[Vertica]] — earlier column-store pioneer
- [[PostgreSQL]] — which lacks a column store
- [[One Size Does Not Fit All]] — the thesis it illustrates
- [[Databases]] — the field
