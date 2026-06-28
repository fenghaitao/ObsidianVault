---
title: "Slack"
type: entity
tags: [company, communication, search, summarization, claude, integration]
sources: [raw/03-transcripts/Claude/How teams use Claude/04 - How Slack uses Claude for AI search and summaries.md, raw/01-articles/claude/2025-10-01 - Claude and Slack.md]
last_updated: 2026-06-28
---

## Definition

Slack is a business communication platform owned by [[Salesforce]]. Slack uses Claude for AI-powered search and high-volume information summarization internally, and is also deeply integrated with Claude.ai as both a deployable app (Claude in Slack) and a data-source connector (Slack in Claude).

## Internal Use of Claude

Slack uses Claude internally for AI-powered search and summarization, helping users distill through information overload in channels, with improved query success rates and reduced self-reported noise levels. Slack also uses [[ClaudeCode]] internally for bug fixes and accelerating development.

## Claude–Slack Integration (October 2025)

[[Anthropic]] and Slack introduced a bidirectional integration with two modes:

- **Claude in Slack**: The Claude app is installed in a Slack workspace via the Slack Marketplace (available for paid Slack plans). Workspace admins approve the app; individual users then authenticate with their Claude accounts. Claude can help in channels and threads with drafting, document analysis, web search, and other capabilities — drafts are shown privately to the user before posting.
- **Slack connector in Claude**: Slack is connected to Claude.ai as a data source. Claude can then search channels, DMs, and shared files to pull context during conversations and research sessions. Admins enable the connector via the Claude directory; users configure it in the "Connectors" tab of Claude settings.

### Connector Availability by Plan

| Plan | Availability |
|---|---|
| Claude Team | Available at launch (October 2025) |
| Claude Enterprise | Available at launch (October 2025) |
| Claude Pro & Max | Expanded January 26, 2026 |

### Privacy and Security

- Claude only accesses channels and conversations the authenticated user has permission to view.
- Slack conversations follow the organization's existing retention policies and security settings.
- Security standards mirror the user's existing Claude account settings.

## Related

- [[summary-04 - How Slack uses Claude for AI search and summaries]] — source talk on Slack's internal Claude usage
- [[summary-2025-10-01 - Claude and Slack]] — source article on the bidirectional integration
- [[Anthropic]] — model provider and integration partner
- [[ClaudeCode]] — used internally by Slack for development
- [[Salesforce]] — parent company of Slack
- [[Integrations]] — broader category of Claude data-source connectors
- [[ClaudeTeamPlan]] — initial plan tier for the Slack connector
- [[ClaudeEnterprise]] — initial plan tier for the Slack connector
- [[ClaudeMax]] — expanded access as of January 2026
