---
title: "summary-2026-06-09 - New in Claude Managed Agents run agents on a schedule and store environment variables in vaults"
type: source
tags: [source, claude-blog, managed-agents]
sources: ["raw/01-articles/claude/2026-06-09 - New in Claude Managed Agents run agents on a schedule and store environment variables in vaults.md"]
last_updated: 2026-07-07
---

## Core Summary

Claude Managed Agents introduces two new public beta features: scheduled deployments that let agents run on a cron schedule for recurring automation (nightly syncs, weekly reports, compliance scans) without building or hosting a scheduler, and environment variable support in vaults that lets agents authenticate CLI tools and external services securely — the agent never sees the real key; it's injected at the network boundary and only on approved domains.

## Key Points

- Scheduled deployments use cron expressions to fire agent sessions automatically, with pause, resume, archive, and on-demand trigger controls.
- Environment variable vaults extend the existing vaults feature (previously MCP OAuth only) to support CLI tool authentication via placeholder injection at the network boundary.
- CLI tools are positioned as a fast, lightweight integration path for agents compared to full API integrations.
- Browserbase and KERNEL CLIs give Managed Agents web browser capabilities for the first time, authenticated through vaults.
- Customer examples: Rakuten (scheduled reports and log monitoring), Actively AI (scheduled agentic search refreshes), Ando (scheduled follow-ups and reminders), Notion (CLI + MCP file uploads without token exposure), Browserbase (scheduled catalog validation), KERNEL (usage surge detection), Milana (automated bug fixing with large-scale data analysis).

## Related

- [[ClaudeManagedAgents]] — the platform these features extend
- [[ScheduledDeployments]] — cron-based agent scheduling concept
- [[AgenticVaults]] — secure credential management for agents
- [[Sandboxing]] — the sandbox architecture that enables secure key injection
- [[ModelContextProtocol]] — MCP integration that vaults also support
