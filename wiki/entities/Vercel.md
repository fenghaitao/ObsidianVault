---
title: "Vercel"
type: entity
tags: [company, infrastructure, sandboxing, claude-managed-agents]
sources: ["raw/01-articles/claude/2026-05-19 - New in Claude Managed Agents self-hosted sandboxes and MCP tunnels.md", "raw/01-articles/claude/2026-06-17 - Claude Design now stays on brand for daily work.md"]
last_updated: 2026-07-05
---

## Definition

Vercel is a managed sandbox/compute provider offered as a self-hosted sandbox option for [[ClaudeManagedAgents]], letting customers run Claude agent tool execution on infrastructure Vercel manages instead of building their own sandbox environment.

## Key Information

- Listed alongside [[Cloudflare]], [[Daytona]], and [[Modal]] as one of the supported providers customers can start with when setting up self-hosted sandboxes for Claude Managed Agents (public beta, May 19, 2026).
- Anthropic's docs point to a Vercel-specific guide ("Run Claude Managed Agent tools with Vercel Sandbox") for setting up Vercel as a sandbox provider.
- The source article does not provide further detail on Vercel's product beyond its role as a sandbox provider.

## Related

- [[summary-2026-05-19 - New in Claude Managed Agents self-hosted sandboxes and MCP tunnels]] — source announcing Vercel as a self-hosted sandbox provider
- [[ClaudeManagedAgents]] — product Vercel provides sandbox infrastructure for
- [[Sandboxing]] — the security pattern this provider role implements
- [[Cloudflare]] — fellow self-hosted sandbox provider
- [[Daytona]] — fellow self-hosted sandbox provider
- [[Modal]] — fellow self-hosted sandbox provider
- [[ClaudeDesign]] — exports to Vercel as a connector destination
- [[summary-2026-06-17 - Claude Design now stays on brand for daily work]] — source listing Vercel as a connector
