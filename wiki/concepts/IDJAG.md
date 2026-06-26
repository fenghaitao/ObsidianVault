---
title: "ID JAG"
type: concept
tags: [identity, authentication, jwt, oauth, mcp]
---

# ID JAG

## Definition

ID JAG (Identity JWT Authorization Grant) is an IETF specification that defines a token-based mechanism for identity providers to issue cross-service authorization tokens. It is the underlying spec for Cross-App Access (XAA) in MCP authentication.

## Key Information

- **Full Name**: Identity JWT Authorization Grant
- **Purpose**: Enables an identity provider to issue a signed JWT token that an MCP client can present to an MCP server's authorization endpoint to obtain an access token, without requiring user interaction
- **Flow**: Client presents a refresh token or ID token to the IDP, requests an ID JAG token for a specific audience (the target MCP server). IDP validates the user has access to both applications, issues the ID JAG. Client exchanges it with the resource authorization server for a standard OAuth access token
- **Audience**: The ID JAG token is scoped to a specific audience URL (e.g., `mcp.figma.com`), which the IDP uses to verify the access request against configured policies
- **Token Types**: The spec supports sending a refresh token, ID token, or SAML assertion to the IDP to prove the user has an active session
- **Security**: Tokens are short-lived. Combined with short-lived access tokens (~5 minutes), this provides better security than long-lived OAuth refresh tokens
- **Adoption**: Supported by Okta for OIDC-based connections. SAML support planned. Microsoft Entra support in progress

## Related

- [[CrossAppAccess]]
- [[SingleSignOn]]
- [[JWT]]
- [[OAuth]]
- [[SAML]]
- [[MCP]]
- [[Okta]]
- [[summary-20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS]]
