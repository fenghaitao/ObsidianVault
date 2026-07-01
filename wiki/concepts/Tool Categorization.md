---
title: "Tool Categorization"
type: concept
tags: [agents, mcp, tool-design, context-management]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google.md"]
last_updated: 2026-06-30
---

## Definition
Tool Categorization is the practice of hiding niche or specialized tools behind command-line parameters rather than exposing them in the default agent tool list, reducing context window consumption by only surfacing tools relevant to the agent's current task.

## Key Information
- First of three token burn reduction angles in Chrome DevTools MCP
- Example: Chrome extension debugging tools are hidden behind CLI parameters because not everyone develops Chrome extensions
- "Why add it to the default context menu? There's no point in doing that"
- More moderate approach than [[Slim Mode]] (which exposes only 3 tools)
- Complements [[CLI For Agents]] — niche tools can be accessed via CLI when needed
- Related to [[CurateRuthlessly]] (Jeremiah Lowin) — both are about being selective with tool exposure
- Trade-off: agents can't discover niche tools unless they know to look for them

## Related
- [[summary-20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google]] — source
- [[Slim Mode]] — extreme version
- [[CLI For Agents]] — complementary technique
- [[CurateRuthlessly]] — related concept from Jeremiah Lowin
- [[Agent Discoverability]] — the problem this helps solve
- [[Chrome DevTools MCP]] — implementation
