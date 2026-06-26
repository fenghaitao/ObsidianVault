---
title: "Delegated Agent Identity"
type: concept
tags: [identity, agents, mcp, enterprise, security]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gateways are All You Need — Karan Sampath, Anthropic.md"]
last_updated: 2026-06-26
---

## Definition
Delegated Agent Identity is the concept that AI agents require novel and distinct definitions of identity — separate from human user identity — that can be uniquely defined, scoped, and managed within an enterprise, typically through an MCP Gateway.

## Key Information
- Identified by Karan Sampath (Anthropic) as an important development for the coming year
- Agents will require identity definitions that differ from traditional user identity
- A gateway enables delegated identity in terms of both users and agents
- Access control can be scoped based on whether a team, a user, or an agent is accessing an MCP server
- The gateway can plug into an enterprise's existing IDP (Identity Provider) for authentication
- This enables fine-grained, role-based access control across all agents and MCPs from a single control panel
- Important for the vision of separating the agent harness from the data layer — agents need their own identity to be properly scoped

## Related
- [[MCPGateway]] — the platform enabling delegated agent identity
- [[AgentIdentity]] — broader concept of identity for AI agents
- [[MCP]] — underlying protocol
- [[summary-20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0]] — related talk on agent identity
- [[summary-20260427 - Gateways are All You Need — Karan Sampath, Anthropic]] — source
