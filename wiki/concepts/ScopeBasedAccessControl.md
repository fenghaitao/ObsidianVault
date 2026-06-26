---
title: "Scope-Based Access Control"
type: concept
tags: [identity, authorization, oauth, security]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0.md"]
last_updated: 2026-06-26
---

# Scope-Based Access Control

## Definition

Scope-Based Access Control is an authorization model using OAuth scopes to define fine-grained API access permissions for AI agents. Scopes are defined at the API level and determine which resources and operations an agent can access on behalf of a user.

## Key Information

- **Scopes vs. Roles**: Scopes control API access (what endpoints/operations); roles control persona-based access (what kind of user). FGA handles roles; scopes handle API permissions
- **Definition**: Scopes are defined by the upstream service and are part of the contract between the service and its consumers
- **Connection Mapping**: Local tenant scopes can be mapped/translated to upstream provider scopes at the connection definition level
- **Security**: Authorization happens in SDK code (not LLM-generated code) before tool execution. Scopes not part of the connection definition can never end up in an access token, preventing prompt injection attacks on authorization
- **Well-Known Discovery**: Protected resource metadata endpoints advertise supported scopes for dynamic client registration
- **MCP Integration**: MCP tools are protected by scopes; the MCP server advertises its supported scopes via the well-known endpoint

## Related

- [[Auth0]]
- [[FineGrainedAuthorization]]
- [[TokenExchange]]
- [[MCP]]
- [[AgentIdentity]]
- [[ProtectedResourceMetadata]]
- [[summary-20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0]]
