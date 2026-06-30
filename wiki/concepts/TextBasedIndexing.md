---
title: "Text-Based Indexing"
type: concept
category: data-engineering
tags: [full-text-search, indexing, agent-traces, tantivy, database]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition

Text-based indexing is the capability to perform full-text search across agent traces, enabling queries like "find every trace containing the word Amazon." It is a requirement unique to agent observability — traditional observability tools do not need to index unstructured text within traces — and is a primary reason existing OLAP databases like ClickHouse could not serve agent trace workloads.

## Key Information

- Enables natural-language-like queries across agent traces: find all traces matching a keyword, phrase, or pattern in any unstructured text field
- Makes intuitive sense for agent observability because traces contain extensive natural language (prompts, completions, reasoning chains, tool outputs) that users want to search
- Braintrust implemented this via Tantivy, a Rust-based full-text search framework similar to Apache Lucene, forked and integrated into their custom Brainstorm database
- Traditional OLAP databases (ClickHouse) lacked this capability at the time Braintrust needed it, driving the decision to build a custom database
- Part of a three-component custom database architecture: write-ahead log (immediate ingestion) + indexing layer (analytical queries) + text-based index (full-text search), all unified through SQL
- A completely new systems problem — text search was never a consideration in traditional observability database design

## Related

- [[summary-20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust]] — source
- [[Tantivy]] — the Rust-based framework implementing text-based indexing
- [[AgentTraceData]] — the data type requiring text-based indexing
- [[AgentObservability]] — the paradigm driving the need for this capability
- [[TraditionalObservability]] — the paradigm that never needed text indexing
- [[ClickHouse]] — OLAP database that lacked this capability
- [[Braintrust]] — company that implemented text-based indexing in Brainstorm
