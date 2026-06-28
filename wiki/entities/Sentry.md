---
title: "Sentry"
type: entity
tags: [error-tracking, devops, monitoring, development-tool, mcp-server]
sources: [raw/01-articles/claude/2025-06-18 - Remote MCP support in Claude Code.md]
last_updated: 2026-06-28
---

# Sentry

Sentry is an error tracking and monitoring platform that helps developers identify and debug issues in their applications.

## Key Information

- **Error tracking platform** for monitoring application errors and issues in real-time
- **Development integration**: Sentry provides an MCP (Model Context Protocol) server that integrates with Claude Code
- **MCP server integration**: Through the Sentry MCP server, developers can access errors and issues directly within Claude Code for debugging without leaving the terminal

## Integration with Claude Code

The Sentry MCP server enables:
- Direct access to errors and issues from Sentry within Claude Code
- Debugging with full context of reported issues without context switching
- Seamless error diagnosis as part of the development workflow

## Related

- [[ModelContextProtocol]] — the protocol enabling Sentry's Claude Code integration
- [[ClaudeCode]] — the development tool that integrates with Sentry
- [[summary-2025-06-18 - Remote MCP support in Claude Code]] — announcement of remote MCP support including Sentry integration
