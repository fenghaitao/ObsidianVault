---
title: "Code Mode"
type: concept
tags: [mcp, llm, tool-calling, optimization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect.md"]
last_updated: 2026-06-26
---

## Definition
Code Mode is an emerging technique where LLMs write code that calls MCP tools in sequence, sidestepping iteration and context problems but introducing sandboxing and code execution concerns.

## Key Information
- First blogged about by Cloudflare, then followed up by Anthropic
- The LLM writes code that calls MCP tools in sequence rather than calling tools one at a time through the agentic loop
- Sidesteps many of the iteration and context problems Lowin describes in his talk
- Lowin doesn't recommend it wholeheartedly due to sandboxing and code execution concerns
- A colleague at Prefect wrote a FastMCP extension supporting code mode the day it was announced
- Initially not included in FastMCP main because the framework tries to be opinionated
- Due to its success, planned for inclusion under an "experiments" or "optimize" CLI flag
- Part of a broader world of "optimizing tool calls"

## Related
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — source
- [[FastMCP]] — framework adding code mode support
- [[MCP]] — protocol this technique works with
- [[Anthropic]] — company that followed up on the technique
