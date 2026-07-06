---
title: "Notion"
type: entity
tags: [company, productivity, agent-orchestration, managed-agents]
sources: [raw/03-transcripts/Claude/How teams use Claude/03 - How Notion built with Claude Managed Agents.md, raw/03-transcripts/Claude/Product Launches/14 - How Notion built with Claude Managed Agents.md, raw/01-articles/claude/2025-08-14 - Prompt caching with Claude.md]
last_updated: 2026-06-23
---

## Definition

Notion is a productivity and collaboration platform that uses Claude Managed Agents to power agent orchestration within its workspace. Notion's vision is to be the agent orchestration platform where humans and AI agents collaborate on complex workflows, with Notion providing context (databases, task boards) and Claude providing execution.

## Key Information

- **Agent orchestration:** Users drag tasks to start, multiple agent threads kick off, Claude Managed Agents sessions run in cloud, results appear in Notion.
- **Managed Agents integration:** Plug-and-play API integration — "If you were to roll it up yourself, it's like a mega brain engineering effort."
- **Long-running tasks:** Harness runs for 20 minutes to hours with memory management and quality outputs.
- **Dual view:** Notion UI for end users; Claude platform console for developers to see traces and improve agents.
- **Skill-from-connector distribution (April 2026)**: Notion is cited as one of the providers (with Canva and Sentry) that publishes a companion skill alongside its MCP server in Claude's connector directory. See [[ModelContextProtocol]].

## Prompt Caching Integration

Notion was one of the early adopters of [[PromptCaching]] on the Anthropic API. Notion AI integrates prompt caching into its Claude-powered features to reduce operational costs and improve response latency for end users. Simon Last (Co-founder, Notion): "We're excited to use prompt caching to make Notion AI faster and cheaper, all while maintaining state-of-the-art quality."

## Related

- [[ClaudeManagedAgents]] — the platform powering orchestration
- [[ToolIntegration]] — Pattern of connecting Claude to external tools like Notion
- [[summary-03 - How Notion built with Claude Managed Agents]] — source talk
- [[summary-2025-07-14 - Discover tools that work with Claude]] — Notion included in tool directory
- [[Anthropic]] — model provider
- [[PromptCaching]] — API feature used to optimize Notion AI cost and latency
- [[summary-2025-08-14 - Prompt caching with Claude]] — launch article featuring Notion as early adopter
- [[summary-2026-04-08 - Claude Managed Agents get to production 10x faster]] — reaffirms Notion as a Managed Agents customer
- [[summary-2026-04-22 - Building agents that reach production systems with MCP]] — skill-from-connector distribution example
