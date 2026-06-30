---
title: "Code Execution (Sandboxed)"
type: concept
tags: [gemini, tool, sandbox, python, data-science, crewai, code-mode]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240808 - Using agents to build an agent company： Joao Moura.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - MCP = Mega Context Problem - Matt Carey.md"]
last_updated: 2026-06-29
---

## Definition
Code Execution is a Gemini tool that provides a sandboxed Python environment with pre-installed data science libraries. It allows Gemini models to write and run Python code as a sub-tool to solve arbitrary data science tasks without affecting the user's local environment. More broadly, sandboxed code execution is an emerging infrastructure primitive for running untrusted agent-generated code.

## Key Information
- **Gemini Code Execution**: Available as a toggleable tool in AI Studio and via Gemini APIs
- Provides a sandboxed Python environment with data science libraries pre-installed
- Gemini can invoke code execution as a tool call to write and run Python code
- No risk of impacting the user's local environment since it runs in a sandbox
- Demonstrated use cases: drawing bounding boxes around objects in images, generating SVG representations, segmentation masks, counting entities in photos
- Works with even the smallest Gemini 3.1 Flash Light model at well under a fraction of a penny per operation
- Can be combined with compare mode in AI Studio to compare how different models use code execution
- Automatically invocable via the API
- **CrewAI Code Execution**: Single flag (`allow_code_execution`) that enables agents to write and execute their own code. Agents can dynamically build their own tools at runtime rather than relying solely on pre-configured tools. Uses automated coder and command-line code executor instances.

### Broader Sandbox Primitives (Matt Carey)
- **WorkerD** (Cloudflare): V8 isolates with programmable guardrails — toggle internet access, restrict domains. Runs at Cloudflare scale.
- **Deno**: JavaScript/TypeScript runtime with sandboxed `deno run` and permission flags
- **Pydantic Monty**: Python code interpreter for untrusted Python code
- Running untrusted code was historically a CVE-level vulnerability; now becoming a standard infrastructure primitive
- More infrastructure primitives expected to emerge as models get smarter

## Related
- [[summary-20240808 - Using agents to build an agent company： Joao Moura]] — source (CrewAI code execution)
- [[summary-20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind]] — source
- [[summary-20260425 - MCP = Mega Context Problem - Matt Carey]] — source (WorkerD, Deno, Pydantic Monty)
- [[AI Studio]] — platform where Gemini code execution is available
- [[CrewAI]] — framework with allow_code_execution flag
- [[Gemini 3.1 Flash Light]] — model supporting code execution
- [[Function Calling]] — related tool capability
- [[Sandboxing]] — related concept
- [[WorkerD]] — Cloudflare's sandbox
- [[Deno]] — JavaScript/TypeScript sandbox
- [[Pydantic Monty]] — Python sandbox
- [[Untrusted Code Execution]] — broader concept
- [[CodeMode]] — paradigm enabled by sandboxed code execution
- [[CapabilityBasedSecurity]] — security model
