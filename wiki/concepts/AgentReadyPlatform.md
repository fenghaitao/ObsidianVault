---
title: "AgentReadyPlatform"
type: concept
tags: [agents, platform-engineering, ai, developer-experience, self-service]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Platforms for Humans and Machines： Engineering for the Age of Agents — Juan Herreros Elorza.md"]
last_updated: 2026-06-30
---

## Definition
An agent-ready platform is an internal developer platform (IDP) designed to be consumable by AI coding agents as first-class users, not just by human developers. It eliminates human-mediated processes, provides API/CLI interfaces, validates early, exposes observability programmatically, and maintains structured, discoverable documentation.

## Key Information
- Juan Herreros Elorza argues that platforms must serve two user classes: human developers and AI coding agents
- AI agents cannot compensate for platform deficiencies the way humans can — they cannot walk to someone's desk, negotiate timelines, or interpret fragmented documentation
- Six pillars of an agent-ready platform:
  1. **Self-service**: no human-dependent processes; agents trigger everything independently
  2. **API-based**: well-defined APIs with discoverability, schema validation, and auth
  3. **Local-first / shift-left**: validate and fail as early as possible, on the local machine
  4. **Agent-first observability**: logs, metrics, and traces available via API/CLI, not just GUI dashboards
  5. **Structured documentation**: agents.md files, skills, centralized or co-located docs, API-accessible documentation
  6. **Contribution-friendly**: guardrails (policies) plus agent guidance (agents.md, skills) to enable community contributions
- The core insight: "best practices are still best practices" — these were always good ideas, but AI agents make the pain of not following them "much more obvious and perhaps much more painful"
- Strategic framing: use organizational AI interest as leverage to implement platform best practices that previously faced resistance

## Related
- [[summary-20260408 - Platforms for Humans and Machines： Engineering for the Age of Agents — Juan Herreros Elorza]] — source transcript
- [[PlatformEngineering]] — parent discipline
- [[SelfServicePlatform]] — pillar 1
- [[APIFirstDesign]] — pillar 2
- [[ShiftLeftValidation]] — pillar 3
- [[AgentFirstObservability]] — pillar 4
- [[AgentFriendlyDocumentation]] — pillar 5
- [[AgentsAsPlatformUsers]] — the paradigm shift
- [[AgentsDotMd]] — agent configuration files
- [[Skills]] — reusable agent playbooks
- [[MCP]] — API wrapper pattern for agents
