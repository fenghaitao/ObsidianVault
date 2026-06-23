---
title: "Arcade"
type: entity
tags: [tool, mcp, integrations, agent-authorization, platform]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260202 - Turn Claude Code into Your Full Engineering Team with Subagents.md"
last_updated: 2026-06-20
---

## Definition

Arcade is a platform that exposes third-party services (Linear, GitHub, Slack, and many more) to AI agents through a single **MCP gateway**, handling authentication via **agent authorization** (guided OAuth flows). [[ColeMedin]] uses it in his "full AI engineer" [[AgentHarness]] so the harness can reach Linear, GitHub, and Slack without standing up an individual [[ModelContextProtocol]] server per service.

## Key Information

- **MCP gateway**: create a named gateway, pick allowed tools across services, and get a single URL + API key to set as environment variables. Cole's gateway exposed **91 tools** across GitHub + Linear + Slack.
- **Agent authorization**: Arcade walks the agent through each service's OAuth flow. Consequence: you can **share a harness with teammates via the Arcade gateway** without sharing raw credentials (each user doesn't need their own Linear API key or Slack app, and you don't share yours).
- **Auth mode**: set authentication to **Arcade headers**; run a one-time `authorize arcade` script to complete the OAuth flows; thereafter the harness has standing access to the chosen Linear project, Slack channel, and GitHub repo.
- **Context efficiency**: relies on MCP **tool discovery** in Claude Code, so 91 tool definitions are *not* dumped into the agent's context upfront.
- **Pricing**: has a free tier.

## Related

- [[ModelContextProtocol]] — the protocol Arcade gateways speak
- [[AgentHarness]] — Cole's harness uses Arcade for service connectivity
- [[ClaudeAgentSDK]] — the harness defines the Arcade MCP gateway in code
- [[ColeMedin]] — uses it in the "full AI engineer" demo
- [[summary-20260202 - Turn Claude Code into Your Full Engineering Team with Subagents]] — primary source
