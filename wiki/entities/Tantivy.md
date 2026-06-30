---
title: "Tantivy"
type: entity
tags: [technology, full-text-search, indexing, rust, open-source, database]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition

Tantivy is an open-source full-text search engine library written in Rust, similar to Apache Lucene. Braintrust forked Tantivy to provide text-based indexing across agent traces, enabling users to query traces by their textual content (e.g., "find every trace containing the word Amazon").

## Key Information

- Written in Rust, analogous to Apache Lucene (Java-based)
- Provides full-text search and indexing capabilities
- Forked by Braintrust for use in their custom agent trace database (Brainstorm)
- Enables text-based queries across traces, which is a requirement unique to agent observability — traditional observability tools do not need to index unstructured text within traces
- Part of Braintrust's custom database architecture alongside write-ahead log (WAL) for immediate ingestion and SQL-based query unification
- Addresses a gap that traditional OLAP databases like ClickHouse could not handle for agent trace workloads

## Related

- [[summary-20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust]] — source
- [[Braintrust]] — company that forked and uses Tantivy
- [[TextBasedIndexing]] — the concept Tantivy implements for agent traces
- [[AgentTraceData]] — the data type Tantivy indexes
- [[ClickHouse]] — OLAP database Braintrust moved away from, partially because it lacked Tantivy-like capabilities
