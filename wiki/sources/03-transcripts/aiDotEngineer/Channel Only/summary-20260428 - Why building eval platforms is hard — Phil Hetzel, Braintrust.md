---
title: "Why building eval platforms is hard — Phil Hetzel, Braintrust"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md"
author: "Phil Hetzel"
company: "Braintrust"
date: 2026-04-28
tags: [evals, observability, agent-quality, platform-engineering, llm]
---

# Why building eval platforms is hard — Phil Hetzel, Braintrust

## Core Thesis

Building eval platforms is fundamentally a systems and data problem, not just a UI/UX problem. The unique combination of high-velocity, large (10-20MB spans), semi-structured trace data with diverse query patterns — low-latency viewing, aggregate analytics, and full-text search — makes eval platforms far more complex than the spreadsheet-and-for-loop approach most teams start with. As agents become the norm for customer interactions, the stakes for getting evals right include brand risk, compliance risk, and maintenance cost.

## Key Points

### The Four Maturity Stages of Eval Platforms

1. **Spreadsheet + For Loop**: The starting point — iterating through input examples, executing an agent, recording outputs and human scores in a spreadsheet. Great for getting started but becomes cumbersome; more documentation than experimentation.

2. **Vibe-Coded UI**: Building a bespoke UI with a proper database (e.g., Neon/Postgres) for persistence. Brings more people into the fold but remains primarily a reporting/documentation tool rather than encouraging iteration.

3. **Experimentation Platform**: Adding playground features that let both technical and non-technical users tweak agent parameters (system prompts, configurations) and compare results side-by-side with automated scoring. This is where failure mode analysis begins — building scoring functions around known failure modes discovered through production traces.

4. **Observability-Integrated Platform**: Connecting production observability with offline evals to form a flywheel. Production traces reveal real user behavior and failure modes; those examples feed back into offline evals for improvement. This requires solving hard data problems: high-velocity ingestion, low-latency trace viewing, aggregate analytics, and full-text search across unstructured LLM data.

### The Eval Flywheel

Observability and evals are the same problem from a systems perspective. The loop: observe agents in production → analyze real user interactions → pull examples back into offline environment → improve agent via offline evals → redeploy. This loop should run continuously for the lifetime of the agent.

### Why the Data Layer Is the Hard Part

- **Velocity**: Production traffic generates traces at high speed
- **Size**: Individual spans can be 10-20MB (vs. traditional spans at a few KB)
- **Structure**: Semi-structured to unstructured, heavy on text
- **Query patterns**: Need both low-latency point queries (viewing a trace) and aggregate analytics (trends) plus full-text search
- **Novelty**: None of these problems are individually unique, but together they create a novel systems challenge

### Beyond the UI: Headless and Agentic Evals

A growing use case is headless evals — letting coding agents interact with the eval platform programmatically to self-heal and improve agents without human UI interaction. This requires a robust data backend that supports SQL and programmatic access.

### Future Directions

- **Topic modeling** to uncover unknown unknowns in agent usage patterns
- **Building for agents** as well as humans (coding agents consuming eval data)
- **Non-functional requirements**: role-based access control, data masking at scale
- **AI proxy/gateway** for automatic tracing so teams can't avoid instrumenting their LLMs

## Entities

- [[PhilHetzel]] — Solutions engineering lead at Braintrust, presenter
- [[Braintrust]] — Agent quality platform combining evals and observability
- [[KPMG]] — Consulting firm where Phil worked for 4 years
- [[SlalomConsulting]] — Consulting firm where Phil led the global Databricks business unit for 8 years
- [[Databricks]] — Data and AI platform; Phil led Slalom's global Databricks practice
- [[Notion]] — Productivity platform; Braintrust customer sending large volumes of unstructured trace data
- [[DuckDB]] — In-browser analytical database used by Braintrust for client-side aggregation
- [[Neon]] — Serverless Postgres provider, example of database used for eval persistence
- [[Postgres]] — Relational database; challenges with cramming large traces into rows
- [[BTQL]] — Braintrust's deprecated domain-specific query language for stitching data sources

## Concepts

- [[EvalPlatforms]] — The architecture and challenges of building platforms for LLM/agent evaluation
- [[EvalMaturityStages]] — Four-stage progression from spreadsheet to observability-integrated eval platforms
- [[EvalFlywheel]] — The continuous loop connecting production observability with offline experimentation
- [[TraceDataChallenges]] — Unique data problems of agent traces: velocity, size, structure, and query diversity
- [[PlaygroundFeature]] — UI for non-technical users to tweak agent parameters and compare results
- [[FailureModeAnalysis]] — Building scoring functions around known failure modes discovered via production traces
- [[OnlineEvals]] — Pointing scoring functions at live observability traffic for alerting
- [[OfflineEvals]] — Running evals in a safe environment, effectively rerunning production scenarios
- [[AgentQualityPlatform]] — Platform category combining evals and observability as two pillars of agent quality
- [[TopicModelingForEvals]] — Using topic modeling to uncover unknown unknowns in agent usage
- [[HeadlessEvals]] — Programmatic eval platform interaction via coding agents, not human UI
- [[AIProxyGateway]] — Automatic LLM tracing through a proxy so teams can't avoid instrumentation
- [[MultiPersonaProblem]] — Evals require collaboration across engineers, SMEs, and product people

## Related

- [[AgentObservability]] — the observability pillar of agent quality platforms
- [[Braintrust]] — the company behind this talk
- [[PhilHetzel]] — the presenter
