---
title: "Async Authorization"
type: concept
tags: [identity, authorization, agents, security]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0.md"]
last_updated: 2026-06-26
---

# Async Authorization

## Definition

Async Authorization is a feature enabling AI agents to request user approval for risky operations through out-of-band channels (push notifications, email) without requiring the user to be actively interacting with the agent. It is built on the CIBA (Client Initiated Backchannel Authentication) protocol.

## Key Information

- **Purpose**: Prevent autonomous agents from performing risky operations (e.g., purchases, financial transactions) without human supervision
- **Mechanism**: Agent calls SDK to initiate backchannel authorization; user receives notification on a separate device; user approves; agent receives access token with approved details
- **Channels**: Push notifications (Guardian), email, with more channels planned
- **Prerequisite**: User must be enrolled in MFA for push notification delivery
- **Authorization Details**: Uses Rich Authorization Requests (RAR) to carry structured transaction details (symbol, quantity, price) in the authorization request
- **Token**: The resulting access token contains the exact details the user approved, enabling resource servers to verify consent
- **Developer Control**: Developers define which operations are "risky" and require async approval

## Related

- [[CIBA]]
- [[RichAuthorizationRequests]]
- [[Guardian]]
- [[Auth0]]
- [[AgentIdentity]]
- [[HumanInTheLoopWorkflows]]
- [[summary-20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0]]
