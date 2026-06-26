---
title: "Capability-Based Security"
type: concept
tags: [security, sandbox, agents, code-mode, architecture]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare.md"]
last_updated: 2026-06-26
---

## Definition
Capability-Based Security is a security model for agent code execution where the sandbox starts with zero capabilities and each capability (API access, network access, file system access) must be explicitly granted. This is the inverse of traditional container security, which starts with full capabilities and restricts from the outside.

## Key Information
- Start with nothing: no fetches, no exposed APIs, no network connections
- Grant capabilities explicitly and individually
- Unlike containers, which come with all features and are secured from the outside
- Language-agnostic: can be implemented in JavaScript (V8 isolates), Python, WASM, or any runtime
- Cloudflare's implementation uses V8 isolates with Dynamic Workers
- Default recommendation: no outgoing fetches, only explicitly exposed APIs
- Requires full observability into every execution for audit and debugging
- Key attributes: events, sandboxing, capability-based security, embeddable for fast ephemeral startup
- Enables safe execution of agent-generated code in production environments

## Related
- [[summary-20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare]] — source
- [[CodeMode]] — paradigm enabled by this security model
- [[AgentHarness]] — the harness architecture using this security model
- [[V8Isolates]] — Cloudflare's implementation
- [[CloudflareWorkers]] — platform using this model
- [[SunilPai]] — advocate for this approach
