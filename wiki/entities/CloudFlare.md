---
title: "Cloudflare"
type: entity
tags: [company, cloud, sandbox, infrastructure, mcp, code-mode]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251220 - The Infinite Software Crisis – Jake Nations, Netflix.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - MCP = Mega Context Problem - Matt Carey.md"]
last_updated: 2026-06-29
---

## Definition
Cloudflare is a web infrastructure and security company. In the agent context, it provides sandbox environments suitable for hosting agents built with the Claude Agent SDK, pioneered the code mode pattern for agent-API interaction, and built WorkerD for running untrusted agent-generated code at scale.

## Key Information
- Referenced as an example of production system failure in the Infinite Software Crisis talk
- Has published blog posts on programmatic tool use / code mode for agents
- Provides a sandbox integration with the Claude Agent SDK: `sandbox.start` followed by running the agent script
- One of several sandbox providers (alongside Modal, DigitalOcean, AWS) for hosting agents in production
- Has ~2,600 API endpoints — the context explosion problem from this large API surface motivated code mode
- Initially split API into 16 product-based MCP servers, but this had incomplete coverage
- Cloudflare MCP server provides read-only access to the entire Cloudflare API via code mode
- WorkerD enables executing untrusted agent-generated code in V8 isolates with programmable guardrails
- **Garrett Galow**: Garrett Galow previously worked at Cloudflare before joining WorkOS

## Related
- [[summary-20251220 - The Infinite Software Crisis – Jake Nations, Netflix]] — source
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[summary-20260425 - MCP = Mega Context Problem - Matt Carey]] — source
- [[summary-20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS]] — source
- [[GarrettGalow]] — former Cloudflare employee
- [[Sandboxing]] — the security approach
- [[ClaudeAgentSDK]] — the framework
- [[CodeMode]] — paradigm pioneered at Cloudflare
- [[WorkerD]] — dynamic worker sandbox
- [[MattCarey]] — engineer working on MCP and agents
