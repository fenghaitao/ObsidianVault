---
title: "GoogleSuiteConnector"
type: entity
tags: [claude, connector, mcp, google-workspace, productivity]
sources: ["raw/01-articles/claude/2026-05-22 - How Anthropic's finance team uses Claude to shape the narrative behind the numbers.md"]
last_updated: 2026-07-07
---

## Definition

Google Suite Connector is a [[ModelContextProtocol|MCP]] connector that links [[ClaudeCowork]] to Google Workspace applications (Docs, Sheets, Slides, Drive, Gmail, Calendar), enabling Claude to read, write, and interact with Google Suite files and data directly within Cowork conversations.

## Key Information

- Part of [[ClaudeCowork]]'s ecosystem of connectors that give Claude access to the same context as the user: documents, local files, email, Slack, and other team knowledge sources.
- Used by [[AliceFong]] on Anthropic's corporate finance team as one of her three primary tools alongside [[ClaudeCowork|Claude Cowork projects]] and [[ClaudeForExcelPowerPoint|Claude for Excel]].
- Enables Claude to work with Google Docs (e.g., monthly financial review documents), Google Sheets (financial models and tables), and Google Drive (supporting context documents).
- Connectors are part of the broader MCP ecosystem; Google Workspace connectors (Calendar, Drive, Gmail) were added to Claude Cowork in February 2026 alongside the private plugin marketplaces and admin controls update.

## Related

- [[ClaudeCowork]] — the product that uses this connector
- [[ModelContextProtocol]] — the protocol underlying MCP connectors
- [[AliceFong]] — Anthropic finance team member who uses this connector
- [[summary-2026-05-22 - How Anthropic's finance team uses Claude to shape the narrative behind the numbers]] — source article
