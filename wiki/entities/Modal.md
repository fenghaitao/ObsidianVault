---
title: "Modal"
type: entity
tags: [company, infrastructure, sandboxing, claude-managed-agents]
sources: ["raw/01-articles/claude/2026-05-19 - New in Claude Managed Agents self-hosted sandboxes and MCP tunnels.md"]
last_updated: 2026-07-05
---

## Definition

Modal is a managed sandbox/compute provider offered as a self-hosted sandbox option for [[ClaudeManagedAgents]], letting customers run Claude agent tool execution on infrastructure Modal manages instead of building their own sandbox environment.

## Key Information

- Listed alongside [[Cloudflare]], [[Daytona]], and [[Vercel]] as one of the supported providers customers can start with when setting up self-hosted sandboxes for Claude Managed Agents (public beta, May 19, 2026).
- Anthropic provides a dedicated GitHub reference implementation, `modal-labs/claude-managed-agents-modal-sandbox`, for integrating Modal as a sandbox provider.
- The source article does not provide further detail on Modal's product beyond its role as a sandbox provider.

## Related

- [[summary-2026-05-19 - New in Claude Managed Agents self-hosted sandboxes and MCP tunnels]] — source announcing Modal as a self-hosted sandbox provider
- [[ClaudeManagedAgents]] — product Modal provides sandbox infrastructure for
- [[Sandboxing]] — the security pattern this provider role implements
- [[Cloudflare]] — fellow self-hosted sandbox provider
- [[Daytona]] — fellow self-hosted sandbox provider
- [[Vercel]] — fellow self-hosted sandbox provider
