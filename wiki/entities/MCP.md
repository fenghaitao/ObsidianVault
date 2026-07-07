---
title: "MCP"
type: entity
tags: [protocol, claude-code, integration, model-context-protocol]
sources: [raw/01-articles/claude/2026-06-08 - Observability for developers building connectors.md]
last_updated: 2026-07-07
---

# MCP

MCP (Model Context Protocol) is a protocol that enables [[ClaudeCode]] to integrate with external systems and access tools, knowledge bases, and real-time information.

## Usage Context

At [[Anthropic]], [[ClaudeCode]] uses [[MCP]] alongside `CLAUDE.md` files to consolidate scattered technical documentation into accessible formats. This integration makes expertise available across teams and reduces research time by up to 80%.

## Connector Ecosystem

As of June 2026, over 300 third-party MCP connectors are in the Claude directory, used by millions of people daily. [[Anthropic]] launched a public beta [[ConnectorObservability|observability dashboard]] enabling connector developers to monitor performance (errors, latency) across all Claude product surfaces. The same launch enabled in-app connector directory submission directly within Claude's Organization Settings.

## Related

- [[ClaudeCode]] — Tool that uses MCP for documentation integration
- [[Anthropic]] — Company using MCP integration in internal workflows
- [[ModelContextProtocol]] — the full concept page covering the protocol standard
- [[ConnectorObservability]] — the observability dashboard for published connectors
- [[MCPConnector]] — the Anthropic API MCP connector feature
- [[summary-2026-06-08 - Observability for developers building connectors]] — source announcement
