---
title: "Guardian"
type: entity
category: product
---

# Guardian

## Definition

Guardian is Okta's multi-factor authentication (MFA) application, used in the AI agent context as the push notification channel for async authorization flows where agents request user approval for risky operations.

## Key Information

- **Organization**: Okta / Auth0
- **Function**: MFA application that delivers push notifications to users
- **AI Agent Use Case**: Receives Rich Authorization Requests from agents via CIBA, displays structured transaction details (symbol, quantity, price), and captures user approval
- **SDK Support**: Guardian SDK available for custom implementations
- **Alternative Channels**: Email and additional channels planned for reaching users
- **Rendering**: Supports a dynamic schema for rendering structured authorization request details

## Related

- [[Okta]]
- [[Auth0]]
- [[CIBA]]
- [[AsyncAuthorization]]
- [[RichAuthorizationRequests]]
- [[summary-20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0]]
