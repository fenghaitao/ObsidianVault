---
title: "DuckDB"
type: entity
tags: [tool, database, analytics, in-browser]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-26
---

## Definition
DuckDB is an in-process analytical database (often called "SQLite for analytics"). Braintrust used DuckDB running in the browser as a third level of aggregation for trace data, on top of their open-source data warehouse and BTQL stitching layer.

## Key Information
- In-process OLAP database, runs embedded (including in-browser via WebAssembly)
- Used by Braintrust for client-side aggregation of trace data
- Part of Braintrust's three-tier data architecture: open-source data warehouse → BTQL stitching → DuckDB in-browser aggregation
- This architecture worked for a while but didn't support full-text search across traces, which customers like Notion needed

## Related
- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — source
- [[Braintrust]] — company using DuckDB
- [[BTQL]] — query language used alongside DuckDB
- [[TraceDataChallenges]] — the problem DuckDB helped address
