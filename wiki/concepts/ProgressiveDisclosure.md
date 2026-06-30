---
title: "Progressive Disclosure"
type: concept
tags: [mcp, design-pattern, context, token-budget]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - The Future of MCP — David Soria Parra, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-29
---

## Definition
Progressive Disclosure is a design pattern for MCP servers where tool information is revealed incrementally rather than all at once during handshake, reducing initial token consumption.

## Key Information
- Discussed during Q&A as a technique for managing the token budget problem
- One approach: on initialization, describe each tool at a high level (95% less context), then expose full details only when the agent needs a specific tool
- Can be implemented as spec-compliant tool calls that provide more information on demand
- Challenge: creates "meta-tools" where agents use tools to learn about tools, adding complexity
- Another form: using error messages for progressive disclosure (documenting recovery from common failures)
- Claude Desktop's SQLite caching breaks many progressive disclosure techniques because it ignores subsequent tool list updates
- Lowin notes this is "usually implemented as a dedicated product" rather than a simple pattern

## Related
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — source
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — source (progressive discovery as client-side counterpart)
- [[summary-20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic]] — source (agent skills as progressive disclosure for tool parameters)
- [[TokenBudget]] — constraint this pattern addresses
- [[ErrorsAsPrompts]] — related form of progressive disclosure
- [[ClaudeDesktop]] — client that breaks progressive disclosure
- [[MCP]] — protocol
- [[ProgressiveDiscovery]] — related client-side pattern for on-demand tool loading
- [[ToolSearch]] — mechanism for progressive discovery
- [[Agent Skills]] — uses progressive disclosure for skill documentation
