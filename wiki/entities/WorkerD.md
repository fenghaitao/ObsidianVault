---
title: "WorkerD"
type: entity
tags: [cloudflare, sandbox, code-execution, security, v8]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - MCP = Mega Context Problem - Matt Carey.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Why, and how you need to sandbox AI-Generated Code — Harshil Agrawal, Cloudflare.md"]
last_updated: 2026-06-30
---

## Definition
WorkerD is Cloudflare's dynamic worker sandbox for running untrusted agent-generated code. It uses V8 isolates to execute code from a string in a fully isolated environment with programmable guardrails, enabling safe execution of LLM-generated code at Cloudflare scale.

## Key Information
- Executes code from a string in a fully isolated dynamic worker on the backend
- No access to `process.env` or secrets by default
- Programmable guardrails: toggle internet access on/off, restrict to specific domains
- Capability-based security: start with zero capabilities, grant explicitly
- Runs at Cloudflare scale — supports billions of requests
- Demonstrated in Matt Carey's talk: listing workers, deploying workers, adding access policies, inspecting DNS
- Part of Cloudflare's code mode approach: agents generate code that runs in WorkerD against the Cloudflare API
- Alternative to Deno and Pydantic Monty for running untrusted code
- Harshil Agrawal used WorkerD isolates in an OpenClaw alternative: `loader.load()` creates a new isolate, `globalOutbound null` blocks all network, bindings define the entire surface area the AI code can touch
- Network control spectrum: null (fully blocked), proxied through your service, or fully open (not recommended)

## Related
- [[summary-20260425 - MCP = Mega Context Problem - Matt Carey]] — source
- [[summary-20260408 - Why, and how you need to sandbox AI-Generated Code — Harshil Agrawal, Cloudflare]] — source
- [[Cloudflare]] — parent company
- [[CloudflareWorkers]] — platform
- [[V8Isolates]] — execution environment
- [[CodeMode]] — paradigm enabled by WorkerD
- [[CapabilityBasedSecurity]] — security model
- [[Untrusted Code Execution]] — concept
- [[Harshil Agrawal]] — used WorkerD for OpenClaw alternative
