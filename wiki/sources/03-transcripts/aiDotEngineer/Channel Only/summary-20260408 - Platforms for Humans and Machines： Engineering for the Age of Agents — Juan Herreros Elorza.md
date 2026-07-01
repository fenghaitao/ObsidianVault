---
title: "summary-20260408 - Platforms for Humans and Machines： Engineering for the Age of Agents — Juan Herreros Elorza"
type: source
tags: [source, transcript, platform-engineering, agents, self-service]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Platforms for Humans and Machines： Engineering for the Age of Agents — Juan Herreros Elorza.md"]
last_updated: 2026-06-30
---

## Core Summary

Juan Herreros Elorza from Banking Circle presents platform engineering for the age of agents. Best practices are still best practices — but the pain points developers faced (tribal knowledge, manual processes, waiting on other teams) are now impossible for coding agents. Three principles: self-service, API-based, and treating agents as first-class platform consumers.

## Key Points

- Banking Circle: processes 1 trillion euro/year, 700+ regulated financial institutions, 250+ engineers.
- Atlas platform: sub-platforms for compute (Kubernetes), infrastructure, messaging, observability.
- Developer pain story: copy pipeline → it fails → ask teammate → ask infra team → wait → realize you need a database too. Frustrating for humans, impossible for agents.
- Three principles: (1) Self-service — no human in the loop for any platform action. (2) API-based — well-defined, discoverable, schema-validated APIs that agents can call. (3) Treat agents as platform consumers — CLI, MCP server, or direct API access.
- Agents are local, can't walk to the second floor to ask someone. Platform must be fully automatable.

## Related

- [[JuanHerrerosElorza]] — speaker, Banking Circle
- [[BankingCircle]] — fintech company
- [[PlatformEngineering]] — core practice
- [[SelfService]] — platform principle
- [[AgentReadyPlatforms]] — designing platforms for agents
- [[APIDrivenDevelopment]] — API-first approach
