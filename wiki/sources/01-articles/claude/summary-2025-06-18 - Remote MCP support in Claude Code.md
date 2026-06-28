---
title: "Remote MCP support in Claude Code"
type: source
tags: [mcp, claude-code, remote-servers, oauth, tool-integration, anthropic]
sources: [raw/01-articles/claude/2025-06-18 - Remote MCP support in Claude Code.md]
last_updated: 2026-06-28
---

# Remote MCP support in Claude Code

Anthropic announced support for remote MCP servers in Claude Code, enabling developers to securely connect their favorite development tools and data sources without managing local servers.

## Key Features

- **Remote server integration**: Developers can add vendor-provided remote MCP server URLs directly to Claude Code with no manual setup required. Vendors handle updates, scaling, and availability.
- **Lower maintenance**: Remote servers reduce infrastructure management burden compared to local server deployments.
- **Native OAuth support**: Claude Code features native OAuth authentication for remote MCP servers, ensuring secure connections to existing accounts. No API keys to manage or credentials to store.
- **Tool and resource access**: Claude Code can access both tools and resources exposed by MCP servers, enabling it to pull context from third-party services and take actions within them.

## Use Cases & Examples

### Sentry Integration
By integrating Claude Code with the Sentry MCP server, developers can:
- Access errors and issues directly from Sentry
- Debug with full context of reported issues without leaving the terminal

### Linear Integration  
Integration with the Linear MCP server allows:
- Access to Linear projects and issues with structured, real-time context
- Pull issue details and project status directly into Claude Code
- Stay in flow when moving between planning, coding, and issue management
- Eliminate copy-paste workflows and tab switching

As Tom Moor, Head of Engineering at Linear, noted: "With structured, real-time context from Linear, Claude Code can pull in issue details and project status—engineers can now stay in flow when moving between planning, writing code, and managing issues. Fewer tabs, less copy-paste. Better software, faster."

## Availability & Resources

- Remote MCP server support is available now in Claude Code
- Documentation: anthropic.com/docs/claude-code/mcp
- MCP directory with recommended servers: anthropic.com/partners/mcp

## Related

- [[ModelContextProtocol]] — the MCP standard enabling this functionality
- [[ClaudeCode]] — the IDE tool being extended with remote MCP support
- [[Sentry]] — error tracking platform with MCP server support
- [[Linear]] — project management tool with MCP server integration
