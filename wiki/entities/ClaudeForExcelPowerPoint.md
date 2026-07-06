---
title: "Claude for Excel and PowerPoint"
type: entity
tags: [claude, product, excel, powerpoint, office, finance]
sources: ["raw/01-articles/claude/2026-02-05 - Advancing finance with Claude Opus 4.6.md", "raw/01-articles/claude/2026-03-11 - Advancing Claude for Excel and PowerPoint.md", "raw/01-articles/claude/2026-05-07 - Collaborate with Claude across Excel, PowerPoint, Word and Outlook.md"]
last_updated: 2026-07-04
---

## Definition

Claude for Excel, PowerPoint, Word, and Outlook are Office add-ins letting Claude read/edit/create workbooks, presentations, documents, and email/calendar items directly inside Microsoft's apps, sharing one persistent conversation and full context across all open files and all four apps. As of May 7, 2026, Excel/PowerPoint/Word are generally available and Outlook is in public beta.

## Key Information

- **Launch**: Claude in Excel launched with improved handling of complex, long-running tasks; Claude in PowerPoint launched as a research preview in beta (Max/Team/Enterprise) alongside [[Claude4.6Opus|Claude Opus 4.6]] — reading existing layouts/fonts/masters before building or editing decks in-line.
- **Cross-app context (March 2026)**: every action in one app is informed by everything happening in the other — reading cells, writing formulas, merging datasets, editing slides in one continuous conversation without re-explaining context at each step (e.g., pulling comps from a workbook, building a trading comps table, dropping a valuation summary into a deck, and drafting an email in one flow).
- **Skills support**: any Skill already configured in Claude (personal or org-wide) works inside both add-ins automatically. Anthropic shipped a preloaded starter set of Excel (financial-analysis) and PowerPoint (presentation-layer) skills, also bundled in the Financial Analysis plugin (auto-installs, auto-updates).
- **Instructions**: persistent app-level preferences (e.g., firm number formatting, one-line PowerPoint bullets, flagging hardcoded-assumption cells) applied automatically without re-prompting; Claude can help write/edit them.
- **Excel capabilities**: pivot table editing, chart modification, conditional formatting, sorting/filtering, data validation, finance-grade formatting, auto-compaction for long conversations, drag-and-drop multi-file support.
- **Cloud platform availability**: accessible via a Claude account or routed through an existing LLM gateway to Claude models on [[AmazonBedrock]], [[VertexAI|Google Cloud's Vertex AI]], or Microsoft Foundry, meeting existing enterprise compliance postures. Also powers Agent Mode natively inside Excel for [[Microsoft365Copilot]] customers.
- Available in beta on Mac and Windows for all paid plans. *Update (April 10, 2026): Claude for Word beta added for Team and Enterprise plans.*
- **General availability + Outlook beta (May 7, 2026)**: Claude for Excel, PowerPoint, and Word reached general availability; Claude for Outlook launched in public beta for all paid plans. One conversation now carries context across all four apps — e.g., triage an email in Outlook, draft a memo from it in Word, build supporting analysis in Excel, and turn it into a PowerPoint deck, with changes to an Excel assumption automatically flowing into linked PowerPoint charts and Word memo figures (as long as the files are open side by side). Conversations persist per file, so a sidebar session survives being closed and reopened, and can be resumed via keyboard or voice.
- **Claude for Outlook (beta)**: triages the inbox by sorting messages into needs-response / draftable / noise; drafts replies directly into Outlook's native compose pane with recipients, subject, and body pre-filled; and creates calendar invites that check attendee availability and open in Outlook's native event form. Every reply and invite requires explicit user review before sending — nothing is sent automatically. When an attachment from a triaged email is opened in Word or Excel, Claude already has context on what the sender requested.
- **Enterprise admin (May 2026)**: Excel, PowerPoint, and Word ship under one Microsoft AppSource listing; Outlook (beta) has a separate AppSource listing. Both are deployable from the Microsoft admin center. Admins can configure an [[OpenTelemetry]] collector to stream prompts, tool calls, and document references to their own SIEM/collector, and use the [[ComplianceAPI|Analytics API]] to break out activity per user, per app, per day.

## Related

- [[Claude4.6Opus]] — model powering these capabilities
- [[ClaudeCowork]] — sibling finance-focused product with its own plugin ecosystem
- [[ClaudeCodeSkills]] — Skills mechanism now available inside both add-ins
- [[AmazonBedrock]] — cloud platform hosting Claude for Excel/PowerPoint
- [[VertexAI]] — cloud platform hosting Claude for Excel/PowerPoint
- [[Microsoft365Copilot]] — Claude's Agent Mode integration inside Excel
- [[OpenTelemetry]] — admin observability for prompts/tool calls/document references across the four add-ins
- [[ComplianceAPI]] — per-user/per-app/per-day activity breakdown (Analytics API)
- [[summary-2026-02-05 - Advancing finance with Claude Opus 4.6]] — original launch article
- [[summary-2026-03-11 - Advancing Claude for Excel and PowerPoint]] — cross-app context and skills update
- [[summary-2026-05-07 - Collaborate with Claude across Excel, PowerPoint, Word and Outlook]] — GA announcement plus Claude for Outlook beta
