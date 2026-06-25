---
title: "Pydantic"
type: entity
tags: [company, python, validation, ai, open-source]
sources: [raw/03-transcripts/Pydantic/Channel Only/20250415 - Pydantic, Jason Liu & MCP Meetup - April 8, 2025.md, raw/03-transcripts/Pydantic/Channel Only/20260112 - One API Key for Every LLM Provider - Pydantic AI Gateway.md, raw/03-transcripts/Pydantic/Channel Only/20260401 - Samuel Colvin Controlling the wild： Monty, from tool calling to computer use - PyAI Conf 2026.md]
last_updated: 2026-06-25
---

## Definition

Pydantic is both a Python data validation library (downloaded ~300M times/month) and the company founded by Samuel Colvin that builds the Pydantic stack: Pydantic (validation), PydanticAI (agent framework), Logfire (observability), Pydantic AI Gateway (unified LLM inference), and Monty (secure Python interpreter for AI agents).

## Key Information

### The Pydantic Stack

Samuel Colvin describes the stack as covering the full AI development lifecycle:

1. **Pydantic Validation** — the original library; data validation via type annotations, powered by a Rust core. Used by OpenAI, Anthropic, Google, and virtually all major AI SDKs.
2. **PydanticAI** — agent framework launched late 2024. Type-safe, production-ready, with MCP support, structured outputs, and Pydantic Graph for finite state machine workflows.
3. **Logfire** — observability platform built on OpenTelemetry. General-purpose (logs, traces, metrics) with AI-specific capabilities. Supports distributed tracing across MCP client/server boundaries. Available on GCP Marketplace.
4. **Pydantic AI Gateway** — unified LLM inference layer. One API key for OpenAI, Anthropic, Google, Bedrock, Grok. Runs on Cloudflare edge. Core is open source (AGPLv3).
5. **Monty** — minimal secure Python interpreter in Rust for running AI-generated code. From-scratch implementation with no file system, network, or env var access by default.

### Company Philosophy

- Open source core, commercial services layered on top
- "Boring but necessary" — building infrastructure developers need rather than chasing hype
- Type safety and production readiness as differentiators
- Embracing open standards: OpenTelemetry, MCP

### Events

Pydantic organizes the PyAI Conference (first held 2026) and regular meetups in London, often co-hosted with Google, Atomico, and other partners.

## Related

- [[SamuelColvin]] — founder and CEO
- [[PydanticAI]] — agent framework
- [[Logfire]] — observability platform
- [[Monty]] — secure Python interpreter
- [[PydanticAIGateway]] — unified inference layer
- [[FastAPI]] — web framework built on Pydantic
- [[PyAIConf2026]] — Pydantic's conference
- [[summary-20250415 - Pydantic, Jason Liu & MCP Meetup - April 8, 2025]] — MCP meetup
- [[summary-20250806 - Pydantic @ Google London July Meetup - All Talks]] — Google London meetup
- [[summary-20260515 - Pydantic at PyCon US 2026 - meet the team!]] — PyCon US 2026
