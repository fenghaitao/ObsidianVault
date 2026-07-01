---
title: "MCP Tool Description Quality"
type: concept
tags: [mcp, tool-design, agent-interface, quality]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google.md"]
last_updated: 2026-06-30
---

## Definition
MCP Tool Description Quality refers to the standard of MCP server tool descriptions as user interfaces for AI agents. Research cited by Michael Hablich found that 97% of MCP tool descriptions have quality smells, and this matters because "the schema is the UI for the agent."

## Key Information
- 97% of MCP tool descriptions have quality smells per cited research
- Tool descriptions are the primary interface through which agents discover and use tools
- Quality dimensions:
  - **Purpose definition**: clear explanation of core function
  - **Usage guidelines**: activation criteria for when to use/not use
  - **Domain alignment**: using terminology agents can connect to tasks
- Trade-off: better descriptions consume more context window tokens
- Smaller models are particularly affected — they get biased by verbose descriptions and use wrong tools
- "Endless quest for minimum viable description" because models and harnesses keep changing
- Chrome DevTools MCP example: performance trace tool description includes LCP, INP, CLS — web performance metrics that help agents connect the tool to "improve page load" tasks
- Complements [[Tool Description]] (general concept) with specific quality measurement perspective

## Related
- [[summary-20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google]] — source
- [[Tool Description]] — general concept
- [[Agent Discoverability]] — the problem quality descriptions solve
- [[Slim Mode]] — alternative approach (fewer tools, less need for descriptions)
- [[TokenBudget]] — constraint driving the trade-off
