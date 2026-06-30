---
title: "Shared Context"
type: concept
tags: [ai, agents, context, integrations, company, organization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Viktor： AI Coworker That Lives in Slack — Fryderyk Wiatrowski.md"]
last_updated: 2026-06-29
---

## Definition
Shared Context is an integration model for company agents where tools and data connections are configured once by a single person and then made available to the entire organization's agent. This eliminates the need for each team member to individually connect the same integrations and prevents errors from incorrect or conflicting integration configurations.

## Key Information
- Described by Fryderyk Wiatrowski as a core differentiator between company agents (Viktor) and personal agents (OpenClaw)
- **How it works**: One person from the company connects an integration (e.g., Meta Ads, PostHog, analytics). The agent inherits permissions, and the whole team has access. "You don't need to connect them 100 times."
- **Benefits**:
  - Reduced setup friction: in a 100-person team with 20 in growth, one person connects vs 20 individual connections
  - Consistency: prevents different team members from connecting different/wrong integrations that could confuse the agent
  - Cloud operation: shared context enables the agent to work without individual computers being open
- **Risk**: Without proper scoping, shared context can expose private data — e.g., an admin connecting personal Gmail as a team integration allows the whole team to discuss that person's emails
- **Mitigation**: Viktor added integration scoping to distinguish between personal integrations (used in DMs by the owner) and shared integrations (available company-wide)
- Shared context is what allows a company agent to have "horizontal and broad context about the whole company" — knowledge no single human employee possesses
- Contrasts with desktop agents like Claude Code where context is limited to the individual user's environment

## Related
- [[Company Agent]] — the agent type that uses shared context
- [[AI Employee]] — the role enabled by shared context
- [[Viktor]] — the platform implementing shared context
- [[Integration Scoping]] — the access control mechanism for shared context
- [[Personal Agent]] — the individual context model contrasted with shared context
- [[Context Isolation]] — preventing shared context from leaking across boundaries
- [[ContextEngineering]] — broader discipline of managing context for agents
- [[summary-20260511 - Viktor： AI Coworker That Lives in Slack — Fryderyk Wiatrowski]] — source
