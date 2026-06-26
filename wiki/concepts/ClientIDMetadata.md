---
title: "Client ID Metadata"
type: concept
tags: [identity, oauth, mcp, protocol]
---

# Client ID Metadata

## Definition

Client ID Metadata (CIMD) is a newer OAuth specification that pre-defines client metadata upfront, allowing authorization servers to recognize clients without requiring per-session Dynamic Client Registration (DCR).

## Key Information

- **Supersedes DCR**: CIMD is positioned as the successor to Dynamic Client Registration, providing a better experience by defining clients upfront rather than registering them at runtime
- **Age**: Approximately 3 months old as of April 2026
- **Adoption**: Has limited ecosystem support compared to DCR, which is more widely implemented
- **MCP Relevance**: In MCP authentication flows, CIMD could simplify client registration by avoiding the need for DCR at each session, but broad support is still developing

## Related

- [[DynamicClientRegistration]]
- [[OAuth]]
- [[MCP]]
- [[CrossAppAccess]]
- [[summary-20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS]]
