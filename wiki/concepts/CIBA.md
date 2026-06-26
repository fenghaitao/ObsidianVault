---
title: "CIBA"
type: concept
tags: [identity, authorization, oauth, protocol]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0.md"]
last_updated: 2026-06-26
---

# CIBA

## Definition

CIBA (Client Initiated Backchannel Authentication) is an IETF specification (OpenID Connect CIBA) that enables a client (such as an AI agent) to initiate an authentication and authorization flow that results in a push notification to the user on an out-of-band device, without requiring the user to be present at the client.

## Key Information

- **Full Name**: Client Initiated Backchannel Authentication
- **Standard**: IETF / OpenID Connect specification
- **AI Agent Use Case**: An autonomous agent running a long-running task reaches a risky operation, initiates a CIBA request, the user receives a push notification with transaction details, approves it, and the agent receives an access token with the exact details the user approved
- **Flow**:
  1. Agent calls SDK to initiate backchannel authorization with transaction details
  2. User receives push notification (via Guardian, email, or other channels)
  3. User reviews and approves the structured authorization request
  4. Approval returns to agent as an access token containing the approved details
- **Auth0 Implementation**: Part of the async authorization feature, built into the Auth0 SDK with a simple method call

## Related

- [[Auth0]]
- [[AsyncAuthorization]]
- [[RichAuthorizationRequests]]
- [[Guardian]]
- [[AgentIdentity]]
- [[summary-20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0]]
