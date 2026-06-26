---
title: "SAML"
type: concept
tags: [identity, authentication, protocol, enterprise]
---

# SAML

## Definition

SAML (Security Assertion Markup Language) is an XML-based standard for exchanging authentication and authorization data between an identity provider and a service provider. It is widely used for enterprise single sign-on.

## Key Information

- **SSO Protocol**: One of the two main SSO protocols alongside OIDC (OpenID Connect)
- **ID JAG Support**: The ID JAG spec supports SAML assertions as a credential type — a client can send a SAML assertion to the IDP to prove the user has an active session, then receive an ID JAG token
- **Okta Support**: Okta currently supports XAA/ID JAG for OIDC-based connections, with SAML-based support planned
- **Relevance to MCP**: SAML-based SSO connections are common in enterprises. Supporting SAML assertions in the ID JAG flow extends XAA to organizations using SAML rather than OIDC

## Related

- [[SingleSignOn]]
- [[IDJAG]]
- [[CrossAppAccess]]
- [[OAuth]]
- [[Okta]]
- [[summary-20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS]]
