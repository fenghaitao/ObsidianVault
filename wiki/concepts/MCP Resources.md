---
title: "MCP Resources"
type: concept
tags: [mcp, protocol, context, agents, documentation, context-priming]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260523 - Introducing WebMCP： Agents in the Browser — RL Nabors.md"]
last_updated: 2026-06-30
---

## Definition
MCP Resources are a feature of the Model Context Protocol designed to expose bulk data (documentation, transcripts, reference material) to AI agents in a structured way. Unlike MCP tools which are called on demand, resources are intended for pre-priming agent context with relevant information. The feature is currently under-implemented across major MCP clients.

## Key Information
- Resources are the ideal vehicle for exposing documentation, transcripts, and other bulk content to agents
- Designed for pre-priming: agent harnesses could decide when to load relevant resources (e.g., switching to React mode loads React documentation from React's MCP server)
- Unlike tools which are called on demand, resources allow harnesses to proactively load context
- RL Nabors's critique: the spec is loosely defined and loosely implemented — no major client UI exposes resources
- Agents resist using MCP tools to fetch markdown for context — it's an inefficient use of context and not how tools were intended
- Using tools to fetch documentation is wasteful: each call burns tokens for both the call and the response
- Call to action: harness builders should implement resources, even bare-bones implementations

## Related
- [[summary-20260523 - Introducing WebMCP： Agents in the Browser — RL Nabors]] — source transcript
- [[MCP]] — the Model Context Protocol
- [[MCP Tools]] — the complementary on-demand mechanism
- [[RL Nabors]] — speaker who advocated for resources implementation
- [[ContextEngineering]] — the practice resources support
- [[ContextPriming]] — the use case resources are designed for
- [[ProgressiveDisclosure]] — related pattern for managing agent context
