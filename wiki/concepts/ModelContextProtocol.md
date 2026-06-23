---
title: "ModelContextProtocol"
type: concept
tags: [mcp, protocol, tools, integration, claude-code]
sources: [raw/03-transcripts/Claude/Claude Code 101/08 - MCP in Claude Code.md]
last_updated: 2026-06-23
---

## Definition

Model Context Protocol (MCP) is an open standard that enables AI agents like Claude Code to connect to external tools and data sources. It allows Claude to automatically determine when to use connected services to better answer queries.

## Key Information

- **Server types:** HTTP (remote services, hosted by provider) and STDIO (local processes on the user's machine).
- **Scoping:** local (current project only), user (all projects), project (`.mcp.json` in version control, shared with team).
- **Management:** use `claude mcp add` to add servers, `/mcp` command to view, enable, or disable within a session.
- **Context cost:** MCP tools add persistent tool definitions to the context window even when idle. Disable unused servers.
- **10% threshold:** if MCP tools exceed 10% of context, Claude auto-switches to tool search mode (on-demand discovery, less reliable).
- **Alternatives:** CLI equivalents (e.g., `gh`, `aws`) are more context-efficient. Skills load only a name/description into context and the full content on demand.
- Hundreds of connectors available at claude.com/connectors.

## Related

- [[summary-08 - MCP in Claude Code]] — source summary
- [[ClaudeCode]] — the tool MCP extends
- [[ContextWindow]] — the memory constraint MCP tools consume
