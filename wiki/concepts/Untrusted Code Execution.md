---
title: "Untrusted Code Execution"
type: concept
tags: [security, sandbox, code-execution, agents, infrastructure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - MCP = Mega Context Problem - Matt Carey.md"]
last_updated: 2026-06-29
---

## Definition
Untrusted Code Execution is the practice of running agent-generated code in isolated sandboxes with programmable guardrails. It is an emerging infrastructure primitive that enables agents to write and execute code safely without risking the host system.

## Key Information
- Running LLM-generated code without human review is inherently dangerous: it could read file systems, exfiltrate secrets, run infinite loops, consume resources, or run crypto miners
- Historically considered a CVE-level vulnerability — "you would just immediately have to stop allowing that"
- LLMs are very good at writing code, making code execution a natural interface for agent-tool interaction
- Three emerging primitives for safe untrusted code execution:
  - **WorkerD** (Cloudflare): V8 isolates with programmable guardrails, toggle internet access, restrict domains
  - **Deno**: JavaScript/TypeScript runtime with sandboxed `deno run` and permission flags
  - **Pydantic Monty**: Python code interpreter for untrusted Python code
- Historical attempts: DSLs (JSON specs interpreted as code), VMs/sandboxes, code review — all limited
- Matt Carey predicts many more infrastructure primitives will emerge for this purpose
- Analogous to 1950s computing: users submitted punch cards to an operator who ran them — untrusted code execution by design
- Cloud era moved away from this model; AI era is returning to it

## Related
- [[summary-20260425 - MCP = Mega Context Problem - Matt Carey]] — source
- [[CodeMode]] — paradigm enabled by untrusted code execution
- [[ProgrammaticToolCalling]] — pattern using untrusted code execution
- [[Sandboxing]] — security approach
- [[CapabilityBasedSecurity]] — security model
- [[WorkerD]] — Cloudflare's implementation
- [[Deno]] — JavaScript/TypeScript sandbox
- [[Pydantic Monty]] — Python sandbox
- [[V8Isolates]] — execution environment
