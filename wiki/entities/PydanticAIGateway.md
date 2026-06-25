---
title: "PydanticAIGateway"
type: entity
tags: [api, gateway, llm, inference, pydantic]
sources: [raw/03-transcripts/Pydantic/Channel Only/20260112 - One API Key for Every LLM Provider - Pydantic AI Gateway.md]
last_updated: 2026-06-25
---

## Definition

Pydantic AI Gateway is a unified LLM inference layer that lets developers use a single API key across OpenAI, Anthropic, Google, Amazon Bedrock, and Grok. Runs on Cloudflare's edge network. Core is open source (AGPLv3); admin UI is commercial.

## Key Information

### Features

- **Unified API key**: one key works across all supported providers
- **Two modes**: buy inference through Pydantic, or bring your own API keys (free during beta)
- **Edge deployment**: runs on Cloudflare Workers (~200-300 data centers) for 1-20ms latency overhead
- **No request translation**: passes requests through unchanged, so new model features work immediately
- **Model fallback**: automatic routing to alternatives if a provider goes down (e.g., Anthropic -> Google -> Bedrock)
- **Budgeting**: limits at project, user, and key level; daily/weekly/monthly/total caps
- **Observability**: drop in a Logfire write token to trace all requests
- **Caching**: planned for eval workloads

### Deployment Options

- Cloud (managed by Pydantic)
- Self-hosted on Cloudflare Workers
- Docker container / Helm chart for own infrastructure

### PydanticAI Integration

Simply prefix model names with `gateway/` — no other code changes needed.

## Related

- [[Pydantic]] — parent company
- [[PydanticAI]] — agent framework
- [[Logfire]] — integrated observability
- [[SamuelColvin]] — creator
- [[summary-20260112 - One API Key for Every LLM Provider - Pydantic AI Gateway]] — source
