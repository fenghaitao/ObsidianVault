---
title: "Dynamic Client Registration"
type: concept
tags: [identity, oauth, mcp, protocol]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0.md"]
last_updated: 2026-06-26
---

# Dynamic Client Registration

## Definition

Dynamic Client Registration (DCR) is an OAuth mechanism that allows clients (including MCP servers and AI agents) to dynamically register with an authorization server at runtime, obtaining client credentials without manual pre-configuration.

## Key Information

- **MCP Integration**: Auth0 models MCP servers as OAuth clients that can dynamically register using DCR
- **Flow**: MCP client discovers the authorization server via protected resource metadata (well-known endpoint), registers dynamically, obtains client credentials, then performs standard OAuth flows (authorization code with PKCE)
- **Auth0 Status**: Launched as Early Access (EA) in January 2026
- **Supported Providers**: Works with any provider supporting DCR, static clients, or pre-configured clients
- **Next Spec**: Client ID Metadata is the upcoming specification to extend registration capabilities
- **Scaling Concerns**: There are open concerns about how DCR will scale at production levels
- **Protected Resource Metadata**: Well-known endpoint that advertises supported scopes and authorization server details before registration

- **CIMD Successor**: Client ID Metadata (CIMD) is a newer spec (~3 months old as of April 2026) that supersedes DCR by pre-defining client metadata upfront, avoiding per-session registration
- **Ecosystem Support**: DCR is widely supported among MCP clients and servers, but not universal — Microsoft Entra notably does not support DCR
- **Scaling Concerns**: Open questions about how DCR scales at production levels

## Related

- [[Auth0]]
- [[MCP]]
- [[ProtectedResourceMetadata]]
- [[ScopeBasedAccessControl]]
- [[AgentIdentity]]
- [[ClientIDMetadata]]
- [[MicrosoftEntra]]
- [[summary-20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0]]
- [[summary-20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS]]
