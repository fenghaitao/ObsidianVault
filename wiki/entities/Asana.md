---
title: "Asana"
type: entity
tags: [company, work-management, ai-teammates, managed-agents, enterprise]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - San Francisco/12 - Building with Claude Managed Agents and Asana AI teammates.md, raw/01-articles/claude/2025-05-22 - New capabilities for building agents on the Anthropic API.md, raw/01-articles/claude/2026-06-18 - Centrally manage authorization for MCP connectors.md]
last_updated: 2026-07-07
---

## Definition

Asana is a work management platform that integrates with [[Anthropic]] to power AI-driven task management and automation. It offers both [[ClaudeManagedAgents|AI teammates]] powered by Claude and a remote [[ModelContextProtocol|MCP server]] for API-based agent integration. Asana provides the enterprise context layer (17-year work graph), security, and human interface, while Claude handles multi-step action execution.

## Key Information

- **21+ pre-built AI teammates:** Available across PMO, marketing, IT, HR, and R&D — generally available as of March 2026.
- **Multiplayer agents:** Agents are real actors with sharing controls, working with multiple humans, receiving nudges, and retaining memory.
- **Enterprise memory:** Historical decisions, approvals, and interactions tracked and provided to agents with security and auditability.
- **Work graph:** 17 years of structured context (mission → goals → portfolios → projects → tasks with approvals).
- **Remote MCP server:** Asana offers a remote [[ModelContextProtocol|MCP server]] that Claude agents can access through the [[Anthropic]] API [[MCPConnector|MCP connector]], enabling API-based agents to reference tasks, assign work, and integrate with Asana workflows.
- **Enterprise-Managed Authorization:** Asana was among the MCP providers supporting [[EnterpriseManagedAuthorization|EMA]] at its June 2026 launch, enabling admins to provision the Asana connector centrally through [[Okta]] groups and roles.

## Related

- [[ClaudeManagedAgents]] — the platform powering AI teammates
- [[MCPConnector]] — Anthropic API feature for connecting to Asana MCP server
- [[ModelContextProtocol]] — protocol Asana implements
- [[Anthropic]] — model provider and API partner
- [[Claude4Opus]] — model accessing Asana via MCP connector
- [[Claude4Sonnet]] — model accessing Asana via MCP connector
- [[summary-12 - Building with Claude Managed Agents and Asana AI teammates]] — source talk on AI teammates
- [[summary-2025-05-22 - New capabilities for building agents on the Anthropic API]] — announcement of Asana MCP server
- [[AgenticMemory]] — memory from user feedback
- [[summary-2026-04-08 - Claude Managed Agents get to production 10x faster]] — reaffirms Asana as a Managed Agents customer
