---
title: "ConnectorObservability"
type: concept
tags: [mcp, connectors, observability, monitoring, claude, anthropic]
sources: ["raw/01-articles/claude/2026-06-08 - Observability for developers building connectors.md"]
last_updated: 2026-07-07
---

## Definition

Connector Observability is a public beta dashboard feature in Claude that lets MCP connector (server) developers monitor their published connectors' performance across all Claude product surfaces, tracking metrics such as error rates and latency.

## Key Information

- Launched in public beta by [[Anthropic]] on 2026-06-08.
- Available to published connectors in the [[Claude.ai]] connector directory.
- Provides a dashboard view of how connectors perform across all Claude product surfaces (web, desktop, mobile, API).
- Tracks key performance indicators including error rates and latency.
- Enables developers to diagnose issues with their connectors in production.

## Access Requirements

- Found in Claude under **Directory** in **Organization Settings**.
- Requires **Admin** or **Owner** access on a **Team** or **Enterprise** plan.
- On Enterprise plans, Owners can delegate access via [[ClaudeEnterprise|custom roles]] with the **Directory management** or **Libraries** permission.

## Relationship to Connector Submission

The same launch also enabled in-app connector directory submission: developers can now submit their [[ModelContextProtocol|MCP]] servers to the directory directly within Claude's Organization Settings, streamlining what was previously a separate submission process.

## Scale Context

As of launch, the connector directory hosts over 300 third-party connectors, used by millions of people daily, all built on the [[ModelContextProtocol|Model Context Protocol (MCP)]].

## Related

- [[summary-2026-06-08 - Observability for developers building connectors]] — source announcement article
- [[MCPConnector]] — the Anthropic API MCP connector feature
- [[ModelContextProtocol]] — the underlying protocol standard for all connectors
- [[Anthropic]] — the company that launched this feature
- [[ClaudeEnterprise]] — Enterprise plan with custom role delegation support
- [[ClaudeTeamPlan]] — Team plan with directory access
