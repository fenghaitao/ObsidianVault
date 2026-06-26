---
title: "Agent Identity"
type: concept
tags: [identity, agents, authorization, security]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gateways are All You Need — Karan Sampath, Anthropic.md"]
last_updated: 2026-06-26
---

# Agent Identity

## Definition

Agent Identity is Auth0's four-pillar framework for managing AI agent identity, authentication, and authorization. The pillars are: (1) AI needs to know who the user is, (2) AI needs to call APIs on the user's behalf, (3) AI can request user confirmation for risky operations, and (4) AI access should be fine-grained.

## Key Information

- **Four Pillars**:
  1. **User Identity**: AI must know who the user is to apply security, restrictions, and authorization
  2. **Delegated API Access**: Agents need to call APIs on behalf of users via token exchange (Token Vault)
  3. **User Confirmation**: Agents can request approval for risky operations via async CIBA-based flows
  4. **Fine-Grained Access**: Users control exactly which resources agents can access
- **Agent Modalities Supported**:
  - Interactive agents (chat boxes, code editors)
  - Dash runners / autonomous agents
  - Fully autonomous agents (acting on behalf of users or talking to other agents)
- **Three-Way Trust**: Establishes relationships between user, agent, and upstream service
- **Agent as Client**: Auth0 models agents as OAuth clients, with MCP servers also modeled as clients
- **Authorizing Party**: Access tokens include an `azp` (authorizing party) claim identifying the agent, distinct from the user subject

## Related

- [[Auth0]]
- [[Okta]]
- [[TokenVault]]
- [[CIBA]]
- [[AsyncAuthorization]]
- [[FineGrainedAuthorization]]
- [[ScopeBasedAccessControl]]
- [[summary-20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0]]
- [[DelegatedAgentIdentity]] — novel identity definitions for AI agents scoped through MCP Gateways
- [[summary-20260427 - Gateways are All You Need — Karan Sampath, Anthropic]] — source (delegated agent identity through gateways)
