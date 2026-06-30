---
title: "Matt Carey"
type: entity
tags: [person, cloudflare, code-mode, api, mcp]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - MCP = Mega Context Problem - Matt Carey.md"]
last_updated: 2026-06-29
---

## Definition
Matt Carey is an engineer at Cloudflare who works on MCP and agents. He created the search+execute code mode approach for the Cloudflare API surface, reducing ~1.2M tokens of tool definitions to ~1,000 tokens by exposing just two tool calls that accept code strings.

## Key Information
- Works at Cloudflare alongside Sunil Pai
- Created a clever approach to the Cloudflare API surface (~2,600 endpoints) by exposing only two tool calls: search and execute
- Search accepts code as input, with the full OpenAPI JSON spec as the function input
- Execute provides functions to call against discovered API endpoints
- Achieved a 99.9% token reduction: from ~1.2M tokens to ~1,000 tokens
- Presented his own talk "MCP = Mega Context Problem" at AIE Code, covering three approaches to progressive discovery: CLI, tool search, and code mode
- Demonstrated WorkerD — Cloudflare's dynamic worker sandbox for running untrusted agent-generated code with programmable guardrails
- Showed a live MCP client with read-only access to the entire Cloudflare API (all 2,600+ endpoints)
- Advocated for MCP becoming a native flag in web frameworks (`MCP=true`)
- Referenced NPMI agents at the end of his talk

## Related
- [[summary-20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare]] — source
- [[summary-20260425 - MCP = Mega Context Problem - Matt Carey]] — source (his own talk)
- [[Cloudflare]] — employer
- [[SunilPai]] — colleague
- [[CodeMode]] — concept he pioneered at Cloudflare
- [[WorkerD]] — dynamic worker sandbox he demonstrated
- [[ProgressiveDiscovery]] — pattern he advocated for
- [[MCP as Middleware]] — vision he presented
- [[NPMI agents]] — package he referenced
