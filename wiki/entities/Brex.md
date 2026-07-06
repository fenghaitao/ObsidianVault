---
title: "Brex"
type: entity
tags: [company, fintech, financial-services, claude-code, ai-adopter]
sources: ["raw/01-articles/claude/2025-10-30 - Building AI agents for financial services.md", "raw/01-articles/claude/2025-10-30 - How Brex improves code quality and productivity with Claude Code.md", "raw/01-articles/claude/2025-11-03 - Building AI agents for startups.md"]
last_updated: 2026-07-04
---

## Definition

Brex is an intelligent finance platform that uses Claude for both customer-facing AI (transaction anomaly detection) and internal engineering productivity via [[ClaudeCode]].

## Key Information

- **Anomaly detection**: Claude powers Brex's review of 100% of transactions, grouping related expenses, flagging policy concerns, and providing explanations with recommended actions for financial professionals.
- Hits 94% compliance rates versus a 70% industry standard, while automating 75% of transactions and saving customers $56.5M annually.
- **Claude Code adoption**: three team case studies —
  - **Andy Reed** (content designer): went from filing engineering tickets for string changes to shipping PRs directly; integrated content guidelines into every component of Brex's design system in days instead of an estimated weeks-to-months; built a Figma plugin reviewing designs against Brex's standards.
  - **Hércules Gimenes** (Product AI team): frames Claude Code as a shift from "driver" to "reviewer" — exploring three implementation approaches in the time one used to take, arriving at a cleaner solution rather than just a faster one. Built a hackathon submission agent in hours using Claude Code's headless mode.
  - **Sumeet Marwaha** (Data & Analytics): built "Brex Explorer," a text-to-SQL interface (Claude Code + MCP servers) for non-SQL staff, plus an AI data-engineering agent letting any engineer add data tables/tests without specialized ORM knowledge — a "4x speed increase across ~2x more contributors." Claude Code adoption at 50% org-wide.
- Claude Code also functions as an informal "oracle" answering questions about Brex's complex Kotlin/Bazel monorepo, reducing reliance on tribal knowledge.

## Related

- [[ClaudeCode]] — the tool driving Brex's internal productivity gains
- [[Figma]] — plugin platform Reed automated with Claude Code
- [[FinancialServicesAI]] — the broader practice Brex exemplifies
- [[summary-2025-10-30 - Building AI agents for financial services]] — source article (anomaly detection)
- [[summary-2025-10-30 - How Brex improves code quality and productivity with Claude Code]] — source article (engineering case studies)
- [[summary-2025-11-03 - Building AI agents for startups]] — source article (compliance and transaction-automation stats)
