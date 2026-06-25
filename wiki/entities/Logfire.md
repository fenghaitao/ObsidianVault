---
title: "Logfire"
type: entity
tags: [observability, pydantic, opentelemetry, tracing, monitoring]
sources: [raw/03-transcripts/Pydantic/Channel Only/20250415 - Pydantic, Jason Liu & MCP Meetup - April 8, 2025.md, raw/03-transcripts/Pydantic/Channel Only/20250806 - Pydantic @ Google London July Meetup - All Talks.md, raw/03-transcripts/Pydantic/Channel Only/20260326 - We refactored the Logfire Explorer view： here's what changed.md]
last_updated: 2026-06-25
---

## Definition

Logfire is Pydantic's observability platform built on OpenTelemetry. It provides general-purpose observability (logs, traces, metrics) with specialized AI-specific capabilities. Available as cloud, self-hosted, and via GCP Marketplace.

## Key Information

### Architecture

- Built on OpenTelemetry standards — emits standard OTel spans, metrics, and logs
- General-purpose: can monitor any application, not just AI workloads
- AI-specific features: token counting, cost tracking, LLM call tracing, MCP distributed tracing
- SQL-based querying for power users and AI agents
- Jupyter-like Explorer view with AI assistant for query writing (added March 2026)

### Key Features

- **One-line instrumentation**: `logfire.instrument_pydantic_ai()`, `logfire.instrument_openai()`, etc.
- **Distributed tracing**: traces span across MCP client/server boundaries, showing full call chains
- **Real-time trace viewing**: modified OpenTelemetry to stream trace data before completion (OTel normally only sends after trace finishes)
- **Cost tracking**: per-request LLM costs visible in traces
- **MCP server**: Logfire can act as an MCP server, allowing coding agents to query observability data via SQL
- **Enterprise**: available on GCP Marketplace, supports self-hosting, OIDC auth

### Integration Points

- Auto-instruments PydanticAI, OpenAI, FastAPI, PostgreSQL, and more
- Pydantic AI Gateway can send all request traces to Logfire
- DBOS integration for durable agent observability
- Render deployment with one-click Logfire configuration

## Related

- [[Pydantic]] — parent company
- [[PydanticAI]] — agent framework with native Logfire integration
- [[OpenTelemetry]] — underlying standard
- [[SamuelColvin]] — creator
- [[summary-20260326 - We refactored the Logfire Explorer view： here's what changed]] — source
