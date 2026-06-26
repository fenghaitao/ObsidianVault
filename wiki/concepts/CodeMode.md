---
title: "Code Mode"
type: concept
tags: [mcp, llm, tool-calling, optimization, code-generation, sandbox]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - The Future of MCP — David Soria Parra, Anthropic.md"]
last_updated: 2026-06-26
---

## Definition
Code Mode is a paradigm where LLMs generate executable code (typically JavaScript) instead of doing JSON-based tool calling back-and-forth. This enables single-shot execution with looping, state, sequencing, and parallelization. It sidesteps iteration and context problems but introduces sandboxing and code execution concerns.

## Key Information

### Origins and Motivation
- First blogged about by Cloudflare, then followed up by Anthropic
- Tool calling breaks at scale: hundreds of tools fill up context, composition is weird, back-and-forth is slow
- Models are trained on gigabytes of code — they already know how to write it
- Code provides typed APIs, type checking, syntax errors, and the ability to execute everything in one run

### Cloudflare's Implementation (Sunil Pai)
- Matt Carey reduced the Cloudflare API surface (~2,600 endpoints, ~1.2M tokens) to two tool calls: search and execute, both accepting code strings — a 99.9% token reduction
- Example: a DDoS response that would take ~8 round trips with regular MCP is done in one shot
- Uses V8 isolates for sandboxing: fast startup, ~10 years of security hardening
- Capability-based security: start with zero capabilities, grant explicitly
- Default recommendation: no outgoing fetches, only explicitly exposed APIs
- Full observability into every code execution

### Broader Implications
- Enables a new software architecture where agents inhabit state machines rather than generating separate programs
- Breaks the programmer/non-programmer dichotomy: everyone gets access to a "buddy that can spit out code"
- Enables long-running workflows (days, months, years) with persistent state
- Enables generative UI: perfectly custom interfaces per user
- Requires thinking about developer experience for agents: docs as markdown, errors that guide agents, discoverability via search

### FastMCP Support (Jeremiah Lowin)
- A colleague at Prefect wrote a FastMCP extension supporting code mode the day it was announced
- Initially not included in FastMCP main because the framework tries to be opinionated
- Due to its success, planned for inclusion under an "experiments" or "optimize" CLI flag
- Lowin doesn't recommend it wholeheartedly due to sandboxing and code execution concerns

## Related
- [[summary-20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare]] — primary source
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — source
- [[FastMCP]] — framework adding code mode support
- [[MCP]] — protocol this technique works with
- [[Anthropic]] — company that followed up on the technique
- [[Cloudflare]] — company that pioneered the approach
- [[SunilPai]] — speaker who presented code mode
- [[MattCarey]] — creator of Cloudflare's search+execute approach
- [[V8Isolates]] — sandbox execution environment
- [[CapabilityBasedSecurity]] — security model for code mode
- [[AgentHarness]] — the safe execution environment architecture
- [[InhabitingTheStateMachine]] — emergent behavior enabled by code mode
- [[GenerativeUI]] — application of code mode to UI generation
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — source (programmatic tool calling as code mode)
- [[ProgrammaticToolCalling]] — same concept under a different name, advocated by Anthropic
- [[DavidSoriaParra]] — advocated for this pattern in MCP context
