---
title: "Integration Scoping"
type: concept
tags: [ai, agents, security, access-control, integrations, company]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Viktor： AI Coworker That Lives in Slack — Fryderyk Wiatrowski.md"]
last_updated: 2026-06-29
---

## Definition
Integration Scoping is the access control mechanism that distinguishes between personal integrations (available only to the owner in DMs or when they personally invoke the agent) and shared integrations (available company-wide to all team members). It prevents private data exposure in company agents where integrations are inherited across the organization.

## Key Information
- Originated from a Viktor customer incident: an admin at a major US e-commerce brand connected Viktor to their personal Gmail as a team integration, and the team started discussing that person's emails
- Fryderyk Wiatrowski's response: "Why did you give Viktor access to your personal email? If you hire a new employee, do you give them access to your personal email? Probably not."
- **The fix**: Viktor added the capability to scope integrations — they are not always shared. Users can have personal integrations for their own use while team integrations remain separate
- **Why it matters**: Company agents inherit integrations across the team, so without scoping, any connected integration becomes visible to everyone. This creates a data leakage risk that personal agents don't face
- **Design principle**: Treat the AI employee like a human hire — don't give it access to anything you wouldn't give a new employee
- Integration scoping is a necessary complement to [[Shared Context]] — shared context enables the company agent's value, and integration scoping prevents its misuse

## Related
- [[Shared Context]] — the integration model that requires scoping
- [[Company Agent]] — the agent type where integration scoping is critical
- [[Viktor]] — platform that implemented integration scoping
- [[Context Isolation]] — broader security concept that integration scoping supports
- [[AI Employee]] — the "hire, not a tool" philosophy driving scoping
- [[summary-20260511 - Viktor： AI Coworker That Lives in Slack — Fryderyk Wiatrowski]] — source
