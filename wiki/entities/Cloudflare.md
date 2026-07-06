---
title: "Cloudflare"
type: entity
tags: [company, infrastructure, cdn, mcp-server, sandboxing]
sources: [raw/01-articles/claude/2026-04-22 - Building agents that reach production systems with MCP.md, "raw/01-articles/claude/2026-05-19 - New in Claude Managed Agents self-hosted sandboxes and MCP tunnels.md"]
last_updated: 2026-07-05
---

## Definition

Cloudflare is a CDN and internet infrastructure company. It is cited by Anthropic as the reference example for designing MCP servers around code orchestration rather than one-to-one API mirroring, and its infrastructure is also used as a self-hosted sandbox option for Claude Managed Agents.

## Key Information

- **MCP server design reference (April 2026)**: Cloudflare's MCP server exposes a thin two-tool surface (search and execute) that lets an agent write and run short scripts against Cloudflare's ~2,500-endpoint API, covering the whole surface in roughly 1,000 tokens — the pattern Anthropic recommends for any service too large for an intent-grouped toolset (alongside AWS and Kubernetes). See [[ModelContextProtocol]].
- **Self-hosted sandbox option**: offered alongside [[Daytona]], [[Modal]], and [[Vercel]] as a self-hosted sandbox environment for [[ClaudeManagedAgents]], keeping agent execution data inside a customer's own perimeter (public beta, May 19, 2026). See [[summary-2026-05-19 - New in Claude Managed Agents self-hosted sandboxes and MCP tunnels]].
- Listed among the initial 10 platforms in Anthropic's May 2025 Integrations launch (Claude.ai connector for CDN/infrastructure management), alongside Atlassian, Zapier, Asana, Sentry, and others. See [[Integrations]].

## Related

- [[summary-2026-04-22 - Building agents that reach production systems with MCP]] — source describing the code-orchestration MCP server pattern
- [[ModelContextProtocol]] — protocol Cloudflare's MCP server implements
- [[ClaudeManagedAgents]] — platform offering Cloudflare as a self-hosted sandbox option
- [[Integrations]] — Claude.ai connector feature that includes Cloudflare
- [[Sandboxing]] — the security pattern Cloudflare's sandbox environment implements
- [[summary-2026-05-19 - New in Claude Managed Agents self-hosted sandboxes and MCP tunnels]] — self-hosted sandboxes launch article naming Cloudflare as a provider
- [[Daytona]] — fellow self-hosted sandbox provider
- [[Modal]] — fellow self-hosted sandbox provider
- [[Vercel]] — fellow self-hosted sandbox provider
