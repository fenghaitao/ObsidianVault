---
title: "Slim Mode"
type: concept
tags: [agents, mcp, tool-design, context-management, token-efficiency]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google.md"]
last_updated: 2026-06-30
---

## Definition
Slim Mode is an extreme form of tool categorization in Chrome DevTools MCP that exposes only three essential tools (select page, navigate page, evaluate script) to agents, minimizing context window consumption at the cost of requiring more agent turns to accomplish tasks.

## Key Information
- Part of Chrome DevTools MCP's token burn reduction strategy
- Exposes only three tools: select page, navigate page, evaluate script
- Pushes tool categorization to its limits for context window savings
- Key trade-off: fewer tools = less context consumed, but agents may need extra turns to achieve the same goal
- Some tasks become impossible without the right tools — e.g., getting network requests cannot be done with evaluate script
- Sits alongside [[Tool Categorization]] (hiding niche tools behind CLI parameters) and [[CLI For Agents]] (command chaining for post-processing)
- Related to the [[FiftyToolRule]] — but Slim Mode goes far below 50 to just 3

## Related
- [[summary-20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google]] — source
- [[Tool Categorization]] — less extreme version
- [[CLI For Agents]] — complementary technique
- [[Tokens Per Successful Outcome]] — metric Slim Mode optimizes for
- [[Chrome DevTools MCP]] — implementation
- [[FiftyToolRule]] — related heuristic
