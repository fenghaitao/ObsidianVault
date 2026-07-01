---
title: "AI Gateway"
type: concept
tags: [ai, llm, gateway, proxy, observability, security, networking]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - What if the network was the sandbox — Remy Guercio, Tailscale.md"]
last_updated: 2026-06-30
---

## Definition
An AI Gateway (or LLM Gateway) is a centralized proxy that sits between AI agents and LLM providers, holding a single API key per provider and using identity information from connecting agents to enforce permissions, budgets, quotas, and observability. Unlike traditional API gateways, an AI Gateway can leverage network-level identity so agents connect with zero keys of their own.

## Key Information
- **Single key per provider**: The gateway holds one API key per provider (Anthropic, OpenAI, Gemini, Vertex AI, Bedrock, etc.), not per agent or user
- **Identity-based access**: Agents connect with network-level identity (tags, groups, users) rather than API keys; the gateway uses this identity to determine permissions
- **Cross-provider budgets**: A single budget (e.g., $5/day per user) works across all providers — not per-provider budgets
- **Per-identity observability**: See all tokens, models, costs, and requests per user, per tag, per group — everything that goes through the gateway
- **Tool call visibility**: All tool calls (bash commands, MCP calls, etc.) are visible because they must pass through the gateway at the network layer — guaranteed, cannot be bypassed
- **Webhook integration**: Fire webhooks on each tool call with full request/response information for external processing
- **Permission granularity**: Can control model access, provider access, quotas, and budgets per identity; finer-grained tool-level restrictions (e.g., blocking dangerous bash commands) are being developed
- **Network-layer enforcement**: Because the gateway operates at the network layer, revocation is immediate and absolute — the agent has no keys to use as workarounds
- **Reference implementation**: [[Aperture (Tailscale)]] is Tailscale's AI Gateway, built on [[TS Net]] and Tailscale identity primitives
- **Works with major coding agents**: Claude Code, Codex, Gemini CLI can all connect by setting a dummy API key and pointing the base URL to the gateway

## Related
- [[Aperture (Tailscale)]] — reference implementation by Tailscale
- [[Network as Sandbox]] — architectural pattern the gateway enables
- [[NetworkLevel Identity]] — identity mechanism used by the gateway
- [[Keyless Agent Sandbox]] — agent-side benefit
- [[AI Observability]] — related observability concept
- [[summary-20260427 - Gateways are All You Need — Karan Sampath, Anthropic]] — related talk on gateways
- [[summary-20260601 - What if the network was the sandbox — Remy Guercio, Tailscale]] — source
