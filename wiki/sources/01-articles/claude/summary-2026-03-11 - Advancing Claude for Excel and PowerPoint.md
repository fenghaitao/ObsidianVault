---
title: "summary-2026-03-11 - Advancing Claude for Excel and PowerPoint"
type: source
tags: [source, excel, powerpoint, skills, cloud-platforms]
sources: ["raw/01-articles/claude/2026-03-11 - Advancing Claude for Excel and PowerPoint.md"]
last_updated: 2026-07-04
---

## Core Summary

Claude for Excel and Claude for PowerPoint now share full conversational context across all open files — every action in one app is informed by everything happening in the other — and both add-ins gained Skills support plus availability across Amazon Bedrock, Google Cloud's Vertex AI, and Microsoft Foundry.

## Key Points

- **Cross-app context**: Claude can pass context across multiple open Excel and PowerPoint files in one continuous conversation — reading cells, writing formulas, merging datasets, editing slides — without re-explaining the dataset at each step. Example: pull comps from an open workbook, build a trading comps table, drop the valuation summary into a pitch deck, and draft an email, all in one flow.
- **Skills in the add-ins**: any Skill already set up in Claude (personal or org-wide) works inside the Excel/PowerPoint add-ins automatically, the same way MCP connectors do. Anthropic shipped a preloaded starter set of Excel skills (common financial-analysis workflows) and PowerPoint skills (presentation-layer work following an analysis); these starter skills are also bundled in the Financial Analysis plugin, which auto-installs on both add-ins and updates automatically as new skills are added.
- **Instructions**: persistent, app-level preferences (e.g., always use the firm's number formatting, keep PowerPoint bullets to one line, flag hardcoded-assumption cells) set once and applied automatically without re-prompting; Claude can help write/edit instructions.
- **Cloud platform availability**: organizations can access both add-ins via a Claude account or route traffic through an existing LLM gateway to Claude models on Amazon Bedrock, Google Cloud's Vertex AI, or Microsoft Foundry, meeting existing compliance postures.
- Claude also powers Agent Mode natively inside Excel for Microsoft 365 Copilot customers, working alongside Copilot.
- Available in beta on Mac and Windows for all paid plans. *Update (April 10, 2026): Claude for Word beta added for Team and Enterprise plans.*

## Related

- [[ClaudeCodeSkills]] — Skills mechanism now available inside Excel/PowerPoint
- [[AmazonBedrock]] — cloud platform hosting Claude for Excel/PowerPoint
- [[VertexAI]] — cloud platform hosting Claude for Excel/PowerPoint
- [[Microsoft365Copilot]] — Claude's Agent Mode integration inside Excel
- [[ClaudeCowork]] — sibling finance-focused product with its own plugin ecosystem
