---
title: "Curate Ruthlessly"
type: concept
tags: [mcp, design-pattern, tool-management]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect.md"]
last_updated: 2026-06-26
---

## Definition
Curate Ruthlessly is the MCP design principle of aggressively pruning tools to only the essential outcomes an agent needs, starting with what works and then tearing down to essentials.

## Key Information
- Fifth and final of Jeremiah Lowin's five MCP best practices
- "If you do nothing else, start with what works and then just tear it down to the essentials"
- Lowin still finds himself putting too many tools in servers and having to remind himself to remove them
- Contrasts with normal API development where you keep adding endpoints and maintain backward compatibility -- "it doesn't work here"
- Analogy: "It would be like using a UI that just showed a REST API to a user"
- Case study: Kelly KFL at Fiverr went from 188 tools to 5 tools
- Recommended workflow: start with REST-to-MCP conversion for bootstrapping, then strip out and curate
- "Don't ship the REST API to prod as an MCP server. You will regret it."

## Related
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — source
- [[AgenticProductDesign]] — parent design philosophy
- [[FiftyToolRule]] — heuristic for when curation is needed
- [[TokenBudget]] — constraint driving the need for curation
- [[KellyKFL]] — case study exemplar
- [[OutcomesOverOperations]] — complementary principle
