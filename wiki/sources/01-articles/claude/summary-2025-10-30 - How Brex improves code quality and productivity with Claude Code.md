---
title: "summary-2025-10-30 - How Brex improves code quality and productivity with Claude Code"
type: source
tags: [source, brex, claude-code, case-study]
sources: ["raw/01-articles/claude/2025-10-30 - How Brex improves code quality and productivity with Claude Code.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic profiles three [[Brex]] teams using [[ClaudeCode]]: a content designer who went from filing tickets to independently shipping PRs and a company-wide content-guidelines integration; a Product AI engineering team reframing Claude Code as a "mindset shift" toward reviewing rather than typing; and a Data & Analytics team that built a text-to-SQL interface and an AI data-engineering agent. Reported gains: 3-4x productivity on specific tasks, 50% org-wide adoption, and Claude Code emerging as an informal knowledge repository ("oracle") for Brex's complex Kotlin/Bazel monorepo.

## Key Points

- **Andy Reed** (content designer): previously needed an engineer to change a string; now ships PRs directly. Completed a backlog project embedding content guidelines into every design-system component — estimated weeks/months of manual work done in a few days. Also built a Figma plugin that reviews designs against Brex's standards.
- **Hércules Gimenes** (Product AI team): describes Claude Code as shifting engineers from "driver" to "reviewer" of changes — trying three implementation approaches in the time it used to take for one, arriving at a clearer, cleaner solution rather than just a faster one. Built a hackathon submission agent in hours using Claude Code's headless mode.
- **Sumeet Marwaha** (Data & Analytics): built "Brex Explorer," a text-to-SQL interface (Claude Code + MCP servers) letting non-SQL staff query data in plain English. An AI data-engineering agent lets any engineer add data tables with file edits and test configs that previously required specialized knowledge — a "4x speed increase across ~2x more contributors." Claude Code adoption at 50% org-wide, targeting 100%.
- Claude Code acts as an "oracle" answering questions about how Brex's complex monorepo (Kotlin, Bazel) works, reducing reliance on tribal knowledge in design/engineering meetings.

## Related

- [[Brex]] — subject of this case study
- [[ClaudeCode]] — the tool driving these workflows
- [[Figma]] — plugin built with Claude Code to automate design review
