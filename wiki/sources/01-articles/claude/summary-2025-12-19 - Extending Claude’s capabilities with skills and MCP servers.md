---
title: "summary-2025-12-19 - Extending Claude's capabilities with skills and MCP servers"
type: source
tags: [source, skills, mcp, agent-architecture]
sources: ["raw/01-articles/claude/2025-12-19 - Extending Claude’s capabilities with skills and MCP servers.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic clarifies the division of labor between MCP and Skills: MCP provides connectivity (secure, standardized access to external systems), while Skills provide expertise (the domain knowledge and workflow logic that turn raw access into reliable, team-specific outcomes). The two compose — a single skill can orchestrate multiple MCP servers, and a single MCP server can support many skills — illustrated with financial comparable-company-analysis and Notion meeting-prep examples.

## Key Points

- **Hardware-store analogy**: MCP is having access to the aisles (inventory); a Skill is the employee's expertise on what to buy and how to use it. Without the context Skills provide, Claude has to guess at what's wanted.
- **Rule of thumb**: "If you're explaining *how* to do something, that's a skill. If you need Claude to *access* something, that's MCP." MCP instructions should stay generic (query syntax, API formats); skill instructions cover process-specific sequencing (which records to check first, how to cross-reference, output structure).
- **Composability**: adding a new MCP connection lets existing skills incorporate it automatically; refining a skill improves outcomes across every tool it touches. Watch for conflicting instructions between an MCP server's built-in hints and a skill's formatting requirements (e.g., JSON vs. markdown) — let MCP handle connectivity, skills handle presentation/sequencing/logic.
- **Financial example**: a pre-built comparable-company-analysis skill automates a standard valuation workflow, paired with MCP connections to S&P Capital IQ, Daloopa, and Morningstar for live market data — replacing hours of manual metric-pulling and compliance-formatting.
- **Notion example**: a "Meeting Intelligence" skill defines which pages to search and how to structure meeting prep, paired with an MCP server that searches/reads/creates Notion pages.
- Benefits of combining both: clear discovery (skill encodes which sources matter for which tasks), reliable orchestration (predictable multi-step sequencing), and consistent performance (skill defines what "done" looks like for a team).

## Related

- [[ClaudeCodeSkills]] — the concept this article positions relative to MCP
- [[ModelContextProtocol]] — the connectivity layer this article contrasts with Skills
