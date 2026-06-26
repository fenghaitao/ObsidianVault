---
title: "Auth0"
type: entity
category: company
---

# Auth0

## Definition

Auth0 is an identity and access management platform (a product of Okta) that provides authentication and authorization services. In the context of AI agents, Auth0 launched new features for agent identity, token vault, async authorization, and fine-grained access control.

## Key Information

- **Parent Company**: Okta
- **Vision**: "To free everyone to safely use any technology" — a vision that predates the AI era
- **Key AI Agent Features** (launched January 2026):
  - **Token Vault**: Persists upstream refresh tokens and manages token exchange for agents
  - **Async Authorization (CIBA)**: Client Initiated Backchannel Authentication for agent-to-user approval flows
  - **MCP Server Authorization**: Models MCP servers as OAuth clients with DCR and scope-based access
  - **Custom API Client**: Linked client mechanism for MCP servers to access remote APIs
  - **Connected Accounts API**: Manages federated connections between user identities and upstream services
- **Related Products**: FGA (Fine-Grained Authorization) for role-based access control, Guardian (MFA app)
- **SDK Support**: Next.js SDK with middleware wrappers, token exchange helpers (`getAccessTokenForConnection()`)

## Related

- [[Okta]]
- [[PatrickRiley]]
- [[CarlosGalan]]
- [[Guardian]]
- [[TokenVault]]
- [[CIBA]]
- [[AgentIdentity]]
- [[FineGrainedAuthorization]]
- [[summary-20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0]]
