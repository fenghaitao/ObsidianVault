---
title: "APIFirstDesign"
type: concept
tags: [api, platform-engineering, agents, design-pattern, self-service]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Platforms for Humans and Machines： Engineering for the Age of Agents — Juan Herreros Elorza.md"]
last_updated: 2026-06-30
---

## Definition
API-first design is the approach of building platforms with well-defined, discoverable APIs as the primary interface, rather than relying on UIs, manual processes, or human-mediated workflows. For AI agents, APIs provide discoverability, schema validation, authentication, and a structured loop for iterative interaction.

## Key Information
- Juan Herreros Elorza argues that agents are "good at calling well-defined APIs" — APIs are the natural interface for machine consumers
- CLIs, MCP servers, and other interfaces can wrap the API, but the API is the foundation
- APIs provide three critical properties for agent interaction:
  1. **Discoverability**: agents can explore what operations are available
  2. **Schema validation**: agents only send valid requests, reducing errors
  3. **Authentication and authorization**: agents can use developer credentials or their own identity securely
- With an API, an agent can iterate in a loop: try something, get a response, adjust, and retry until the task succeeds
- Contrast with UI-based or manual processes that require human interpretation and clicking
- Self-service could take many forms (text, buttons), but API-based self-service is the most agent-friendly
- In the platform context, API-first also means making logs, metrics, and traces available via API/CLI rather than only through graphical dashboards

## Related
- [[summary-20260408 - Platforms for Humans and Machines： Engineering for the Age of Agents — Juan Herreros Elorza]] — source transcript
- [[SelfServicePlatform]] — enabled by API-first design
- [[AgentReadyPlatform]] — the goal state
- [[PlatformEngineering]] — parent discipline
- [[MCP]] — Model Context Protocol, a wrapper pattern for APIs
- [[AgentFirstObservability]] — API-accessible observability
