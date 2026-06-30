---
title: "ClickHouse"
type: entity
tags: [technology, database, olap, analytics]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition

ClickHouse is an open-source column-oriented OLAP database management system. Braintrust previously used ClickHouse as their database backend before building their own custom database (Brainstorm) specifically for agent traces.

## Key Information

- Open-source columnar OLAP database designed for analytical queries
- Braintrust used ClickHouse before migrating to a custom-built database
- Migration was driven by the need for text-based indexing (full-text search across traces) which ClickHouse could not provide at the time
- Agent trace workloads require both fast point reads (viewing a single trace instantly) and analytical queries (SQL aggregation, filtering) plus full-text search — a combination not well served by traditional OLAP solutions
- Illustrates that agent observability creates a new systems problem not addressed by existing database technologies

## Related

- [[summary-20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust]] — source
- [[Braintrust]] — company that migrated away from ClickHouse
- [[Tantivy]] — text indexing framework that ClickHouse lacked
- [[TextBasedIndexing]] — the missing capability that drove the migration
- [[AgentTraceData]] — the data type requiring specialized database design
- [[SingleStore]] — database company where Braintrust's founder previously worked
