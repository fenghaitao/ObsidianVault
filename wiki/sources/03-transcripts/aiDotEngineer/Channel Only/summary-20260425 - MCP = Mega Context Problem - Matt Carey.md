---
title: "MCP = Mega Context Problem - Matt Carey"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - MCP = Mega Context Problem - Matt Carey.md"
author: "Matt Carey"
date: 2026-04-25
ingested: 2026-06-29
---

## Core Thesis

Matt Carey presents three approaches to solving the context explosion problem when giving agents access to large API surfaces: CLI-based interaction, tool search, and code mode. He argues that running untrusted agent-generated code in programmable sandboxes is the most promising direction, and that infrastructure primitives for safe code execution will proliferate as models get smarter.

## Key Points

### The Context Problem
- Giving agents naive tools for every API endpoint explodes context windows: Cloudflare's OpenAPI spec is 2.3M tokens, ~1.1M tokens as tools
- Cloudflare's initial response was splitting into 16 product-based MCP servers, but this had incomplete coverage and required user selection
- Cloudflare has ~2,600 API endpoints — impossible to split into manageable MCP servers with full coverage
- The real need: progressive discovery of tools

### Three Approaches to Progressive Discovery

**1. CLI-based interaction**: Agents use shell access to call `--help`, parse commands, and interact with CLIs. Used by OpenClaw and widely popular. Works well but requires shell access, which is not always available (e.g., Cloud Code).

**2. Tool Search**: A search tool loads relevant tools into context on demand via keyword matching. Used by Cloud Code. Works well but unused tools remain in context (~2,100 tokens loaded, only ~500 used).

**3. Code Mode**: Let the model write TypeScript code against a typed SDK generated from the OpenAPI spec. Types are a concise way to represent inputs and outputs. The model generates code, which runs against the typed SDK. Benefits: the model gets better over time, the OpenAPI spec is the source of truth, code has more degrees of freedom than individual tool calls.

### The Untrusted Code Problem
- Running agent-generated code is scary: it could read file systems, exfiltrate secrets, run infinite loops, consume resources, run crypto miners
- Historical attempts: DSLs (JSON specs interpreted as code), VMs/sandboxes, code review — all limited
- Cloudflare's solution: **WorkerD** — dynamic workers using V8 isolates with programmable sandbox and guardrails
  - Execute code from a string in a fully isolated dynamic worker
  - No access to `process.env` or secrets
  - Programmable guardrails: toggle internet access on/off, restrict to specific domains
  - Capability-based: start with zero, grant explicitly
- Other emerging primitives: **Deno** run (with sandboxing), **Pydantic Monty** (Python code interpreter for untrusted Python)

### Live Demo
- Demonstrated an MCP client with read-only access to the entire Cloudflare API (all 2,600+ endpoints)
- Can list workers, deploy workers, add access policies, inspect DNS, send emails
- Full API surface accessible through code mode

### Future Directions

**Server-side**: APIs must be ready for agents — good rate limiting is essential because agents can hammer APIs from multiple sandboxes in parallel.

**Client-side**:
- **Programmatic tool calling**: running untrusted code in clients will become standard
- **Saved mini-scripts**: users save LLM-generated code for reuse — enables cron jobs, web scraping, self-healing scripts
- **More MCP clients**: building MCP clients has been hard (stateful connections, resumability), but will get easier
- **Stateless agent loops**: cloud-native approach where state can be turned on/off — essential when there are 100 agents per person

**MCP as middleware**: MCP will become a flag in frameworks (`MCP=true`), SDK getting super lightweight, natively in every TypeScript full-stack framework by end of year. Express thousands of APIs from one Next.js app with `MCP=true`.

### Historical Analogy
- 1950s: running untrusted code via punch cards given to the computer operator
- Cloud era: moved away from that model
- AI era: returning to it — users (AI) write code against your services, and your services must be ready

## Entities Mentioned

- [[MattCarey]] — Speaker, works on MCP and agents at Cloudflare
- [[Cloudflare]] — Employer, provider of Workers, V8 isolates, WorkerD, Cloudflare MCP
- [[CloudflareWorkers]] — Serverless platform; Dynamic Workers provide the sandbox for code mode
- [[WorkerD]] — Cloudflare's dynamic worker sandbox for running untrusted agent-generated code
- [[V8Isolates]] — JavaScript execution environment used by Cloudflare for sandboxing
- [[OpenClaw]] — Agent framework that uses CLI-based interaction
- [[Deno]] — JavaScript runtime with sandboxed code execution (`deno run`)
- [[Pydantic]] — Company behind Monty, a Python code interpreter for untrusted code
- [[NextJS]] — Framework where MCP will be natively integrated
- [[Cloud Code]] — Uses tool search for progressive discovery
- [[NPMI agents]] — Referenced at the end ("Try out NPMI agents")

## Concepts Introduced

- [[ProgressiveDiscovery]] — Loading tools on demand rather than all at once into context
- [[ToolSearch]] — Keyword-matching mechanism for loading relevant tools into context
- [[CodeMode]] — Letting the model write code against typed SDKs instead of individual tool calls
- [[ProgrammaticToolCalling]] — Running untrusted agent-generated code in sandboxes
- [[CLI for Agents]] — Agents using shell access to interact with CLIs via --help and command parsing
- [[Untrusted Code Execution]] — Running agent-generated code safely in isolated sandboxes with programmable guardrails
- [[Saved MiniScripts]] — Users saving LLM-generated code for reuse in cron jobs and recurring tasks
- [[Stateless Agent Loop]] — Cloud-native agent architecture where state can be toggled on/off
- [[MCP as Middleware]] — MCP becoming a native flag in web frameworks rather than a separate concern
- [[CapabilityBasedSecurity]] — Security model starting with zero capabilities, granting explicitly
- [[Sandboxing]] — Isolated execution environments for agent-generated code
- [[AgenticLoop]] — The core execution pattern for agents

## Related

- [[summary-20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare]] — companion talk covering code mode in depth
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — MCP roadmap and progressive discovery
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — MCP design principles
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — OpenClaw and CLI-based agent interaction
