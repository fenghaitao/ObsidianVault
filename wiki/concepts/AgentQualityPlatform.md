---
title: "Agent Quality Platform"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition

An Agent Quality Platform is a category of tools that ensure AI agent reliability through two main pillars: evals (pre-production experimentation to build confidence) and observability (post-production monitoring to maintain confidence). Braintrust self-identifies as this category of platform.

## Key Information

- **Two pillars**: Evals (before production) + Observability (in production)
- **Unified view**: Treats evals and observability as the same problem from a systems perspective
- **Flywheel**: Connects production insights back to offline experimentation for continuous improvement
- **Multi-persona**: Serves engineers, SMEs, product managers, and non-technical stakeholders
- **Data challenges**: Must handle high-velocity, large, semi-structured trace data with diverse query patterns
- **Beyond UI**: Growing use cases for headless/programmatic interaction via coding agents
- **Custom database**: Braintrust built Brainstorm, a custom database from the ground up, because existing OLAP solutions (ClickHouse) could not handle the text-based indexing, write-ahead log, and dual read pattern requirements of agent traces
- **Text indexing**: Full-text search across traces via Tantivy (Rust-based, similar to Apache Lucene) — a capability absent from traditional observability databases
- **Topic modeling**: Automated embedding and clustering of agent traces to surface user intent, sentiment, and failure modes without manual review

## Related

- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — source
- [[summary-20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust]] — source
- [[Braintrust]] — example platform in this category
- [[EvalPlatforms]] — closely related concept
- [[EvalFlywheel]] — the core operational model
- [[AgentObservability]] — one of the two pillars
- [[OnlineEvals]] — production-side quality assessment
- [[OfflineEvals]] — pre-production quality assessment
- [[Tantivy]] — text indexing framework used in Brainstorm database
- [[ClickHouse]] — OLAP database Braintrust moved away from
- [[TextBasedIndexing]] — full-text search requirement for agent traces
- [[TopicModelingForAgents]] — automated trace clustering feature
