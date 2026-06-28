---
title: "ModelContextProtocol"
type: concept
tags: [mcp, protocol, tools, integration, claude-code]
sources: [raw/03-transcripts/Claude/Claude Code 101/08 - MCP in Claude Code.md, raw/01-articles/claude/2025-06-18 - Remote MCP support in Claude Code.md, raw/01-articles/claude/2025-05-22 - New capabilities for building agents on the Anthropic API.md]
last_updated: 2026-06-28
---

## Definition

Model Context Protocol (MCP) is an open standard that enables AI agents like Claude Code to connect to external tools and data sources. It allows Claude to automatically determine when to use connected services to better answer queries.

## Key Information

- **Server types:** HTTP (remote services, hosted by provider) and STDIO (local processes on the user's machine).
- **Remote MCP servers:** MCP now supports remote servers hosted across web and desktop apps, enabling seamless integration with cloud services and web-based tools.
- **Scoping:** local (current project only), user (all projects), project (`.mcp.json` in version control, shared with team).
- **Management:** use `claude mcp add` to add servers, `/mcp` command to view, enable, or disable within a session.
- **Context cost:** MCP tools add persistent tool definitions to the context window even when idle. Disable unused servers.
- **10% threshold:** if MCP tools exceed 10% of context, Claude auto-switches to tool search mode (on-demand discovery, less reliable).
- **Alternatives:** CLI equivalents (e.g., `gh`, `aws`) are more context-efficient. Skills load only a name/description into context and the full content on demand.
- Hundreds of connectors available at claude.com/connectors.

## Integrations

[[Integrations]] bring MCP to [[Claude.ai]] users through a curated set of pre-built remote MCP servers. As of May 2025, integrations include major platforms like Atlassian (Jira, Confluence), Zapier, Cloudflare, Intercom, Asana, Square, Sentry, PayPal, Linear, and Plaid. Users can connect any number of integrations to enhance Claude's capabilities with deep context about their work and enable automated actions across platforms.

## Anthropic API MCP Connector

The [[Anthropic]] API offers the [[MCPConnector|MCP connector]] (beta, May 2025), which automatically manages remote MCP server connections without requiring custom client code:
- Automatic connection management to remote MCP servers
- Tool discovery and agentic reasoning about tool selection
- Automatic error handling and authentication
- Available remote servers from [[Zapier]], [[Asana]], and hundreds of others
- Works with [[Claude4Opus]] and [[Claude4Sonnet]]

## Related

- [[Integrations]] — MCP integrations available on Claude.ai
- [[Research]] — uses MCP integrations for searching custom data sources
- [[ToolIntegration]] — Pattern of connecting Claude to external tools via MCP
- [[MCPConnector]] — Anthropic API feature for automatic MCP server management
- [[summary-08 - MCP in Claude Code]] — source summary on Claude Code MCP
- [[summary-2025-06-18 - Remote MCP support in Claude Code]] — remote MCP servers announcement
- [[summary-2025-07-14 - Discover tools that work with Claude]] — tool directory and connectors announcement
- [[summary-2025-05-22 - New capabilities for building agents on the Anthropic API]] — announcement of API MCP connector
- [[ClaudeCode]] — supports MCP for local and remote servers
- [[ContextWindow]] — the memory constraint MCP tools consume
- [[Sentry]] — error tracking platform with MCP integration
- [[Linear]] — project management platform with MCP integration
- [[Asana]] — work management platform with remote MCP server
- [[Zapier]] — workflow automation with remote MCP server
- [[Claude4Opus]] — supports API MCP connector
- [[Claude4Sonnet]] — supports API MCP connector
