---
title: "Linear"
type: entity
tags: [product, project-management, issue-tracker]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz.md"]
last_updated: 2026-07-11
---

## Definition

Issue-tracking software that [[Zevi Arnovitz]] integrates directly into his AI development workflow via MCP, letting [[Claude Code]] create and read tickets on his behalf as part of his [[Slash Command Development Workflow]].

## Key Information

- Zevi's `/create issue` slash command uses [[Anthropic]]'s Model Context Protocol (MCP) to let the agent write structured tickets directly into Linear from a quick, mid-development conversation, without Zevi manually opening the tool.
- Later, his `/exploration phase` command can take a Linear ticket ID as an argument, pulling the issue's content back into the agent's context to resume work on it.
- Zevi notes the tickets Claude generates this way are good enough for a solo "company of one" project (where there's no need to coordinate understanding across teams) but says he wouldn't consider them work-ready quality for a larger company's tracker without editing.

## Related

- [[summary-31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz]] — source summary
- [[Zevi Arnovitz]] — integrates this into his workflow
- [[Slash Command Development Workflow]] — the workflow stages that read/write Linear
- [[Claude Code]] — the agent that operates Linear via MCP
