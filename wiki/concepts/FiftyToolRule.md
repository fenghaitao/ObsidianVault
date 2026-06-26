---
title: "Fifty Tool Rule"
type: concept
tags: [mcp, heuristic, performance, tool-design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect.md"]
last_updated: 2026-06-26
---

## Definition
The Fifty Tool Rule is a heuristic stating that agent performance begins to degrade when more than ~50 tools are available to a single agent, serving as a design constraint for MCP server scope.

## Key Information
- Proposed by Jeremiah Lowin as a rule of thumb for MCP server design
- "50 tools is where I draw the line where you're going to have performance problems"
- Clarified: it's 50 tools per agent, not per server (two 50-tool servers = 100 tools to the agent)
- Some practitioners argue for even lower limits
- Having more than 50 tools is a "smell" that prompts questions: can they be split? Are admin tools mixed with user tools? Could namespacing or multiple servers help?
- GitHub's server has ~170 tools but compensates with semantic routing techniques
- Ideal range: 5-15 tools
- "It's an aspiration that you should have and just be careful unless you are prepared to invest in a lot of care and evaluation"
- Kelly KFL's Fiverr server went from 188 to 5 tools, validating the heuristic

## Related
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — source
- [[CurateRuthlessly]] — strategy for staying under the limit
- [[TokenBudget]] — underlying constraint
- [[KellyKFL]] — case study
- [[AgenticProductDesign]] — parent design philosophy
