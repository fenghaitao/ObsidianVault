---
title: "Tool Description"
type: concept
tags: [agents, tools, prompt-engineering, agentic-search]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google.md"]
last_updated: 2026-06-30
---

## Definition

Tool descriptions are the text that tells an AI agent what a tool does, when to use it, and how to use it. They are the most important aspect of tool design for agentic search, yet are often treated with the least effort. Well-crafted tool descriptions are critical for preventing agents from calling the wrong tool or generating incorrect parameters.

## Key Information

- **Core purpose**: Start with a clear statement of what the tool does — if this works, great
- **Trigger conditions**: When the agent struggles, add explicit guidance on when this tool should and should not be used
- **Relationships**: Specify tool ordering — e.g., "first call the agent skill before using this tool" or "get confirmation before calling this tool"
- **System prompt reinforcement**: If the perfect tool description still doesn't work, reinforce it in the agent system prompt
- **Parameter complexity**: Simple parameters (IDs, search strings) are easy; complex parameters (full query languages like ESQL/SQL) are much harder for agents
- **Error handling**: Tools should return errors to the agent so it can self-correct rather than crashing — critical for complex parameter tools
- **Anti-pattern**: One-sentence tool descriptions that don't explain when or how to use the tool
- **Progressive enhancement**: Start simple, add detail only when the agent demonstrates confusion
- **Michael Hablich's perspective**: "The schema is the UI for the agent" — 97% of MCP tool descriptions have quality smells. Fixing descriptions is a trade-off: better descriptions consume more context window, and smaller models get biased by verbose descriptions. Domain terminology (e.g., LCP/INP/CLS for performance tools) helps agents connect tools to tasks.

## Related

- [[summary-20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic]] — source transcript
- [[summary-20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google]] — source (schema is the UI)
- [[Agentic Search]] — the context where tool descriptions matter most
- [[ToolCalling]] — the mechanism that uses tool descriptions
- [[ToolCuration]] — complementary practice
- [[Agent Skills]] — progressive disclosure for complex tool documentation
- [[Low Floor High Ceiling]] — tool design strategy
- [[MCP Tool Description Quality]] — related concept from Michael Hablich
- [[Agent Discoverability]] — problem tool descriptions solve
