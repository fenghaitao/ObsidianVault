---
title: "Aperture (Tailscale)"
type: entity
tags: [tool, ai-gateway, networking, llm, observability, security]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - What if the network was the sandbox — Remy Guercio, Tailscale.md"]
last_updated: 2026-06-30
---

## Definition
Aperture is Tailscale's AI gateway — a node deployed on a tailnet that acts as a centralized LLM proxy. It holds a single API key per provider (Anthropic, OpenAI, Gemini, Vertex AI, Bedrock, etc.) and uses network-level identity from connecting nodes to enforce permissions, budgets, quotas, and observability. Agents connect with zero API keys; their identity (tags, groups) on the tailnet determines what they can access.

## Key Information
- Built entirely on public [[Tailscale]] identity primitives available via [[TS Net]] — no private APIs used
- Available on Tailscale's free plan
- **Keyless agent connection**: Agents (e.g., in GitHub Actions runners) connect with no API key — just a tag on the tailnet. The dummy key `-` is used only to satisfy the tool's API key requirement
- **Identity-aware**: Sees the full identity (user, groups, tags) of every connecting node on every request
- **Cross-provider**: Works with Anthropic, OpenAI, Gemini, Vertex AI, Amazon Bedrock, and any provider supporting major context protocols
- **Usage metrics**: Per-identity views of tokens used, models used, cost per model, all requests
- **Request inspection**: Full request headers, request body, response body visible per request — including Claude Code's complete initial system prompt
- **Tool call observability**: All tool calls (bash commands, MCP calls, grep, etc.) are extracted and visible because they must pass through the gateway at the network layer
- **Cost controls**: Single budget works across all providers (not per-provider). Team-level budgets with individual sub-budgets. Can differentiate free internal GPU endpoints from paid external models
- **Webhooks**: Fires webhooks on each tool call with full information — guaranteed to run
- **Permissioning**: Currently model/provider-level with quota controls; working on finer-grained tool-level restrictions and guardrails (e.g., blocking `rm -rf /`)
- **Setup**: Point the coding agent's base URL to the Aperture node; works with Claude Code, Codex, Gemini CLI
- **Visual editor + GitOps**: Permissions configurable via visual grants editor or JSON in ACL policy file for GitOps workflows; also has an API

## Related
- [[Tailscale]] — parent platform
- [[TS Net]] — open source library Aperture is built on
- [[Remy Guercio]] — demonstrated Aperture
- [[AI Gateway]] — concept
- [[Network as Sandbox]] — core thesis behind the design
- [[Keyless Agent Sandbox]] — enabled by Aperture
- [[summary-20260601 - What if the network was the sandbox — Remy Guercio, Tailscale]] — source
