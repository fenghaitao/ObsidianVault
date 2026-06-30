---
title: "Agent Trace Data"
type: concept
category: data-engineering
tags: [agent-traces, observability, semi-structured, database, text-indexing]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition

Agent trace data is the observability data produced by AI agent runs, characterized by being semi-structured, highly voluminous (gigabyte-scale individual traces), and containing massive amounts of unstructured text. These characteristics make agent trace data fundamentally different from traditional observability data and require specialized database architectures to ingest, index, and query.

## Key Information

- **Semi-structured**: Mix of structured spans (model calls, tool calls) and massive unstructured text within each span
- **Voluminous**: Individual agent traces can exceed a gigabyte; individual spans can be 20MB — orders of magnitude larger than traditional observability spans (typically a few KB)
- **High velocity**: Production traffic generates traces at the same speed as traditional observability, requiring true real-time ingestion
- **Dual read patterns**: Must support both fast point reads (viewing a specific trace instantly after it occurs) and analytical queries (SQL filtering, aggregation, full-text search)
- **Text-heavy**: Unlike traditional traces which contain primarily structured metrics, agent traces contain extensive unstructured natural language (prompts, completions, reasoning chains, tool outputs)
- Creates a new systems problem not addressed by traditional OLAP databases like ClickHouse — driving the need for custom databases with write-ahead logs, text-based indexing (Tantivy), and SQL unification
- Braintrust built Brainstorm, a custom database from the ground up, specifically for this data type

## Related

- [[summary-20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust]] — source
- [[AgentObservability]] — the observability paradigm built around this data
- [[TracesAndSpans]] — the building blocks (traces and spans) that compose this data
- [[TextBasedIndexing]] — the indexing approach required to query unstructured text within traces
- [[WriteAheadLogForTraces]] — WAL pattern for immediate trace ingestion
- [[Tantivy]] — text indexing framework used for full-text search across traces
- [[ClickHouse]] — OLAP database unable to handle this data type
- [[Braintrust]] — company that built a custom database for this data
