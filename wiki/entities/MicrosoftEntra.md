---
title: "Microsoft Entra"
type: entity
category: product
---

# Microsoft Entra

## Definition

Microsoft Entra (formerly Azure Active Directory) is Microsoft's identity and access management platform. As of April 2026, it does not yet support Cross-App Access (XAA) for MCP authentication.

## Key Information

- **XAA Status**: Does not yet support XAA/ID JAG — WorkOS is working with Microsoft to add support
- **DCR Support**: Does not support Dynamic Client Registration (DCR), creating protocol fragmentation issues for MCP clients connecting to Entra
- **Scope Validation**: Has a resource parameter problem where the resource must match the scope, otherwise Entra rejects the request — different MCP clients handle this differently
- **SSO Role**: Used by enterprises for single sign-on to applications including MCP clients and servers
- **Future**: Expected to eventually support XAA as the spec gains broader adoption

## Related

- [[CrossAppAccess]]
- [[IDJAG]]
- [[DynamicClientRegistration]]
- [[Okta]]
- [[MCP]]
- [[summary-20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS]]
