---
title: "Braintrust"
type: entity
tags: [company, evals, observability, agent-quality]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-26
---

## Definition
Braintrust is an agent quality platform built on two main pillars: evals (pre-production experimentation to build confidence) and observability (post-production monitoring to maintain confidence). It started ~3 years ago as an evals-only platform and expanded into observability after noticing customers piping production traffic into evals.

## Key Information
- Self-described as an "agent quality platform"
- Two pillars: evals and observability, treated as the same problem from a systems perspective
- Started as an evals-only platform ~3 years ago (circa 2023)
- Added observability after a customer was running massive evals every hour against production traffic
- Built a custom domain-specific language called BTQL (later deprecated) for stitching data sources
- Used an open-source data warehouse plus DuckDB in the browser for client-side aggregation
- Customers include Notion, which sends large volumes of unstructured trace data
- Handles multimodal traces (audio, video) by storing in object storage and referencing in trace views
- Supports prompt management (optionally)
- Has a blog post about their data architecture for handling trace data

## Related
- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — source
- [[PhilHetzel]] — solutions engineering lead
- [[EvalPlatforms]] — the problem space they operate in
- [[EvalFlywheel]] — the observability-evals loop they advocate
- [[AgentQualityPlatform]] — the platform category
- [[BTQL]] — their deprecated query language
- [[DuckDB]] — technology used in their architecture
- [[Notion]] — customer example
