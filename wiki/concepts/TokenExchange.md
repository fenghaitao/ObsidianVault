---
title: "Token Exchange"
type: concept
tags: [identity, oauth, agents, protocol]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0.md"]
last_updated: 2026-06-26
---

# Token Exchange

## Definition

Token Exchange is an OAuth mechanism (RFC 8693) that allows one token (the subject token) to be exchanged for another token with different scopes or for a different audience, enabling AI agents to obtain access tokens for upstream services on behalf of users.

## Key Information

- **Standard**: OAuth 2.0 Token Exchange (RFC 8693)
- **AI Agent Use Case**: Agent has an access token for itself; it exchanges that token for an access token to an upstream API (Slack, Google Calendar, stock trading service) with the scopes the user granted
- **Subject Token Types**: Access token (short-lived, for SPA/LangGraph-style flows) or Refresh token (longer-lived, for traditional web apps)
- **Auth0 SDK**: `getAccessTokenForConnection()` method handles the exchange transparently
- **Scope Management**: Only scopes defined in the connection can appear in the resulting token; unrecognized scopes are ignored
- **Token Vault Integration**: Token Vault stores the upstream refresh token and handles the exchange grant automatically

## Related

- [[TokenVault]]
- [[ConnectedAccounts]]
- [[Auth0]]
- [[AgentIdentity]]
- [[ScopeBasedAccessControl]]
- [[summary-20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0]]
