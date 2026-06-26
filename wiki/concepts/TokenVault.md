---
title: "Token Vault"
type: concept
tags: [identity, authorization, agents, oauth]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0.md"]
last_updated: 2026-06-26
---

# Token Vault

## Definition

Token Vault is an Auth0 mechanism for persisting upstream refresh tokens and managing token exchange for AI agents. It stores refresh tokens, manages access token lifetimes, and enables agents to exchange their own tokens for third-party API access tokens without requiring repeated user re-authentication.

## Key Information

- **Purpose**: Enables the three-way trust relationship between user, agent, and upstream API by persisting and managing tokens
- **Core Functions**:
  - Stores upstream refresh tokens after the user connects an account
  - Manages access token lifetimes and automatic refresh
  - Provides token exchange: agent's access token → upstream service access token
  - Handles scope management during exchange
- **SDK Integration**: `getAccessTokenForConnection()` method simplifies the token exchange flow
- **Connection Types**: Supports both access token exchange (for SPAs, LangGraph-style external APIs) and refresh token exchange (for traditional web apps with embedded agents)
- **Security**: Tokens are stored server-side; scopes not part of the connection definition can never end up in an access token

## Related

- [[Auth0]]
- [[Okta]]
- [[TokenExchange]]
- [[ConnectedAccounts]]
- [[AgentIdentity]]
- [[summary-20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0]]
