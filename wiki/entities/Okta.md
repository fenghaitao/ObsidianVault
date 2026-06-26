---
title: "Okta"
type: entity
category: company
---

# Okta

## Definition

Okta is an identity and access management company that owns Auth0. In the AI agent space, Okta provides enterprise-level control over what agents acting on behalf of employees can do, complementing Auth0's developer-focused agent identity features.

## Key Information

- **Products**: Auth0 (developer identity platform), FGA (Fine-Grained Authorization), Guardian (MFA)
- **Role in AI Agents**: Provides enterprise governance layer — when an employee's agent acts on their behalf, the company needs control over what those agents can do
- **Auth0 Bridge**: Okta and Auth0 work together on protocols, with Okta handling enterprise policy enforcement and Auth0 providing the developer-facing agent identity features
- **Vision**: "To free everyone to safely use any technology" (shared with Auth0)

- **XAA/ID JAG Support**: Okta supports Cross-App Access (XAA) via the ID JAG spec for OIDC-based connections, with SAML-based support planned. IT admins configure managed connection policies specifying which MCP clients can request access to which MCP servers
- **Managed Connections Portal**: New Okta feature where IT admins define policies like "Cursor can request access to Figma" — Okta validates these policies when issuing ID JAG tokens

## Related

- [[Auth0]]
- [[Guardian]]
- [[FineGrainedAuthorization]]
- [[AgentIdentity]]
- [[CrossAppAccess]]
- [[IDJAG]]
- [[SingleSignOn]]
- [[WorkOS]]
- [[summary-20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0]]
- [[summary-20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS]]
