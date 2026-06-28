---
title: "Discover tools that work with Claude"
type: source
tags: [tool-integration, connectors, mcp, product-announcement]
sources: [raw/01-articles/claude/2025-07-14 - Discover tools that work with Claude.md]
last_updated: 2026-06-28
---

# Discover tools that work with Claude

**Source**: https://claude.com/blog/connectors-directory

**Author**: Anthropic

**Published**: 2025-07-14

## Overview

Anthropic announced a new directory of tools and connectors that integrate with Claude. The directory enables one-click connections between Claude and users' favorite applications and services, allowing Claude to access the context and data from tools users already use.

## Key Announcements

### Tool Directory Launch

Anthropic introduced a centralized directory of recommended tools that connect to Claude. Users can:
- Browse available integrations at `claude.ai/directory`
- Click "Connect" for cloud-based services (with one-click OAuth)
- Click "Install" for local desktop extensions
- Browse partner-built connectors at `anthropic.com/partners/mcp`

### New Partner Integrations

The announcement features new connectors built by Anthropic's partners:

**Remote Services:**
- [[Notion]] — Productivity and workspace management
- [[Canva]] — Design platform
- [[Stripe]] — Payment processing

**Local Desktop Applications:**
- [[Figma]] — Design and prototyping tool
- [[Socket]] — Development tool
- [[Prisma]] — ORM and database toolkit

## Impact & Benefits

### Enhanced Context Access

By connecting Claude to user tools, Claude transitions from a conversational assistant to an "informed AI collaborator" with access to:
- Project details
- Deadlines and timelines
- Existing work context
- Real data from the user's tools

This eliminates the repetitive cycle of users explaining their context in each conversation.

### Practical Use Case

Example workflow enabled by [[Linear]] integration:
- **Before**: Ask Claude to "write release notes for our latest features" → Claude provides a generic template
- **After**: Ask Claude to "write release notes for our latest sprint from Linear" → Claude retrieves actual Linear tickets, sprint data, and generates professional, publication-ready release notes

## Availability

- **Directory**: Available now to all Claude users on web and desktop
- **Local Extensions**: Available through Claude Desktop app
- **Remote Services**: Available to paid plan users only

## Technical Foundation

Tool integrations are built on the [[ModelContextProtocol]] (MCP), an open standard for connecting AI agents to external tools and data sources. Partners build MCP connectors that expose their services to Claude.

## Related

- [[ToolIntegration]] — The pattern of connecting Claude to external tools and services
- [[ModelContextProtocol]] — Technical foundation for tool connectors
- [[Claude]] — The AI assistant that connects to tools
- [[Anthropic]] — The company behind Claude and the tool directory initiative
