---
title: "Agent Discoverability"
type: concept
tags: [agents, tool-design, mcp, agent-interface, discoverability]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google.md"]
last_updated: 2026-06-30
---

## Definition
Agent Discoverability is the challenge of helping AI agents find and correctly use the right tools from a set of available options. Since "the schema is the UI for the agent," tool descriptions, categorization, and progressive disclosure are the primary discoverability mechanisms.

## Key Information
- Core lesson from Chrome DevTools MCP evolution: moving from 1 monolithic "debug webpage" tool to 25 decomposed tools shifted the problem from capability to discoverability
- According to cited research, 97% of MCP tool descriptions have quality smells
- Key discoverability techniques:
  - **Define purpose**: clearly explain the tool's core function
  - **Usage guidelines**: provide clear activation criteria (when to use/not use)
  - **Domain terminology**: use terms agents can connect to tasks (e.g., LCP/INP/CLS for performance)
  - **Tool categorization**: hide niche tools behind CLI parameters (e.g., Chrome extension debugging)
  - **Slim Mode**: expose only essential tools (3 tools: select page, navigate page, evaluate script)
- Trade-off space: better descriptions increase context window size; smaller models get biased by verbose descriptions
- "Endless quest for minimum viable description" — models and harnesses keep changing
- Skills can supercharge discoverability for intricate workflows, but are not free lunch

## Related
- [[summary-20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google]] — source
- [[Tool Description]] — primary mechanism
- [[Slim Mode]] — extreme form of discoverability optimization
- [[Tool Categorization]] — complementary technique
- [[Agent Skills]] — supercharging mechanism
- [[MCP Tool Description Quality]] — the problem this addresses
- [[Chrome DevTools MCP]] — practical implementation
