---
title: "ScheduledDeployments"
type: concept
tags: [agent-orchestration, automation, cron, managed-agents]
sources: ["raw/01-articles/claude/2026-06-09 - New in Claude Managed Agents run agents on a schedule and store environment variables in vaults.md"]
last_updated: 2026-07-07
---

## Definition

Scheduled deployments are a feature of [[ClaudeManagedAgents]] (public beta, June 2026) that lets agents run on a cron schedule, automatically starting a new session and completing their task each time the schedule fires, with no scheduler for the developer to build or host.

## Key Information

- Each scheduled deployment is given a cron expression that defines its cadence.
- When the schedule fires, the agent starts a new session and executes its task.
- Once live, a deployment can be paused, resumed, archived, or triggered on demand for additional runs.
- Common use cases: nightly data syncs, weekly compliance scans, daily digests, periodic report generation, log monitoring.

### Customer Adoption

- **[[Rakuten]]**: uses scheduled deployments to analyze spreadsheet data and produce reports and decks on a weekly or monthly schedule. Teams also monitor production logs and metrics, allowing product managers to see application health without creating a dashboard.
- **[[ActivelyAI]]**: uses Managed Agents to power cross-account agentic search for sales teams. Scheduled deployments refresh answers regularly, replacing scheduling infrastructure the team initially built themselves.
- **[[Ando]]**: uses scheduled deployments to keep hiring and sales teams moving. Agents autonomously watch channels for proposed next steps, follow up when they're due, and send meeting reminders.
- **[[Browserbase]]**: uses a scheduled deployment to periodically validate its public catalog of browser skills to keep it accurate.

## Related

- [[ClaudeManagedAgents]] — the platform providing scheduled deployments
- [[AgenticVaults]] — complementary vault feature for secure credentials
- [[AgentOrchestration]] — broader pattern of managing agent execution
- [[summary-2026-06-09 - New in Claude Managed Agents run agents on a schedule and store environment variables in vaults]] — source announcement
