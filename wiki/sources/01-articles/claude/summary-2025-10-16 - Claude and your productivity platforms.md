---
title: "summary-2025-10-16 - Claude and your productivity platforms"
type: source
tags: [source, original-material, microsoft-365, enterprise-search, mcp]
sources: ["raw/01-articles/claude/2025-10-16 - Claude and your productivity platforms.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic launched a Microsoft 365 connector for Claude (via [[ModelContextProtocol|MCP]]) giving Claude access to SharePoint/OneDrive, Outlook, and Teams, plus [[EnterpriseSearch|enterprise search]] — a dedicated, company-branded shared project that searches across all of an organization's connected data sources in one place. This is the reverse-direction integration from [[Microsoft365Copilot]] (where Claude is a model option inside Microsoft's Copilot product): here, Claude itself connects out to Microsoft 365 as a data source alongside other connected tools.

## Key Points

- **Microsoft 365 connector** (via Anthropic's MCP connector): lets Claude access and reason over documents, communications, and calendar data to help with decisions and problem-solving.
  - **SharePoint and OneDrive**: search and analyze documents across sites and libraries without manual upload.
  - **Outlook**: access email threads and analyze communication patterns for project status, client feedback, team alignment.
  - **Teams**: search chat conversations, channel discussions, and meeting summaries to surface decisions and track updates.
  - Available today for all Claude Team and Enterprise plan customers; admins must enable the connector before individual users authenticate.
- **Enterprise search**: a dedicated, company-branded shared project with custom prompts for searching effectively across all of an organization's connected tools; everyone in the org gets automatic access once an admin sets it up and connects tools.
  - Example: asking about a company's remote-work policy pulls from HR documents in SharePoint, email discussions in Outlook, and team guidelines from other sources into one report.
  - Particularly valuable for onboarding, analyzing patterns in customer feedback, and identifying the right internal experts to consult.
  - Enabled for all Team and Enterprise organizations; admins customize the project and curate data sources.

## Related

- [[Microsoft]] — the company whose productivity suite Claude connects to
- [[Microsoft365Copilot]] — the inverse integration (Claude embedded inside Microsoft's product)
- [[Integrations]] — the broader connector framework this M365 connector belongs to
- [[EnterpriseSearch]] — the cross-tool search capability this article introduces
- [[ModelContextProtocol]] — underlying protocol for the M365 connector
