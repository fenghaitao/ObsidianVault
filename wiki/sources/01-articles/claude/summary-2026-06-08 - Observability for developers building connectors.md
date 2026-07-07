---
title: "summary-2026-06-08 - Observability for developers building connectors"
type: source
tags: [source, claude-blog, connectors, mcp, observability]
sources: ["raw/01-articles/claude/2026-06-08 - Observability for developers building connectors.md"]
last_updated: 2026-07-07
---

## Core Summary

Anthropic launched a public beta observability dashboard that lets MCP connector developers monitor their connectors' performance across Claude product surfaces. Published connectors in the directory now have a dashboard showing error rates, latency, and other performance metrics. The launch also enables in-app connector directory submission, allowing developers to submit their MCP servers to the directory directly within Claude's Organization Settings, without needing a separate submission flow. Access requires Admin or Owner on a Team or Enterprise plan; Enterprise plans can also delegate access via custom roles with Directory management or Libraries permission.

## Key Points

- Observability dashboard for published connectors tracks performance metrics (errors, latency) across all Claude product surfaces, now in public beta.
- In-app connector directory submission is now available directly within Claude under Directory in Organization Settings.
- Access requires Admin or Owner access on a Team or Enterprise plan. Enterprise Owners can delegate via custom roles with Directory management or Libraries permission.
- Over 300 third-party connectors exist in the directory, used by millions of people daily, all built on the [[ModelContextProtocol|Model Context Protocol (MCP)]].
- The feature is found at Claude > Directory in Organization Settings.

## Related

- [[ConnectorObservability]] — the observability dashboard concept
- [[MCPConnector]] — the MCP connector concept for the Anthropic API
- [[ModelContextProtocol]] — the protocol standard underlying all connectors
- [[Anthropic]] — the company launching this feature
- [[ClaudeEnterprise]] — Enterprise plan required for custom role delegation
