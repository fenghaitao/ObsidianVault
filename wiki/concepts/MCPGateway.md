---
title: "MCP Gateway"
type: concept
tags: [mcp, enterprise, architecture, middleware, security]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gateways are All You Need — Karan Sampath, Anthropic.md"]
last_updated: 2026-06-26
---

## Definition
An MCP Gateway is a middleware layer positioned between MCP servers and MCP clients that centralizes cross-cutting concerns — authentication, access control, routing, observability, credential management, and deployment — allowing individual MCP server teams to focus solely on business logic.

## Key Information
- **Core components**: Authentication, role-based access control, routing/proxy (clients see only the gateway), secured tunnel connections, sub-registry (internal MCP catalog), and CLI tooling for server creation
- **Root of trust**: The gateway serves as the single platform blessed by security teams, enabling decentralized MCP development across the organization
- **Decoupling**: Any new MCP server does not need to handle auth, access control, observability, or deployment — teams focus only on business logic
- **Surface invariance**: Once the gateway is set up, new agent surfaces (Claude.ai, Claude Code, Claude Code Work) connect once and all MCP servers are available through them
- **Secured connections**: Enables encrypted connections with root trust between MCP servers and clients, addressing enterprise data exfiltration concerns
- **Faster iteration**: Teams can rapidly change MCP servers without repeated security reviews
- **Standard primitives**: Encodes enterprise SOPs and standards into the gateway layer, ensuring all MCP servers adhere to organizational requirements
- **Pluggable credentials**: Supports company-wide, team-wide, and service account credentials that can be swapped intelligently
- **Scalability**: Handles scaling from tens to hundreds of thousands of agents through a single managed surface
- **Observability**: Beyond usage metrics, enables understanding of which tools are load-bearing and how tool definitions evolve with the MCP protocol
- **Gateway CLI**: Tooling that allows agents (via Claude Code or similar) to easily create and integrate new MCP servers

## Related
- [[MCP]] — underlying protocol
- [[MCPEnterpriseChallenges]] — problems the gateway solves
- [[RootOfTrust]] — architectural principle
- [[AgentHarnessSeparation]] — long-term vision enabled by gateways
- [[DecentralizedMCPDevelopment]] — organizational pattern enabled by gateways
- [[DelegatedAgentIdentity]] — identity management through gateways
- [[summary-20260427 - Gateways are All You Need — Karan Sampath, Anthropic]] — source
