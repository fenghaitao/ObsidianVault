---
title: "Rich Authorization Requests"
type: concept
tags: [identity, oauth, authorization, protocol]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0.md"]
last_updated: 2026-06-26
---

# Rich Authorization Requests

## Definition

Rich Authorization Requests (RAR) is an OAuth extension that allows authorization requests to carry structured, detailed information about what the user is consenting to, such as transaction details (symbol, quantity, price). These details are recorded in the resulting access token.

## Key Information

- **Standard**: OAuth extension specification (RFC 9396)
- **Purpose**: Provide users with detailed context about what they are approving, beyond simple scope strings
- **AI Agent Use Case**: When an agent wants to place a stock order, the RAR carries the symbol, quantity, and price so the user sees exactly what they're approving
- **Token Recording**: The approved details are embedded in the access token, enabling resource servers to verify that the specific operation was consented to
- **Rendering Challenge**: RAR objects are open-ended (any structure), which complicates rendering. Auth0 solves this with a known schema that Guardian and custom apps can dynamically render
- **Schema Support**: Auth0 provides a flexible schema for rendering any authorization request details dynamically

## Related

- [[CIBA]]
- [[AsyncAuthorization]]
- [[Auth0]]
- [[Guardian]]
- [[AgentIdentity]]
- [[summary-20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0]]
