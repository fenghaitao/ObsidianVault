---
title: "Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare.md"
author: "Sunil Pai"
date: 2026-04-19
ingested: 2026-06-26
---

## Core Thesis

Sunil Pai presents "code mode" — a paradigm where LLMs generate executable code (JavaScript) instead of doing JSON-based tool calling back-and-forth. This enables single-shot execution with looping, state, sequencing, and parallelization, and points toward a new software architecture where agents inhabit state machines rather than generating separate programs.

## Key Points

- **Code mode vs. tool calling**: Tool calling breaks at scale with hundreds of tools filling context. Code mode generates code that executes in one run, leveraging typed APIs, syntax checking, and the model's training on vast code datasets.
- **Cloudflare API optimization**: Matt Carey reduced the Cloudflare API surface (2,600 endpoints, ~1.2M tokens) to just two tool calls — search and execute — both accepting code strings. This achieved a 99.9% token reduction to ~1,000 tokens.
- **DDoS response demo**: A prompt like "We are getting DDoS'd, block every offending IP" would take ~8 round trips with regular MCP. Code mode does it in one shot by generating and running JavaScript next to the API surface.
- **Live demo**: Demonstrated listing Cloudflare Workers via code mode — the model searched for API endpoints, then generated and executed code to paginate through results.
- **Programmer vs. non-programmer dichotomy**: Programmers open an IDE and write scripts to interact with systems. Non-programmers are limited to pre-built apps. LLMs break this boundary by giving everyone access to a "buddy that can spit out code."
- **Kenton's tic-tac-toe**: Kenton (creator of Cloudflare Workers) built a canvas and drew a tic-tac-toe board. When asked to play, the model started generating a tic-tac-toe app. Kenton stopped it and said: "You have access to the entire state of the system — an array of strokes. Inspect that and play." The model recognized the board from strokes, drew a circle in the center, and played. There was no tic-tac-toe code anywhere — the model inhabited the state machine.
- **Inhabiting the state machine**: The model stopped generating a program and instead inhabited the state machine — a fundamentally different interaction pattern where the agent reads and writes system state directly rather than building a separate app.
- **The harness architecture**: A safe execution environment (sandbox) where agents generate and run code. Starts with zero capabilities — no fetches, no exposed APIs. Capabilities are granted explicitly. Requires full observability into every execution.
- **V8 isolates**: Cloudflare uses V8 isolates for sandboxing — extremely fast startup and ~10 years of security hardening. Dynamic Workers provide the execution environment.
- **Long-running workflows**: Beyond one-off code execution, agents could run workflows lasting days, months, or years, carrying state through their lifetime.
- **Generative UI**: In a world of generative UI, every user gets a perfectly custom interface. E-commerce example: one user needs to return shoes and find similar items under $100; another has a delayed order. Different programs generated per user, backed by the same backend.
- **Developer experience for agents**: Your next billion users are robots generating code. Design for them: docs as markdown, errors that tell agents what to do next, discoverability via search.
- **Capability-based security**: Start with nothing, grant capabilities explicitly. Language-agnostic (JavaScript, Python, WASM). Attributes: events, sandboxing, capability-based security, embeddable for fast ephemeral startup.
- **Closing**: "For the longest time, programmers got code and infinite power. Everyone else got buttons and forms. That distinction is breaking. Let the code do the talking."

## Entities Mentioned

- [[SunilPai]] — Speaker, builds AI agents at Cloudflare for the Agents SDK, creator of PartyKit
- [[MattCarey]] — Cloudflare colleague who created the search+execute code mode approach for the Cloudflare API
- [[Kenton]] — Creator of Cloudflare Workers, built the tic-tac-toe canvas demo demonstrating inhabiting the state machine
- [[Cloudflare]] — Web infrastructure and security company; provider of Workers, V8 isolates, and the Agents SDK
- [[CloudflareWorkers]] — Serverless platform; Kenton is the creator
- [[PartyKit]] — Open-source tool for real-time multiplayer apps, created by Sunil Pai
- [[React]] — UI library; Pai identifies as a React programmer and discusses implications for UI developers
- [[TLDraw]] — Canvas/drawing library used in Kenton's tic-tac-toe demo
- [[Excalidraw]] — Drawing tool referenced alongside TLDraw
- [[V8Isolates]] — JavaScript execution environment used by Cloudflare for sandboxing; fast startup, 10 years of security hardening
- [[Anthropic]] — AI company; Opus model was used in the tic-tac-toe demo and exhibited alignment behavior (letting Kenton win)
- [[ClaudeCode]] — Anthropic's coding agent; referenced as an example of general-purpose computing via code generation
- [[MCP]] — Model Context Protocol; the baseline that code mode improves upon for wide API surfaces

## Concepts Introduced

- [[CodeMode]] — LLMs generate executable code instead of JSON tool calls; single-shot execution with looping, state, parallelization
- [[InhabitingTheStateMachine]] — Agent reads and writes system state directly rather than generating a separate application
- [[AgentHarness]] — Safe execution environment where agents generate and run code with explicitly granted capabilities
- [[CapabilityBasedSecurity]] — Security model starting with zero capabilities, granting them explicitly; language-agnostic
- [[GenerativeUI]] — Custom user interfaces generated per user based on their context and needs
- [[DeveloperExperienceForAgents]] — Designing APIs, docs, and errors for consumption by AI agents rather than humans

## Related

- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — also discusses code mode
- [[summary-20260427 - Gateways are All You Need — Karan Sampath, Anthropic]] — related agent architecture
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — related Claude tooling and sandboxing
- [[summary-20260428 - Building your own software factory — Eric Zakariasson, Cursor]] — related agent coding paradigm
