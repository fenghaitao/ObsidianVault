---
title: "ToolWrapping"
type: concept
tags: [agentic-tools, context-engineering, mcp, descriptions]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz.md"]
last_updated: 2026-06-26
---

## Definition
Tool wrapping is the practice of replacing the generic descriptions of third-party agentic tools with enhanced, use-case-specific descriptions that guide agent behavior, while keeping the underlying tool functionality unchanged.

## Key Information
- Third-party tool descriptions are intentionally generic because they must serve many different use cases.
- Wrapping creates new tools that invoke the original tool's functionality but with custom descriptions tailored to the specific application.
- Enhanced descriptions can guide the agent to prefer certain tools over others, call tools in a specific order, or use tools with particular considerations.
- In Baz's spec reviewer example, the accessibility snapshot tool was given an enhanced description telling the agent to always prefer it over visual screenshots and to call it before any click or hover action.
- Wrapping may increase context window usage due to longer descriptions, creating a trade-off with curation.
- The wrapped tool does exactly what the original tool did — only the description changes.

## Related
- [[summary-20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz]] — source
- [[ThirdPartyToolOptimization]] — parent framework
- [[ToolCuration]] — complementary practice (often combined with wrapping)
- [[ToolComposition]] — next level: creating new tools, not just rewrapping
- [[MCP]] — protocol providing the tools
