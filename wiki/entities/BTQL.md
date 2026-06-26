---
title: "BTQL"
type: entity
tags: [tool, query-language, deprecated]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-26
---

## Definition
BTQL (Braintrust Query Language) was a custom domain-specific language created by Braintrust to stitch together two data sources — an open-source data warehouse and DuckDB in-browser aggregation — for trace data querying. It was later deprecated because nobody liked it, including the Braintrust team themselves.

## Key Information
- Custom DSL for querying across Braintrust's multi-tier data architecture
- Stitched together an open-source data warehouse and DuckDB in-browser aggregation
- Deprecated — Phil Hetzel noted "no one liked it and including us, we hated it"
- Replaced as Braintrust evolved their data architecture to handle full-text search and other functional requirements
- Illustrates the difficulty of building a query layer for semi-structured, high-velocity trace data

## Related
- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — source
- [[Braintrust]] — company that created and deprecated BTQL
- [[DuckDB]] — one of the data sources BTQL stitched together
- [[TraceDataChallenges]] — the problem BTQL attempted to solve
