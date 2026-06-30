---
title: "Postgres"
type: entity
tags: [tool, database, relational]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle.md"]
last_updated: 2026-06-29
---

## Definition
PostgreSQL (Postgres) is an open-source relational database. In the context of eval platforms, Phil Hetzel noted that cramming a 1GB agent trace into a Postgres row leads to significant performance problems, illustrating why eval platforms need specialized data architectures beyond traditional relational databases.

## Key Information
- Open-source relational database
- Referenced as an example of the data challenges in eval platforms: large, semi-structured traces don't fit well in relational rows
- Traditional relational databases struggle with the velocity, size, and unstructured nature of LLM agent traces
- Neon (serverless Postgres) is mentioned as a step up from spreadsheets, but even Postgres has limits for trace data at scale
- **n8n Agent Memory**: In n8n, Postgres can be used as an external memory backend for AI agents, storing conversation messages in a table that other applications can query. This enables integrating agent memory with existing systems (e.g., displaying chat history in a custom dashboard)

## Related
- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — source
- [[Neon]] — serverless Postgres provider
- [[TraceDataChallenges]] — the data problems Postgres struggles with
- [[EvalPlatforms]] — the platform context
- [[n8n]] — platform using Postgres for agent memory
- [[summary-20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle]] — source
