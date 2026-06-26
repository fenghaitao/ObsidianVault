---
title: "Single Sign-On"
type: concept
tags: [identity, authentication, enterprise]
---

# Single Sign-On

## Definition

Single Sign-On (SSO) is an authentication scheme that allows a user to log in with a single set of credentials to multiple independent applications. It is widely used in enterprises through identity providers like Okta and Microsoft Entra.

## Key Information

- **Enterprise Standard**: Most companies use SSO through identity providers (Okta, Microsoft Entra) for all their applications
- **MCP Problem**: MCP's OAuth-based authentication breaks the SSO model — each MCP server requires its own consent screen and issues independent tokens, forcing users to re-authenticate repeatedly
- **XAA Solution**: Cross-App Access restores the SSO experience for MCP by having the identity provider act as a trust broker, issuing ID JAG tokens that eliminate per-server consent screens
- **Session Lifecycle**: SSO sessions can be configured to last a day, a week, or based on company policy. When revoked, XAA ensures MCP access also terminates (unlike traditional OAuth refresh tokens)

## Related

- [[CrossAppAccess]]
- [[IDJAG]]
- [[OAuth]]
- [[SAML]]
- [[Okta]]
- [[MicrosoftEntra]]
- [[MCP]]
- [[summary-20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS]]
