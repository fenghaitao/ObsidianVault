---
title: "Root of Trust"
type: concept
tags: [security, architecture, mcp, enterprise, gateway]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gateways are All You Need — Karan Sampath, Anthropic.md"]
last_updated: 2026-06-26
---

## Definition
Root of Trust, in the context of enterprise MCP deployments, is the architectural principle of blessing a single platform (gateway) through which all MCP traffic flows, enabling security teams to establish trust once while allowing decentralized development across the organization.

## Key Information
- Described by Karan Sampath as the single most important takeaway from his talk
- Core intuition: when all teams can build MCP servers (via coding agents), security teams need one platform to bless rather than reviewing every individual server
- Enables enterprises to explore MCP usage and thereby explore how powerful agents can be
- Has knock-on effects: every good MCP helps all agents in the company, so the investment compounds
- The gateway becomes the root of trust — all MCP clients see only the gateway, and MCP servers treat the gateway as the only trusted endpoint
- Enables secured encrypted connections between untrusted remote clients and internal enterprise data
- Used successfully both internally at Anthropic and externally with enterprise customers

## Related
- [[MCPGateway]] — the platform that embodies the root of trust
- [[MCPEnterpriseChallenges]] — problems solved by establishing a root of trust
- [[MCP]] — underlying protocol
- [[summary-20260427 - Gateways are All You Need — Karan Sampath, Anthropic]] — source
