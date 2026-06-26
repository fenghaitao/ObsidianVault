---
title: "Agent Harness"
type: concept
tags: [architecture, agents, sandbox, code-mode, execution]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare.md"]
last_updated: 2026-06-26
---

## Definition
An Agent Harness is a safe execution environment (sandbox) where AI agents generate and run code with explicitly granted capabilities. It provides the runtime infrastructure for code mode, enabling agents to execute code against APIs and system state in a controlled, observable manner.

## Key Information
- Everyone building coding agents over the last 3-6 months has realized they need a harness
- The harness is not just a code generator — it provides a safe space to execute code with explicitly exposed capabilities
- Architecture attributes:
  - **Starts with zero capabilities**: no fetches, no APIs, no network — only code execution
  - **Explicit capability grants**: each API, network connection, or system access must be granted
  - **Fast startup**: must be embeddable and ephemeral for quick execution
  - **Full observability**: need to know exactly what code ran and why (e.g., "why did it make a $2.3M trade last Tuesday?")
  - **Controlled network**: default is no outgoing fetches, only explicitly exposed APIs
- Implementation options: V8 isolates (Cloudflare), WebAssembly, custom JavaScript interpreters
- Enables long-running workflows (days, months, years) with persistent state
- Enables generative UI: custom interfaces generated per user
- Can run closer to the user (on-device) to stitch together different services on a task-by-task basis
- Distinct from container-based sandboxes (which start with full capabilities and restrict from outside)

## Related
- [[summary-20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare]] — source
- [[CodeMode]] — paradigm enabled by the harness
- [[CapabilityBasedSecurity]] — security model for the harness
- [[V8Isolates]] — Cloudflare's harness implementation
- [[CloudflareWorkers]] — platform providing the harness
- [[InhabitingTheStateMachine]] — emergent behavior enabled by the harness
- [[GenerativeUI]] — application enabled by the harness
- [[SunilPai]] — speaker who described the harness architecture
