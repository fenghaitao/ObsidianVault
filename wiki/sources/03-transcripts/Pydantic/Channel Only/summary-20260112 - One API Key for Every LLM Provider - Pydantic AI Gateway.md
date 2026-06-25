---
title: "summary-20260112 - One API Key for Every LLM Provider - Pydantic AI Gateway"
type: source
tags: [source, pydantic, gateway, api, inference]
sources: ["raw/03-transcripts/Pydantic/Channel Only/20260112 - One API Key for Every LLM Provider - Pydantic AI Gateway.md"]
last_updated: 2026-06-25
---

## Core Summary

Samuel Colvin and Laís de Pydantic introduce the Pydantic AI Gateway: a unified inference layer that lets developers use one API key across OpenAI, Anthropic, Google, Bedrock, and Grok. The gateway runs on Cloudflare's edge network for single-digit millisecond latency overhead, supports bring-your-own-key or buy-through-us models, and provides budgeting, observability via Logfire, and model fallback. Core is open source (AGPLv3); admin UI is commercial.

## Key Points

- Gateway supports two modes: buy inference through Pydantic or bring your own API keys (free during beta)
- Runs on Cloudflare Workers at the edge for minimal latency (~1-20ms overhead)
- Budgeting at project, user, and key level with daily/weekly/monthly/total limits
- Model fallback: if one provider goes down, automatically routes to alternatives (e.g., Anthropic -> Google -> Bedrock)
- No request translation: new model features (e.g., Anthropic structured outputs) work immediately
- Open source core (AGPLv3), commercial admin UI; available as cloud, Cloudflare self-host, or Docker/Helm
- Part of the Pydantic stack: Validation -> PydanticAI -> Logfire -> Gateway

## Related

- [[PydanticAIGateway]] — the gateway product
- [[PydanticAI]] — agent framework that integrates with the gateway via `gateway/` prefix
- [[Logfire]] — observability integrated with gateway for request tracing
- [[SamuelColvin]] — creator of Pydantic
