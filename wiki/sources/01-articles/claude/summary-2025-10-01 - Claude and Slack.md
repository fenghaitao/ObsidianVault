---
title: "summary-2025-10-01 - Claude and Slack.md"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2025-10-01 - Claude and Slack.md"]
last_updated: 2026-06-28
---

## Core Summary

Claude and [[Slack]] are integrated bidirectionally: Claude can be added directly to a Slack workspace for in-channel AI assistance, and a Slack workspace can be connected to [[Claude.ai]] as a data-source connector so Claude can search conversations and files to provide richer context during deeper work sessions.

## Key Points

- **Two integration modes**: (1) Claude in Slack — the Claude app is installed in a workspace from the Slack Marketplace; (2) Slack connector in Claude — Slack is connected as a data source so Claude can search channels, DMs, and shared files during conversations.
- **Capabilities in Slack**: Users get Claude's full existing capabilities (web search, document analysis, existing connectors) directly inside Slack channels and threads. Claude drafts responses privately first; users review and edit before sharing with the team.
- **Permissions and privacy**: Claude only accesses public and private Slack channels the authenticated user has permission to view. Conversations follow the organization's existing Slack retention policies and security settings. Workspace administrators must approve the Claude app before individual users can authenticate.
- **Connector availability**: The Slack connector was initially available for Claude Team and Enterprise plan customers. As of January 26, 2026 it was expanded to [[ClaudeMax|Claude Pro and Max]] subscribers.
- **Agentic enterprise framing**: Rob Seaman (Chief Product Officer of Slack at [[Salesforce]]) described the integration as accelerating the "agentic enterprise" — where AI agents work alongside humans in the flow of work.
- **Admin controls**: Workspace administrators control organization-wide app approval; individual users authenticate with their existing Claude accounts. The connector is enabled by admins via the Claude directory, then configured by users in the "Connectors" tab of Claude settings.
- **Use cases**: Preparing for meetings by pulling relevant Slack discussions, gathering project updates from multiple channels, finding action items buried in team conversations, and drafting responses to critical messages.

## Related

- [[Slack]] — Communication platform integrated with Claude
- [[Integrations]] — Broader category of Claude data-source connectors
- [[ClaudeTeamPlan]] — Initial plan tier for the Slack connector
- [[ClaudeEnterprise]] — Initial plan tier for the Slack connector
- [[ClaudeMax]] — Expanded access as of January 2026 (Pro and Max)
- [[Salesforce]] — Parent company of Slack; quoted endorsing the integration
- [[AIAgent]] — "Agentic enterprise" framing in the article
