---
title: "Claude Desktop"
type: entity
tags: [tool, mcp-client, anthropic, desktop]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect.md"]
last_updated: 2026-06-26
---

## Definition
Claude Desktop is Anthropic's desktop MCP client application, criticized by Jeremiah Lowin for non-compliant behavior that limits MCP server capabilities.

## Key Information
- One of the most popular MCP clients
- Hashes all tools received on first contact and stores them in a SQLite database, ignoring subsequent updates
- Does not respect MCP spec features like notifications for tool list changes
- Sends all structured (object) arguments as strings, forcing FastMCP to implement automatic string-to-object deserialization as a workaround
- Lowin states: "I'm not a fan of Claude Desktop from an MCP server perspective. I think it's a real missed opportunity because it is such a flagship product of the company that has introduced MCP."
- Contrasted with Claude Code, which Lowin describes as "great"
- The caching behavior means progressive disclosure and dynamic tool listing techniques fail in Claude Desktop

## Related
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — source
- [[Anthropic]] — company that produces Claude Desktop
- [[FastMCP]] — framework that works around Claude Desktop limitations
- [[MCP]] — protocol Claude Desktop partially implements
