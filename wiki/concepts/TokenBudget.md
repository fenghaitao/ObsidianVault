---
title: "Token Budget"
type: concept
tags: [mcp, context-window, constraints, design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect.md"]
last_updated: 2026-06-26
---

## Definition
The Token Budget is the finite context window that constrains how much tool documentation, conversation history, and data an AI agent can hold at once, making it a critical design constraint for MCP servers.

## Key Information
- Fourth of Jeremiah Lowin's five MCP best practices, and the only one he considers non-negotiable
- "If you don't actually do it, you will simply not have a usable server"
- On handshake, agents typically download all tool descriptions in one go
- GitHub's MCP server reportedly ships ~200K tokens on handshake
- With 800 tools and a 200K token window, each tool gets only ~250 tokens for name, schema, and documentation
- If an agent connected to a server with one more tool that had a one-word docstring, it would overflow
- The token budget is a "very scarce resource" and "your server is not the only one that the agent is going to talk to"
- Techniques for saving tokens: sending instructions in error messages instead of docstrings, progressive disclosure, tool curation
- The answer "can't always be do less" -- frameworks and clients need to find ways to solve this problem too

## Related
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — source
- [[AgenticProductDesign]] — parent design philosophy
- [[CurateRuthlessly]] — primary strategy for managing token budget
- [[ProgressiveDisclosure]] — technique for reducing handshake tokens
- [[ErrorsAsPrompts]] — technique for offloading documentation to error messages
- [[FiftyToolRule]] — heuristic derived from token budget constraints
- [[Context Management]] — broader context management concept
