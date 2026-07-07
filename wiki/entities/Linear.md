---
title: "Linear"
type: entity
tags: [project-management, issue-tracking, development-tool, mcp-server, engineering]
sources: [raw/01-articles/claude/2025-06-18 - Remote MCP support in Claude Code.md, raw/01-articles/claude/2026-06-18 - Centrally manage authorization for MCP connectors.md]
last_updated: 2026-07-07
---

# Linear

Linear is a modern project management and issue tracking platform designed for software development teams.

## Key Information

- **Project management platform** for organizing issues, sprints, and project workflows
- **Head of Engineering**: Tom Moor leads engineering at Linear
- **Development integration**: Linear provides an MCP (Model Context Protocol) server that integrates with Claude Code

## Integration with Claude Code

The Linear MCP server enables:
- Access to Linear projects and issues with structured, real-time context within Claude Code
- Pull issue details and project status directly into Claude Code for contextual development
- Engineers stay in flow when moving between planning, writing code, and managing issues
- Eliminate copy-paste workflows and tab switching between tools

As Tom Moor noted: "With structured, real-time context from Linear, Claude Code can pull in issue details and project status—engineers can now stay in flow when moving between planning, writing code, and managing issues. Fewer tabs, less copy-paste. Better software, faster."

Linear was among the MCP providers supporting [[EnterpriseManagedAuthorization|Enterprise-Managed Authorization (EMA)]] at its June 2026 launch, enabling admins to provision the Linear connector centrally through identity provider groups and roles.

## Related

- [[ModelContextProtocol]] — the protocol enabling Linear's Claude Code integration
- [[ClaudeCode]] — the development tool that integrates with Linear
- [[summary-2025-06-18 - Remote MCP support in Claude Code]] — announcement of remote MCP support including Linear integration
- [[EnterpriseManagedAuthorization]] — enterprise auth mechanism Linear's MCP connector supports
- [[summary-2026-06-18 - Centrally manage authorization for MCP connectors]] — EMA launch announcement
