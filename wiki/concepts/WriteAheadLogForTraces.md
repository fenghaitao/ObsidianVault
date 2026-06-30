---
title: "Write-Ahead Log for Traces"
type: concept
category: data-engineering
tags: [write-ahead-log, wal, agent-traces, database, observability, real-time]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition

A write-ahead log (WAL) for agent traces is a database component that immediately persists incoming trace data so users can see agent interactions as soon as they occur — in true real time. It is one of three core components in Braintrust's custom Brainstorm database architecture, alongside an indexing layer for analytical queries and a text-based index (Tantivy) for full-text search.

## Key Information

- Enables immediate trace visibility: when a user interacts with an agent, the trace is visible "basically instantaneously"
- Critical for agent observability because AI engineers and product managers want to see production agent behavior in real time, not after a delay
- Part of Braintrust's custom database (Brainstorm), built from the ground up for agent traces
- One of three core database components: WAL (immediate ingestion) + indexing layer (analytical queries) + text-based index (full-text search), all unified through SQL
- Addresses the dual read pattern requirement: fast point reads (WAL) for real-time trace viewing AND analytical queries (indexing) for aggregation and filtering
- A new systems requirement not addressed by traditional OLAP databases designed for batch-oriented analytical workloads

## Related

- [[summary-20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust]] — source
- [[AgentTraceData]] — the data type ingested via WAL
- [[AgentObservability]] — the paradigm driving real-time requirements
- [[Braintrust]] — company that implemented WAL in Brainstorm
- [[TextBasedIndexing]] — complementary database component for full-text search
