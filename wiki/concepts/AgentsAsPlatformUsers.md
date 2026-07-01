---
title: "AgentsAsPlatformUsers"
type: concept
tags: [agents, platform-engineering, paradigm, developer-experience, ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Platforms for Humans and Machines： Engineering for the Age of Agents — Juan Herreros Elorza.md"]
last_updated: 2026-06-30
---

## Definition
Agents as platform users is the paradigm that AI coding agents are a distinct user class of internal developer platforms, with different needs, capabilities, and limitations compared to human developers. Platforms must be designed to serve both user classes, not just humans.

## Key Information
- Juan Herreros Elorza's central thesis: platforms must serve both human developers and AI coding agents as first-class users
- AI agents have fundamentally different capabilities and limitations as platform users:
  - **Cannot**: walk to someone's desk, negotiate timelines, interpret fragmented documentation, look at graphical dashboards, wait a week for provisioning
  - **Can**: call well-defined APIs, iterate rapidly in loops, follow structured instructions, consume API-accessible data
- The gap between human and agent capabilities exposes platform deficiencies that were always bad but could be worked around by humans
- Implications for platform design:
  - Observability must be API/CLI-based, not just GUI dashboards
  - Documentation must be structured, discoverable, and machine-consumable
  - Processes must be self-service with no human dependencies
  - Validation must happen locally (shift-left) for fast agent iteration loops
- Related to but distinct from "Agents as Software Users" — focuses specifically on internal platform consumption, not end-user software
- Strategic framing: AI agents are "now working next to us" and platform teams must account for them

## Related
- [[summary-20260408 - Platforms for Humans and Machines： Engineering for the Age of Agents — Juan Herreros Elorza]] — source transcript
- [[AgentReadyPlatform]] — platforms designed for this paradigm
- [[PlatformEngineering]] — the discipline affected
- [[SelfServicePlatform]] — eliminates human dependencies
- [[APIFirstDesign]] — the agent-friendly interface pattern
- [[AgentFirstObservability]] — observability for agent users
- [[AgentFriendlyDocumentation]] — documentation for agent users
- [[Agents as Software Users]] — related broader concept
