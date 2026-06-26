---
title: "Trace Data Challenges"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-26
---

## Definition

Trace Data Challenges refers to the unique data infrastructure problems posed by LLM agent traces, which differ fundamentally from traditional application traces. These challenges make building eval and observability platforms a systems problem, not just a UI/UX problem.

## Key Information

### Four Dimensions of Difficulty

1. **Velocity**: Production traffic generates traces at high speed — high ingestion rates required
2. **Size**: Individual spans can be 10-20MB (vs. traditional spans at a few KB). A single trace can be 1GB. Cramming these into a Postgres row causes severe performance issues.
3. **Structure**: Semi-structured to unstructured. Heavy on text — LLM problems inherently involve large amounts of natural language. Traditional structured databases struggle.
4. **Query Diversity**: Two distinct query patterns must be supported:
   - Low-latency point queries for viewing individual traces (observability use case)
   - Aggregate analytics for trend analysis (eval use case)
   - Full-text search across traces (functional requirement from customers like Notion)

### Why It's Novel

None of these problems are individually unique, but together they create a novel systems challenge. Traditional approaches (relational databases, data warehouses, in-browser analytics) each solve parts but not the whole. Braintrust's original architecture (open-source data warehouse + BTQL stitching + DuckDB in-browser) worked temporarily but failed when customers needed full-text search.

## Related

- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — source
- [[Braintrust]] — company facing these challenges
- [[EvalPlatforms]] — the platform context
- [[AgentObservability]] — the observability context
- [[DuckDB]] — technology used in one attempted solution
- [[BTQL]] — deprecated query language for this problem
- [[Postgres]] — traditional database that struggles with trace data
