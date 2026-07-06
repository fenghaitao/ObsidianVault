---
title: "summary-2026-05-19 - New in Claude Managed Agents self-hosted sandboxes and MCP tunnels"
type: source
tags: [source, claude-managed-agents, sandboxing, mcp, mcp-tunnels, enterprise-security]
sources: ["raw/01-articles/claude/2026-05-19 - New in Claude Managed Agents self-hosted sandboxes and MCP tunnels.md"]
last_updated: 2026-07-05
---

## Core Summary

Anthropic announces two new capabilities for [[ClaudeManagedAgents]] that keep agent execution and tool access inside a customer's own security perimeter: self-hosted sandboxes (public beta) and MCP tunnels (research preview). With self-hosted sandboxes, the agent loop (orchestration, context management, error recovery) still runs on Anthropic's infrastructure, but the sandbox where tools actually execute runs on infrastructure the customer controls, their own servers or a managed sandbox provider ([[Cloudflare]], [[Daytona]], [[Modal]], [[Vercel]]), so sensitive files, packages, and services never leave the customer's network, and the customer controls compute sizing and runtime images. With MCP tunnels, agents reach [[ModelContextProtocol|MCP]] servers inside a private network (internal databases, private APIs, knowledge bases, ticketing systems) without exposing them publicly: a lightweight customer-deployed gateway makes a single outbound, end-to-end-encrypted connection, requiring no inbound firewall rules or public endpoints. MCP tunnels works with both Managed Agents and the Messages API, and is administered from workspace settings in the Claude Console by organization admins.

## Key Points

- Self-hosted sandboxes (public beta): tool execution moves to customer-controlled infrastructure while orchestration, context management, and error recovery stay on Anthropic's side; existing network policies, audit logging, and security tooling inside the customer's perimeter automatically apply, and files/repositories never leave it.
- Sandbox client choice: bring any sandbox client, or start with a supported provider, [[Cloudflare]], [[Daytona]], [[Modal]], [[Vercel]], with [[Amplitude]], [[Clay]], and [[Rogo]] also named alongside the provider list (source does not specify whether these three are customers or additional providers).
- Compute control: resource sizing and runtime image are set by the customer, so compute-heavy tasks (long builds, image generation) get the CPU/memory/capacity they need.
- MCP tunnels (research preview): connects agents to MCP servers inside a private network without exposing them to the public internet; a customer-deployed gateway makes one outbound connection (no inbound firewall rules, no public endpoints), traffic encrypted end to end.
- MCP tunnels availability: supported in both Managed Agents and the Messages API; managed from workspace settings in the Claude Console by organization admins; request access required.
- Both features "work within the same core primitives supported by Managed Agents"; docs and a cookbook (anthropics/claude-cookbooks/managed_agents/self_hosted_sandboxes) are provided to set up a sandbox provider.

## Related

- [[ClaudeManagedAgents]] — the product these two features extend
- [[Sandboxing]] — the security pattern self-hosted sandboxes implement at the infrastructure level
- [[ModelContextProtocol]] — the protocol MCP tunnels extends to private-network servers
- [[Cloudflare]] — supported self-hosted sandbox provider
- [[Daytona]] — supported self-hosted sandbox provider
- [[Modal]] — supported self-hosted sandbox provider
- [[Vercel]] — supported self-hosted sandbox provider
