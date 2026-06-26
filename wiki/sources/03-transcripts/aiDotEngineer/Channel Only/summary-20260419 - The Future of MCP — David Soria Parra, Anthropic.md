---
title: "The Future of MCP — David Soria Parra, Anthropic"
type: source
source_type: transcript
source_url: "https://www.youtube.com/watch?v=aiDotEngineer"
author: "David Soria Parra"
organization: "Anthropic"
date: 2026-04-19
raw_file: "raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - The Future of MCP — David Soria Parra, Anthropic.md"
tags: [mcp, anthropic, protocol, agents, connectivity, roadmap]
---

# The Future of MCP — David Soria Parra, Anthropic

## Core Thesis
MCP has grown from a local-only tool protocol to a 110M monthly download ecosystem faster than React. 2025 was about exploration; 2026 is about putting agents into production. The best agents will use a connectivity stack of skills, MCP, and CLI/computer use together. On the client side, progressive discovery and programmatic tool calling are essential patterns. On the server side, authors must design for agents (not wrap REST APIs) and use MCP's rich semantics. The MCP roadmap includes stateless transport, improved async tasks, server discovery, skills over MCP, and cross-app access.

## Key Points
- **MCP Applications**: Agents can ship their own UI interfaces over MCP — not through plugins, SDKs, or client-side rendering. The server serves an app that works across ChatGPT, VS Code Cursor, and other clients. Requires semantics on both sides to understand rendering and UI.
- **Ecosystem growth**: 110 million monthly downloads, faster than React's growth trajectory. Used by OpenAI's Agent SDK, Google's ADK, LangChain, and thousands of frameworks as a dependency — establishing one common standard.
- **Connectivity stack**: Three tools for agent connectivity in 2026: (1) Skills — domain knowledge in simple files, reusable; (2) MCP — rich semantics, UI, long-running tasks, resources, decoupling, platform independence, authorization, governance; (3) CLI/Computer Use — great for local agents with sandboxes, pre-training familiarity (git, GitHub). The right tool depends on the use case.
- **Progressive discovery**: Instead of loading all tools into context, use tool search to defer loading until the model needs them. Demonstrated massive reduction in tool context usage in Claude Code after implementation.
- **Programmatic tool calling (code mode)**: Give the model a REPL/execution environment (V8 isolate, Monty, Lua) to compose tool calls in code rather than sequential round-trips. Uses MCP structured output for type information. Cuts token usage and latency.
- **Design for agents, not REST**: Stop wrapping REST APIs one-to-one in MCP servers. Design for how a human would interact — that's a good start for agents. Use rich MCP semantics: applications, skills over MCP, tasks, elicitation.
- **MCP Roadmap**: (1) Stateless transport protocol (from Google) for easier hyperscaler scaling — coming June; (2) Improved async task primitive for agent-to-agent communication; (3) TypeScript SDK v2 and Python SDK v2 based on lessons learned; (4) Cross-app access — login once with company IdP, use all MCP servers without re-login; (5) Server discovery via well-known URLs — crawlers/agents auto-discover MCP servers on websites; (6) Skills over MCP — ship domain knowledge with servers, continuously update without plugin registries.
- **FastMCP acknowledgment**: David openly acknowledged FastMCP is "way better than Python SDK that we're shipping" and that he wrote the original Python SDK. Anthropic is bringing in better Python developers to rewrite it.
- **2026 vision**: General agents for knowledge workers (financial analysts, marketers) that connect to 5+ SaaS applications and shared drives. Connectivity is the most important thing for these agents.

## Entities
- [[DavidSoriaParra]] — Engineer at Anthropic, MCP protocol contributor, original Python SDK author
- [[Anthropic]] — AI research company, creator of MCP
- [[aiDotEngineer]] — AI engineering conference and YouTube channel
- [[FastMCP]] — community Python SDK for MCP, acknowledged as better than official SDK
- [[ClaudeCode]] — Anthropic's coding agent, used as example for progressive discovery benefits
- [[GoogleDeepMind]] — contributed stateless transport protocol proposal

## Concepts
- [[MCPApplications]] — serving UI interfaces over MCP
- [[ProgressiveDiscovery]] — deferring tool loading with tool search
- [[ProgrammaticToolCalling]] — composing tool calls in code instead of sequential round-trips
- [[ConnectivityStack]] — skills + MCP + CLI/computer use as the three connectivity tools
- [[SkillsOverMCP]] — shipping skills/domain knowledge with MCP servers
- [[StatelessTransportProtocol]] — Google's proposal for scalable MCP transport
- [[AgentToAgentCommunication]] — async task primitive for agent-to-agent communication
- [[ServerDiscovery]] — auto-discovering MCP servers via well-known URLs
- [[ToolSearch]] — pattern for deferring tool loading in progressive discovery
- [[Structured Outputs]] — MCP feature enabling type-safe programmatic tool composition
- [[MCP]] — the underlying protocol
- [[Skills]] — domain knowledge files, part of the connectivity stack
- [[CodeMode]] — related to programmatic tool calling
- [[CrossAppAccess]] — enterprise SSO for MCP
- [[General AI Agent]] — 2026 vision for knowledge worker agents
- [[Elicitation]] — MCP primitive for requesting additional input mid-execution

## Related
- [[summary-20260427 - Gateways are All You Need — Karan Sampath, Anthropic]] — MCP enterprise gateway
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — MCP best practices
- [[summary-20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS]] — cross-app access
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — Claude Agent SDK
