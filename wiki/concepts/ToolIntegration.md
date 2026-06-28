---
title: "Tool Integration"
type: concept
tags: [tools, integration, connectors, mcp]
sources: [raw/01-articles/claude/2025-07-14 - Discover tools that work with Claude.md]
last_updated: 2026-06-28
---

# Tool Integration

Tool Integration is the pattern of connecting [[Claude]] to external applications and services, enabling Claude to access user work context, data, and tools directly. This transforms Claude from a conversational assistant into an informed AI collaborator that can work within the user's existing tool ecosystem.

## Motivation

Traditional AI interactions require users to manually explain their context each time they interact with the assistant. By connecting Claude to the user's actual tools and data sources, Claude can:
- Access real project information and context
- Provide more relevant and actionable responses
- Reduce repetitive context-setting overhead
- Enable direct workflow integration

## Implementation Patterns

Claude supports tool integration through two primary mechanisms:

### Remote Service Connectors
One-click authentication to cloud-based applications and services:
- [[Notion]] — Productivity and knowledge management platform
- [[Canva]] — Design platform
- [[Stripe]] — Payment processing
- [[Linear]] — Project management and issue tracking

### Local Desktop Extensions
Direct integration with local desktop applications through the Claude Desktop app:
- [[Figma]] — Design and prototyping tool
- [[Socket]] — Development tool
- [[Prisma]] — ORM and database toolkit

## Architecture

Tool integration is built on the [[ModelContextProtocol]] (MCP), an open standard for connecting AI agents to external tools and data sources. Partners build connectors that expose their services through the MCP interface.

## Availability & Access

- **Web and Desktop**: Tool directory is available to all Claude users
- **Remote Services**: Paid plan users only (professional and team plans)
- **Local Extensions**: Available through the Claude Desktop app

Users can explore available tools and connectors at:
- `claude.ai/directory` — Browse and connect available tools
- `anthropic.com/partners/mcp` — Partner-built connectors directory

## Benefits

1. **Context Preservation** — Claude retains access to user's tools throughout conversation
2. **Reduced Friction** — One-click connection eliminates repeated context entry
3. **Work Acceleration** — Claude can directly generate production-ready outputs (e.g., release notes, design specifications)
4. **Extensibility** — Open MCP standard allows partner ecosystem to grow

## Related

- [[ModelContextProtocol]] — Open standard underlying tool integration
- [[Claude]] — The AI assistant that connects to tools
- [[Linear]] — Project management tool integrated with Claude
- [[Notion]] — Productivity platform integrated with Claude
- [[Figma]] — Design tool integrated with Claude
