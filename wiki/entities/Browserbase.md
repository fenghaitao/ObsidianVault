---
title: "Browserbase"
type: entity
tags: [company, browser-automation, agent-tools, managed-agents]
sources: ["raw/01-articles/claude/2026-06-09 - New in Claude Managed Agents run agents on a schedule and store environment variables in vaults.md"]
last_updated: 2026-07-07
---

## Definition

Browserbase is a company that provides browser capabilities for [[ClaudeManagedAgents]] through its browse CLI, authenticated via [[AgenticVaults|vaults]]. It is one of the first integrations to give Managed Agents the ability to navigate and interact with the web.

## Key Information

- Built a public catalog of browser skills using the [browse CLI](https://www.npmjs.com/package/browse), authenticated through environment variable vaults.
- Uses a [[ScheduledDeployments|scheduled deployment]] to periodically validate its browser skills catalog to keep it accurate.
- Published a [quickstart guide](https://docs.browserbase.com/integrations/anthropic/managed-agents/quickstart) for integrating with Managed Agents.
- Cited by Anthropic (June 2026) as a key example of CLI-based integration enabling web interaction for agents.

## Related

- [[ClaudeManagedAgents]] — the platform Browserbase integrates with
- [[AgenticVaults]] — the vault feature used for CLI authentication
- [[ScheduledDeployments]] — used for periodic catalog validation
- [[summary-2026-06-09 - New in Claude Managed Agents run agents on a schedule and store environment variables in vaults]] — source announcement
