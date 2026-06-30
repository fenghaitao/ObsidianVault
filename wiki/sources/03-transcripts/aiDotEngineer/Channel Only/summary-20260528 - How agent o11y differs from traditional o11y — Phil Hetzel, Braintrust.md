---
title: "How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust.md"
author: "Phil Hetzel"
company: "Braintrust"
date: 2026-05-28
tags: [agent-observability, traditional-observability, agent-traces, non-deterministic, text-indexing, database-design, cross-functional-teams, topic-modeling]
---

# How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust

## Core Thesis

Agent observability differs fundamentally from traditional observability across three dimensions: data characteristics (non-deterministic agent paths generate semi-structured, voluminous traces up to gigabytes), systems requirements (text-based indexing and custom databases for hybrid read patterns that traditional OLAP solutions cannot handle), and personas (non-technical domain experts actively participate in reviewing traces, a workflow absent from traditional uptime-focused observability). Traditional observability measures whether an application is up and performing from a technical lens; agent observability must also measure whether the agent is performing correctly from a functional and qualitative lens.

## Key Points

### What Traditional Observability Covers

- Scope: uptime and technical performance (latency, duration, 400/500 errors)
- Building blocks: metrics (aggregatable measurements like error count, latency), traces (full interaction workflows), spans (individual steps within a trace)
- Tools: Grafana, Datadog — well-established, operate at scale
- Persona: systems engineers, product engineers — strictly technical people
- Braintrust itself is a happy Datadog user for traditional website uptime monitoring

### Problem 1: Agents Are Non-Deterministic

- Traditional applications have deterministic code paths with known control flow
- LLM-based agents have high variety, abstracted reasoning, and unpredictable paths
- Agent observability must measure not just whether the agent responded but how well: groundedness (was the answer grounded in retrieved context?), tool usage (were expected tools used?), brand alignment (does the response match the system prompt standards?)
- These qualitative metrics cannot be tested by traditional observability tools because the trace data needed to compute them is far larger in volume

### Problem 2: Agent Traces Are Radically Different

- **Semi-structured**: Mix of structured spans and massive unstructured text
- **Voluminous**: Individual agent traces can exceed a gigabyte; individual spans can be 20MB
- **High velocity**: Production traffic generates traces at the same speed as traditional observability data, requiring true real-time ingestion
- **Dual read patterns**: Must support fast point reads (viewing a specific trace instantly) AND analytical queries (SQL, filtering, aggregation) simultaneously
- Braintrust built a custom database from the ground up specifically for agent traces, moving away from ClickHouse

### Problem 3: Custom Database Requirements

- **Write-ahead log (WAL)**: Immediate data ingestion so users can see traces as soon as they occur
- **Indexing layer**: Fast filtering and analytical queries on trace data
- **Text-based indexing (Tantivy)**: Full-text search across traces — users want to query "every trace containing the word Amazon." Tantivy is a Rust-based text indexing framework similar to Apache Lucene, forked by Braintrust
- **SQL unification**: All components unified through a SQL or SQL-like query language
- This is a completely new systems problem not addressed by traditional OLAP databases

### Problem 4: Different Personas

- Traditional observability: strictly technical (systems engineers, product engineers)
- Agent observability done well: both technical and non-technical people — clinicians, registered nurses, wealth advisors, lawyers — actively reviewing traces and contributing improvements
- Non-technical domain experts add value because they are closest to users or the problem space, and they can now write prompts in natural language
- Human annotation is a key part of the process: domain experts grade agent performance and justify their grades, enabling the extraction of failure modes that can be automated into scoring functions

### Observability and Evals Are the Same Problem

- The only difference between observability and evals is that evals run in batch with known inputs ahead of time
- Observability runs in real time with unknown inputs
- Both are solved with the same underlying systems

### Where the Space Is Going: Topic Modeling

- Braintrust recently rolled out automated topic modeling on agent traces
- A lightweight LLM runs on incoming traces to perform embedding and clustering
- Surfaces insights: user intent, sentiment, and common issues
- Goal: shorten the iteration loop between detecting a problem in production and running an experiment to fix it

### Q&A Highlights

- **Functional vs. technical observability**: Braintrust focuses on functional observability (agent quality as defined by the builder), but technical observability (duration, time to first token, cache hits) comes automatically from tracing
- **Human annotation workflow**: Domain experts grade traces and justify their grades → justifications are used to derive failure modes → failure modes are automated into scalable scoring functions via LLM-as-judge
- **Database decision**: Braintrust moved from ClickHouse to a custom database because they needed text-based indexing capabilities that ClickHouse could not provide at the time
- **Evals vs. observability integration**: Traces captured in production can be added to offline datasets for experimentation — closing the loop between observability and evals

## Entities

- [[PhilHetzel]] — Solutions engineering lead at Braintrust, presenter
- [[Braintrust]] — Agent quality platform (evals + observability), built custom trace database
- [[Datadog]] — Traditional observability tool Braintrust uses for website monitoring
- [[Grafana]] — Traditional open-source observability tool, mentioned as established alternative
- [[Tantivy]] — Rust-based full-text indexing framework, forked by Braintrust for trace text search
- [[ClickHouse]] — OLAP database Braintrust previously used before building their own
- [[SingleStore]] — Database company where Braintrust's founder was an early employee

## Concepts

- [[AgentObservability]] — The core topic: how it differs from traditional observability
- [[TraditionalObservability]] — Uptime and technical performance monitoring (metrics, traces, spans)
- [[NonDeterministicAgents]] — Why non-deterministic agent behavior requires broader measurement
- [[AgentTraceData]] — Semi-structured, voluminous (gigabyte-scale) traces with unstructured text
- [[TracesAndSpans]] — Shared building blocks between traditional and agent observability
- [[AgentQualityPlatform]] — Braintrust's category: evals + observability as a unified system
- [[TextBasedIndexing]] — Full-text search indexing across agent traces (Tantivy, Apache Lucene)
- [[WriteAheadLogForTraces]] — WAL pattern for immediate trace visibility in agent observability
- [[TopicModelingForAgents]] — Automated clustering of agent traces to surface user intent and failure modes
- [[HumanAnnotation]] — Domain expert review of agent traces with justifications
- [[CrossFunctionalAgentTeams]] — Technical and non-technical personas collaborating on agent quality
- [[ObservabilityAndEvalsUnified]] — Observability and evals as the same systems problem

## Related

- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — companion talk on platform maturity stages
- [[summary-20260525 - Does GenAI ＂belong＂ to data scientists — Phil Hetzel, Braintrust]] — related talk on cross-functional teams
- [[summary-20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust]] — companion talk on eval maturity
- [[summary-20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop]] — complementary perspective on agent observability
