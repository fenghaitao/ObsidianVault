---
title: "JWT"
type: concept
tags: [identity, authentication, token, standard]
---

# JWT

## Definition

JWT (JSON Web Token) is a compact, URL-safe means of representing claims between two parties. It is the token format used for ID JAG tokens in the Cross-App Access flow for MCP.

## Key Information

- **ID JAG Usage**: ID JAG tokens are signed JWTs issued by the identity provider. The MCP server's authorization endpoint validates the JWT signature against the IDP's public keys
- **Claims**: JWTs contain claims about the user (subject), the audience (target MCP server), issuer (identity provider), and expiration time
- **Validation**: MCP servers verify ID JAG tokens the same way they would validate any JWT — checking the signature, issuer, audience, and expiration
- **Bearer Type**: The ID JAG spec introduces a new JWT bearer grant type that MCP servers must support to accept these tokens

## Related

- [[IDJAG]]
- [[CrossAppAccess]]
- [[OAuth]]
- [[SingleSignOn]]
- [[MCP]]
- [[summary-20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS]]
