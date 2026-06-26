---
title: "Custom API Client"
type: concept
tags: [identity, agents, mcp, api]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0.md"]
last_updated: 2026-06-26
---

# Custom API Client

## Definition

Custom API Client is an Auth0 mechanism that allows creating linked API clients for MCP servers and AI agents to access remote data. It models APIs as linked resources that can be independently configured with their own client credentials and scopes.

## Key Information

- **Purpose**: Enable MCP servers (and other agentic components) to access remote APIs with proper authentication
- **Linked Clients**: APIs can be linked to clients (agent clients or MCP server clients), creating a modeled relationship in the Auth0 tenant
- **Multiple Clients**: Any number of API clients can be created for different services or architectural patterns
- **MCP Integration**: MCP servers use custom API clients to perform backchannel authorization requests and access upstream data
- **Configuration**: Each custom API client has its own client ID and secret, with specific grant types and scopes

## Related

- [[Auth0]]
- [[MCP]]
- [[AgentIdentity]]
- [[TokenVault]]
- [[summary-20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0]]
