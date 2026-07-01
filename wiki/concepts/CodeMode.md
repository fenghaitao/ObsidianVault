---
title: "Code Mode"
type: concept
tags: [mcp, llm, tool-calling, optimization, code-generation, sandbox]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - The Future of MCP — David Soria Parra, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - MCP = Mega Context Problem - Matt Carey.md"]
last_updated: 2026-06-29
---

## Definition
Code Mode is a paradigm where LLMs generate executable code (typically JavaScript or TypeScript) instead of doing JSON-based tool calling back-and-forth. This enables single-shot execution with looping, state, sequencing, and parallelization. It sidesteps iteration and context problems but introduces sandboxing and code execution concerns.

## Key Information

### Origins and Motivation
- First blogged about by Cloudflare, then followed up by Anthropic
- Tool calling breaks at scale: hundreds of tools fill up context, composition is weird, back-and-forth is slow
- Models are trained on gigabytes of code — they already know how to write it
- Code provides typed APIs, type checking, syntax errors, and the ability to execute everything in one run
- Matt Carey: code has "so many more degrees of freedom than an individual tool call" — one tool called "code" replaces many individual tools

### Cloudflare's Implementation (Sunil Pai / Matt Carey)
- Matt Carey reduced the Cloudflare API surface (~2,600 endpoints, ~1.2M tokens) to two tool calls: search and execute, both accepting code strings — a 99.9% token reduction
- Example: a DDoS response that would take ~8 round trips with regular MCP is done in one shot
- Uses V8 isolates (WorkerD) for sandboxing: fast startup, ~10 years of security hardening
- Capability-based security: start with zero capabilities, grant explicitly
- Programmable guardrails: toggle internet access on/off, restrict to specific domains
- Default recommendation: no outgoing fetches, only explicitly exposed APIs
- Full observability into every code execution

### Sandbox Primitives for Code Mode
- **WorkerD** (Cloudflare): V8 isolates with programmable guardrails, runs at Cloudflare scale
- **Deno**: JavaScript/TypeScript runtime with sandboxed `deno run` and permission flags
- **Pydantic Monty**: Python code interpreter for untrusted Python code

### Broader Implications
- Enables a new software architecture where agents inhabit state machines rather than generating separate programs
- Breaks the programmer/non-programmer dichotomy: everyone gets access to a "buddy that can spit out code"
- Enables long-running workflows (days, months, years) with persistent state
- Enables generative UI: perfectly custom interfaces per user
- Enables saved mini-scripts: users save LLM-generated code for cron jobs and recurring tasks
- Requires thinking about developer experience for agents: docs as markdown, errors that guide agents, discoverability via search
- Historical analogy: 1950s computing where users submitted punch cards to an operator — untrusted code execution by design

### FastMCP Support (Jeremiah Lowin)
- A colleague at Prefect wrote a FastMCP extension supporting code mode the day it was announced
- Initially not included in FastMCP main because the framework tries to be opinionated
- Due to its success, planned for inclusion under an "experiments" or "optimize" CLI flag
- Lowin doesn't recommend it wholeheartedly due to sandboxing and code execution concerns

## Related
- [[summary-20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare]] — primary source
- [[summary-20260425 - MCP = Mega Context Problem - Matt Carey]] — source (WorkerD, sandbox primitives, historical analogy)
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — source
- [[FastMCP]] — framework adding code mode support
- [[MCP]] — protocol this technique works with
- [[Anthropic]] — company that followed up on the technique
- [[Cloudflare]] — company that pioneered the approach
- [[SunilPai]] — speaker who presented code mode
- [[MattCarey]] — creator of Cloudflare's search+execute approach
- [[WorkerD]] — Cloudflare's dynamic worker sandbox
- [[Deno]] — JavaScript/TypeScript sandbox alternative
- [[Pydantic Monty]] — Python sandbox alternative
- [[V8Isolates]] — sandbox execution environment
- [[CapabilityBasedSecurity]] — security model for code mode
- [[Untrusted Code Execution]] — the core safety challenge
- [[AgentHarness]] — the safe execution environment architecture
- [[InhabitingTheStateMachine]] — emergent behavior enabled by code mode
- [[GenerativeUI]] — application of code mode to UI generation
- [[Saved MiniScripts]] — user-facing pattern enabled by code mode
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — source (programmatic tool calling as code mode)
- [[ProgrammaticToolCalling]] — same concept under a different name, advocated by Anthropic
- [[DavidSoriaParra]] — advocated for this pattern in MCP context
