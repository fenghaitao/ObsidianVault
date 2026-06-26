---
title: "Protected Resource Metadata"
type: concept
tags: [identity, oauth, mcp, protocol]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0.md"]
last_updated: 2026-06-26
---

# Protected Resource Metadata

## Definition

Protected Resource Metadata is a well-known endpoint (part of the OAuth 2.0 Protected Resource Metadata specification) that advertises the supported scopes and authorization server details for a protected resource, enabling dynamic client registration and discovery for MCP servers and other OAuth clients.

## Key Information

- **Standard**: OAuth 2.0 Protected Resource Metadata
- **Endpoint**: Well-known URL that returns supported scopes, authorization server location, and other metadata
- **MCP Integration**: MCP servers expose this endpoint so that MCP clients (like Claude, ChatGPT) can discover what scopes are needed and where to authorize
- **Flow**: Client fetches metadata → discovers scopes and authorization server → performs DCR → obtains access token with appropriate scopes
- **Auth0 Implementation**: Part of the MCP authorization preview, with middleware for scope verification on the MCP server side

## Related

- [[DynamicClientRegistration]]
- [[MCP]]
- [[ScopeBasedAccessControl]]
- [[Auth0]]
- [[summary-20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0]]
