---
title: "Agentic Product Design"
type: concept
tags: [mcp, design, agent-interface, product-thinking]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google.md"]
last_updated: 2026-06-30
---

## Definition
Agentic Product Design is the practice of designing interfaces (especially MCP servers) optimized for AI agents rather than humans, accounting for their different strengths and weaknesses on dimensions of discovery, iteration, and context.

## Key Information
- Coined/advocated by Jeremiah Lowin as the central framework for building effective MCP servers
- Based on three key differences between humans and AI agents:
  1. **Discovery**: Cheap for humans (do it once), expensive for agents (every handshake enumerates all tools)
  2. **Iteration**: Fast for humans (write a script, run it), slow for agents (every call sends full history)
  3. **Context**: Humans have rich memory across timescales; agents only have ~200K tokens plus model weights
- Core argument: "Agents deserve their own interface that is optimized for them and their own use case"
- Pushback against the question "if a human can use an API, why can't an AI?" -- humans don't use APIs, they use products (websites, SDKs, mobile apps)
- The most important verb for MCP developers is "curate" -- curating information into an agent-appropriate interface
- Analogy: an agent can find a needle in a haystack, but it will look at every piece of hay and decide if it's a needle
- MCP servers should be treated as user interfaces, not infrastructure or transport technology

## Related
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — source
- [[JeremiahLowin]] — advocate
- [[MCP]] — protocol this design philosophy targets
- [[OutcomesOverOperations]] — key principle
- [[TokenBudget]] — constraint driving design decisions
- [[CurateRuthlessly]] — key principle
- [[AgentStory]] — user story analog for agents
- [[summary-20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google]] — complementary perspective (agents as different user class)
- [[Agents As Different User Class]] — related insight from Michael Hablich
- [[Agent Experience]] — broader UX framework
- [[Chrome DevTools MCP]] — practical implementation example
