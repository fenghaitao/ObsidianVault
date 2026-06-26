---
title: "Gateways are All You Need — Karan Sampath, Anthropic"
type: source
source_type: transcript
source_url: "https://www.youtube.com/watch?v=aiDotEngineer"
author: "Karan Sampath"
organization: "Anthropic"
date: 2026-04-27
raw_file: "raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gateways are All You Need — Karan Sampath, Anthropic.md"
tags: [mcp, enterprise, gateway, architecture, security, anthropic]
---

# Gateways are All You Need — Karan Sampath, Anthropic

## Core Thesis
Enterprises face three critical challenges with MCP adoption — observability, access control, and security (the "three-headed hydra") — and the solution is an MCP Gateway: a middleware layer that centralizes authentication, access control, routing, observability, and deployment. This establishes a "root of trust" that allows decentralized MCP development across teams while separating the agent harness from the data layer.

## Key Points
- **Enterprise MCP challenges**: Three core problems — observability (who is using which MCP, which tools aren't working), access control (scoping tools to correct users/groups), and security (verifying server safety, preventing data exfiltration, securing remote untrusted clients)
- **Registry gap**: MCP registries are useful but incomplete for enterprises — they lack authentication, access control, observability, and credential management
- **Current bottleneck**: Teams can develop MCPs but can't deploy them; security teams are overloaded; C-suites see agents as ineffective — this bottleneck fundamentally restricts the protocol
- **Root of trust**: Security teams should bless one platform (gateway) to enable decentralized MCP development — the single most important takeaway
- **Gateway definition**: A middleware layer between MCP servers (potentially hundreds) and MCP clients, providing: authentication, access control (role-based), routing/proxy, secured tunnel connections, sub-registry (internal MCP catalog), and CLI tooling
- **Gateway benefits**: (1) Easy addition of new surfaces (Claude.ai, Claude Code, Claude Code Work all connect once), (2) Secured encrypted connections with root trust, (3) Faster iteration without repeated security reviews, (4) Standard primitives encoding enterprise SOPs, (5) Pluggable credentials (company-wide, team-wide, service accounts), (6) Scalable from tens to hundreds of thousands of agents
- **Decentralized development**: Non-technical teams (e.g., legal) can build their own MCP servers focusing only on business logic, not auth/access/observability
- **Agent harness separation**: Long-term vision is separating the agent harness from where data lives — agents shouldn't be tightly coupled to data structure or MCP structure. The gateway is invariant regardless of which agents are used
- **Delegated agent identity**: Agents will require novel definitions of identity that can be uniquely scoped for enterprises
- **Observability nuance**: Beyond usage metrics, enterprises need to understand how tools are being defined and which are load-bearing, to adapt to the rapidly evolving MCP protocol

## Entities
- [[KaranSampath]] — Forward Deployed Engineer at Anthropic, first outside the US
- [[Anthropic]] — AI research company, creator of MCP protocol
- [[aiDotEngineer]] — AI engineering conference and YouTube channel

## Concepts
- [[MCPGateway]] — middleware layer for enterprise MCP deployment
- [[MCPEnterpriseChallenges]] — observability, access control, security as the three-headed hydra
- [[RootOfTrust]] — blessing one platform to enable decentralized development
- [[AgentHarnessSeparation]] — separating agent harness from data layer
- [[DecentralizedMCPDevelopment]] — enabling non-technical teams to build MCP servers
- [[DelegatedAgentIdentity]] — novel identity definitions for AI agents

## Related
- [[MCP]] — the underlying protocol
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — MCP best practices
- [[summary-20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz]] — MCP optimization
- [[summary-20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0]] — agent identity
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — Claude Agent SDK
