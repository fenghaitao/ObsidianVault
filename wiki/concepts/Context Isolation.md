---
title: "Context Isolation"
type: concept
tags: [ai, agents, security, privacy, company, access-control]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Viktor： AI Coworker That Lives in Slack — Fryderyk Wiatrowski.md"]
last_updated: 2026-06-29
---

## Definition
Context Isolation is the security and architectural requirement that a company-wide AI agent must prevent information from one team or channel from leaking into another. It ensures that context gathered in an executive channel stays there, DM conversations remain private, and the agent respects organizational information boundaries.

## Key Information
- Fryderyk Wiatrowski identifies context isolation as one of the hardest challenges when building a company agent (Viktor) that operates across an entire organization
- **The problem**: A company agent is simultaneously present in multiple channels (growth, engineering, executive, support) and individual DMs. Each has different information sensitivity and access requirements
- **Key isolation requirements**:
  - Context from the growth channel must not leak to engineering or support channels
  - DM context should not pull from the growth channel unless the DM user is on the growth team
  - Executive channel context must be strictly contained
- **Why it's hard**: Unlike a single-thread web app where context is naturally linear and contained, Slack has multiple interaction modes (DMs, channels, threads, reactions, edits) that all serve as agent inputs
- **Interaction complexity**: Users may abandon threads and start new DMs; the agent must roll over context from previous conversations while still respecting isolation boundaries
- **Conflicting instructions**: Different people in different channels may give conflicting instructions — the agent needs rules for resolution while maintaining isolation
- Context isolation is what makes company agents viable in organizations with established hierarchies and access controls

## Related
- [[Company Agent]] — the agent type requiring context isolation
- [[Viktor]] — platform implementing context isolation
- [[AI Employee]] — role that must respect organizational boundaries
- [[Shared Context]] — the integration model that must be balanced with isolation
- [[Integration Scoping]] — personal vs shared access control
- [[Agent Memory]] — memory management across isolated contexts
- [[AgentSocialContext]] — related concept about agent awareness of social/organizational context
- [[summary-20260511 - Viktor： AI Coworker That Lives in Slack — Fryderyk Wiatrowski]] — source
