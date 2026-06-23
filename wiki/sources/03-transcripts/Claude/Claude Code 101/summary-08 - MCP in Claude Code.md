---
title: "summary-mcp-in-claude-code"
type: source
tags: [source, claude-code, mcp, tools, transcript]
sources: [raw/03-transcripts/Claude/Claude Code 101/08 - MCP in Claude Code.md]
last_updated: 2026-06-23
---

## Core Summary

Model Context Protocol (MCP) is an open standard that lets Claude Code connect to external tools and data sources (databases, productivity apps, public repositories). Claude automatically determines when to use MCP tools. Servers are added via `claude mcp add` and come in two types: HTTP (remote services) and STDIO (local processes). MCP servers can be scoped locally (project only), per-user (all projects), or project-wide via `.mcp.json` (shared via version control). Key caveat: MCP tools consume context window space even when idle, so disable unused servers.

## Key Points

- MCP gives Claude Code access to external context: Linear for project management, Context 7 for up-to-date docs, and hundreds of connectors at claude.com/connectors.
- Two server types: HTTP (hosted by provider, network connection) and STDIO (local processes on your machine).
- Three scopes: local (current project), user (all projects), project (`.mcp.json` in version control, shared with team).
- Manage servers with `/mcp` command: view connected servers, status, enable/disable.
- MCP tools add persistent tool definitions to the context window; disable unused servers to save context.
- If MCP tools exceed 10% of context, Claude Code auto-switches to tool search mode (on-demand discovery, may be less reliable).
- CLI equivalents (e.g., `gh` for GitHub, `aws` for AWS) are more context-efficient than MCP servers.
- Skills are an alternative: only a name and description load into context; the full skill loads on demand.

## Related

- [[ClaudeCode]] — the tool MCP extends
- [[ContextWindow]] — the memory constraint MCP tools consume
- [[summary-07 - Context Management in Claude Code]] — related context management strategies
