---
title: "Connected Accounts"
type: concept
tags: [identity, oauth, federation, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0.md"]
last_updated: 2026-06-26
---

# Connected Accounts

## Definition

Connected Accounts is an Auth0 API for managing federated connections between a user's identity and upstream services (Slack, Google Calendar, stock trading APIs, etc.), enabling AI agents to access those services on the user's behalf through token exchange.

## Key Information

- **Purpose**: Establish the three-way trust relationship between user, agent, and upstream API
- **API**: New "My Account" API for managing all connected accounts
- **Flow**: User connects their account once, granting scopes; Auth0 stores the refresh token; agent can then exchange its token for upstream access tokens without repeated user interaction
- **Connection Definition**: Specifies which scopes to request from the upstream provider; scope translation between local tenant scopes and upstream scopes happens here
- **Token Vault Integration**: Connected accounts feed into Token Vault, which persists refresh tokens and manages token exchange
- **Connection Types**: New "token vault" purpose for connections, distinct from traditional social/identity provider connections

## Related

- [[Auth0]]
- [[TokenVault]]
- [[TokenExchange]]
- [[AgentIdentity]]
- [[summary-20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0]]
