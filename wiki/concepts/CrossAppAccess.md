---
title: "Cross-App Access"
type: concept
tags: [identity, mcp, authentication, sso]
---

# Cross-App Access

## Definition

Cross-App Access (XAA) is an authentication pattern where an identity provider acts as a trust broker between applications, enabling MCP clients to obtain credentials for MCP servers without manual consent screens. It is built on the ID JAG (Identity JWT Authorization Grant) specification.

## Key Information

- **Problem Solved**: Eliminates the repetitive OAuth consent screens that MCP users face when connecting to multiple MCP servers, and gives IT teams visibility and control over MCP access
- **How It Works**: Both the MCP client (e.g., Cursor) and MCP server (e.g., Figma) already trust the same identity provider (e.g., Okta) for SSO. XAA leverages this existing trust to issue ID JAG tokens that bridge the gap without user intervention
- **Flow**: (1) User logs into IDP via SSO. (2) Client requests ID JAG token from IDP for target audience. (3) Client exchanges ID JAG with resource authorization server for access token. (4) Standard MCP communication proceeds. Steps 2-3 are invisible
- **Security Benefits**: Access tokens are short-lived (~5 minutes). When SSO session is revoked, no new tokens can be obtained. This is more secure than long-lived OAuth refresh tokens that grant standing access
- **IT Control**: IT admins configure managed connection policies specifying which MCP clients can request access to which MCP servers
- **Current Support**: Okta supports XAA for OIDC-based connections. Microsoft Entra does not yet support it. SAML-based support is planned
- **Limitations**: Authorization scoping (limiting what an agent can do within a service) is not part of the spec today

## Related

- [[IDJAG]]
- [[SingleSignOn]]
- [[OAuth]]
- [[MCP]]
- [[Okta]]
- [[WorkOS]]
- [[ConsentScreens]]
- [[summary-20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS]]
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — source (XAA as part of MCP roadmap)
- [[DavidSoriaParra]] — announced XAA as an upcoming MCP feature
