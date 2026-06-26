---
title: "OAuth"
type: concept
tags: [identity, authentication, authorization, protocol]
---

# OAuth

## Definition

OAuth is an open standard for access delegation, commonly used to grant applications limited access to user resources without exposing passwords. MCP uses OAuth as its underlying authentication layer.

## Key Information

- **MCP Usage**: MCP servers use OAuth for authentication, requiring users to go through consent screens for each server
- **Consent Screen Problem**: OAuth was designed around the assumption that systems don't trust each other, requiring explicit user consent. This creates friction in MCP where users connect to many servers
- **Token Types**: Issues access tokens (typically short-lived) and refresh tokens (long-lived) that grant standing access
- **MCP Limitation**: OAuth refresh tokens persist independently of SSO session revocation, creating security gaps when employees leave or machines are compromised
- **XAA Enhancement**: Cross-App Access layers on top of OAuth, using ID JAG tokens to automate the consent process while maintaining OAuth's access token mechanism for actual API calls

## Related

- [[CrossAppAccess]]
- [[IDJAG]]
- [[SingleSignOn]]
- [[JWT]]
- [[SAML]]
- [[MCP]]
- [[ConsentScreens]]
- [[DynamicClientRegistration]]
- [[summary-20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS]]
