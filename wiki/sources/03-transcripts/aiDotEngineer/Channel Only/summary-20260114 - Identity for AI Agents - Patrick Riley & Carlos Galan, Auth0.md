---
title: "Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0"
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0.md"
date: 2026-01-14
authors: ["Patrick Riley", "Carlos Galan"]
organization: "Auth0 (Okta)"
type: transcript
---

# Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0

## Core Thesis

Auth0 (Okta) launched new identity and authorization features for AI agents built around four pillars: (1) AI needs to know who the user is, (2) AI needs to call APIs on the user's behalf via Token Vault, (3) AI can request user confirmation for risky operations via async CIBA-based authorization, and (4) AI access should be fine-grained with scope-based controls. The presentation demonstrates these features through a live workshop building a Next.js stock trading agent with MCP server integration, token exchange, and push-notification approval flows.

## Key Takeaways

1. **Four pillars of agent identity**: Auth0's framework covers user identity awareness, delegated API access, async user approval for risky operations, and fine-grained scope-based access control.
2. **Token Vault**: A new mechanism for persisting upstream refresh tokens and managing token lifetimes, enabling agents to exchange user tokens for third-party API access tokens without repeated user re-authentication.
3. **Async authorization (CIBA)**: Built on the Client Initiated Backchannel Authentication (CIBA) IETF specification, enabling agents to reach out to users via push notifications (Guardian) or email for approval of risky operations like placing orders.
4. **Rich Authorization Requests (RAR)**: An extension allowing the authorization request to carry structured details (symbol, quantity, price) of what the user is consenting to, recorded in the access token.
5. **MCP server as a client**: Auth0 models MCP servers as OAuth clients, enabling DCR (Dynamic Client Registration), scope-based access to MCP tools, and protected resource metadata endpoints advertising supported scopes.
6. **Custom API Client**: A new linked client mechanism allowing MCP servers to access remote data, with the ability to model any number of API clients independently.
7. **Connected Accounts API**: New API for managing federated connections between user identities and upstream services, enabling the three-way trust relationship between user, agent, and upstream API.
8. **Token Exchange flow**: The SDK provides `getAccessTokenForConnection()` to exchange an agent's access token for an upstream service token with appropriate scopes, handling refresh token lifecycle automatically.
9. **Scope-based access control**: Scopes are modeled around API access (not roles), with translation between local tenant scopes and upstream provider scopes happening at the connection definition level.
10. **Prompt injection resistance**: Authorization happens before tool execution in SDK code (not LLM-generated code), so scopes not part of the connection can never end up in an access token, preventing prompt injection attacks on authorization.

## Entities

- [[PatrickRiley]] — Presenter from Auth0/Okta, formerly at Red Hat
- [[CarlosGalan]] — Co-presenter from Auth0/Okta, based in Spain
- [[Auth0]] — Identity platform (Okta product) providing AI agent authorization features
- [[Okta]] — Identity and access management company, parent of Auth0
- [[Guardian]] — Okta's MFA application used for push notification approval flows
- [[Upstash]] — Database service used in the demo for MCP server state management
- [[aiDotEngineer]] — AI engineering conference and YouTube channel hosting the talk
- [[RedHat]] — Previous employer of Patrick Riley
- [[Abhyek]] — Auth0 architect (nicknamed Shrek) who prepared the workshop material

## Concepts

- [[TokenVault]] — Mechanism for persisting upstream refresh tokens and managing token exchange for AI agents
- [[CIBA]] — Client Initiated Backchannel Authentication protocol for async agent-to-user authorization
- [[AsyncAuthorization]] — Feature enabling agents to request user approval for risky operations via push notifications
- [[DynamicClientRegistration]] — MCP feature for registering new clients dynamically with authorization servers
- [[FineGrainedAuthorization]] — Role-based and scope-based access control for AI agents
- [[AgentIdentity]] — Four-pillar framework for AI agent identity, authentication, and authorization
- [[RichAuthorizationRequests]] — OAuth extension carrying structured consent details in authorization requests
- [[ConnectedAccounts]] — API for managing federated connections between user identities and upstream services
- [[OWASPLLMTop10]] — Updated OWASP top 10 list addressing LLM-specific application security threats
- [[TokenExchange]] — OAuth mechanism for exchanging one token for another with different scopes
- [[CustomAPIClient]] — Linked client mechanism allowing MCP servers and agents to access remote APIs
- [[ScopeBasedAccessControl]] — Fine-grained API access control using OAuth scopes for agent permissions
- [[ProtectedResourceMetadata]] — Well-known endpoint advertising supported scopes and authorization server details

## Related

- [[Auth0]]
- [[Okta]]
- [[TokenVault]]
- [[CIBA]]
- [[AgentIdentity]]
- [[MCP]]
- [[NextJS]]
- [[Vercel]]
