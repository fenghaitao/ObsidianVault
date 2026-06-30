---
title: "Programmatic Tool Calling"
type: concept
tags: [mcp, tool-calling, code-mode, optimization, client]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - The Future of MCP — David Soria Parra, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - MCP = Mega Context Problem - Matt Carey.md"]
last_updated: 2026-06-29
---

## Definition
Programmatic Tool Calling (also called code mode) is a client-side pattern where the model writes code to compose multiple tool calls together in a single execution, rather than making sequential round-trips of tool-call-then-result. The model is given a REPL or execution environment (V8 isolate, Monty, Lua interpreter) and writes scripts that call tools and compose their results.

## Key Information
- Avoids the inefficiency of sequential tool orchestration: model calls tool, takes result, talks, calls another tool, takes result — each step uses inference and is latency-sensitive
- Instead, the model writes a script that composes everything together in one call
- Uses MCP's structured output feature to get type information about return values, enabling the model to compose calls with proper type handling
- Without structured output, you can use a cheap model to extract and type the return values
- Can be implemented on the client side (giving the model a REPL) or on the server side (Cloudflare MCP server provides an execution environment)
- Benefits: cuts token usage, cuts latency, enables more powerful composition
- David Soria Parra: "this is something we're just not doing enough yet, and this is I think something where we can improve our agent harnesses"
- Related to what Claude Code does when it writes bash commands — the same principle applied to MCP tools

### Sandbox Primitives (Matt Carey)
- **WorkerD** (Cloudflare): V8 isolates with programmable guardrails — toggle internet access, restrict domains
- **Deno**: JavaScript/TypeScript runtime with sandboxed `deno run` and permission flags
- **Pydantic Monty**: Python code interpreter for untrusted Python code
- More infrastructure primitives expected to emerge as models get smarter

### Enables Saved Mini-Scripts
- Users can save LLM-generated code for reuse — enables cron jobs, web scraping, self-healing scripts
- When a script breaks, the agent fixes it and re-saves it
- Only works when programmatic tool calling is embraced as a pattern

### Enables Stateless Agent Loops
- Cloud-native approach where agent state can be toggled on/off
- Essential when scaling to 100 agents per person

## Related
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — source
- [[summary-20260425 - MCP = Mega Context Problem - Matt Carey]] — source (sandbox primitives, saved scripts, stateless loops)
- [[MCP]] — protocol
- [[CodeMode]] — same technique, originally blogged by Cloudflare
- [[ProgressiveDiscovery]] — companion client-side pattern
- [[Structured Outputs]] — enables type-safe composition
- [[ToolComposition]] — related server-side composition pattern
- [[ClaudeCode]] — uses this pattern with bash commands
- [[WorkerD]] — Cloudflare's sandbox for programmatic tool calling
- [[Deno]] — JavaScript/TypeScript sandbox alternative
- [[Pydantic Monty]] — Python sandbox alternative
- [[Untrusted Code Execution]] — the core safety challenge
- [[Saved Mini-Scripts]] — user-facing pattern enabled by programmatic tool calling
- [[Stateless Agent Loop]] — scaling pattern enabled by programmatic tool calling
