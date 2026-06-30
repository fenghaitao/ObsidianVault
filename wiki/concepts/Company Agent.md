---
title: "Company Agent"
type: concept
tags: [ai, agents, company, organization, shared-context, enterprise]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Viktor： AI Coworker That Lives in Slack — Fryderyk Wiatrowski.md"]
last_updated: 2026-06-29
---

## Definition
A Company Agent is an AI agent designed for organizational use, where integrations and context are shared across the entire company rather than owned by individual users. Unlike personal agents where each user connects their own integrations, a company agent inherits permissions from a single connection and makes them available to the whole team.

## Key Information
- Fryderyk Wiatrowski draws a clear distinction between company agents (like Viktor) and personal agents (like OpenClaw)
- **Key difference from personal agents**: Only one person needs to connect an integration — the company agent inherits permissions, and the whole team has access. No need to connect the same integration 100 times
- Company agents "live where you live, work where you work, and have all the company context"
- **Shared context advantage**: In a 100-person company with 20 in the growth team, a company agent means one person connects Meta Ads or analytics, not 20 individual connections. This also prevents errors from someone connecting the wrong integration
- **Scaling challenges unique to company agents**:
  - Memory management at scale: if personal agent memory clutters over time for one user, it happens 100x faster for 100 users
  - Context isolation: the agent is in multiple channels (growth, engineering, executive) and DMs simultaneously — context must not leak between them
  - Access control: DM context should not pull from the growth channel unless the DM user is on the growth team
  - Conflicting instructions: different people in different channels may give conflicting instructions that need resolution
- **Integration scoping**: Company agents need the ability to scope integrations as personal vs shared — learned from a customer incident where an admin connected personal Gmail as a team integration
- **Cloud operation**: Company agents work in the cloud, unlike desktop agents that require a computer to be open
- The company agent concept addresses the gap between personal AI assistants and enterprise-wide AI deployment

## Related
- [[Viktor]] — the company agent platform
- [[AI Employee]] — the role a company agent fills
- [[Personal Agent]] — the individual counterpart
- [[Shared Context]] — the integration model enabling company agents
- [[Context Isolation]] — critical security requirement
- [[Agent Memory]] — the scaling challenge for multi-user company agents
- [[Integration Scoping]] — personal vs shared integration access control
- [[AgentCompanyPattern]] — related organizational pattern
- [[summary-20260511 - Viktor： AI Coworker That Lives in Slack — Fryderyk Wiatrowski]] — source
