---
title: "Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect.md"
author: "Jeremiah Lowin"
company: "Prefect Technologies"
date: 2026-01-12
ingested: 2026-06-26
tags: [mcp, agentic-product-design, best-practices, fastmcp]
---

# Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect

## Core Thesis
Jeremiah Lowin argues that MCP servers should be designed as agentic products -- user interfaces for AI agents -- not REST API wrappers. He provides five actionable best practices for building effective MCP servers: outcomes over operations, flatten arguments, treat instructions as context, respect the token budget, and curate ruthlessly.

## Key Points
- **Agentic Product Design**: MCP servers are interfaces for agents, not humans. Design them for agent strengths and weaknesses on three dimensions: discovery (expensive for agents, cheap for humans), iteration (slow for agents, fast for humans), and context (agents have limited token memory).
- **Outcomes Over Operations**: Don't expose atomic REST API operations as individual tools. Instead, compose multiple API calls into a single outcome-oriented tool (e.g., "track latest order by email" rather than separate getUser, getOrders, checkStatus tools).
- **Flatten Arguments**: Avoid complex nested arguments (dicts, Pydantic models). Use top-level primitives, literals, and enums. Name arguments for the agent, not for developers.
- **Instructions Are Context**: Document every tool thoroughly with docstrings and examples. Be careful with examples -- agents treat them as contracts and will replicate their implicit patterns (e.g., number of tags).
- **Errors Are Prompts**: Error messages become part of the agent's next prompt. Make them helpful and informative. Use errors as a form of progressive disclosure for complex APIs.
- **Respect the Token Budget**: Every tool's description consumes tokens on handshake. With 800 tools and a 200K token window, each tool gets only ~250 tokens. Be parsimonious with descriptions.
- **Curate Ruthlessly**: 50 tools per agent is where performance degradation begins. Start with many tools during development, then aggressively prune down to essentials. Kelly KFL's Fiverr server went from 188 tools to 5.
- **Don't Convert REST APIs**: The fastest way to violate all best practices. Use REST-to-MCP conversion for bootstrapping only, then replace with curated, outcome-oriented tools.
- **Readonly Hint**: MCP spec supports annotations marking tools as read-only, helping clients set permissions and avoid unnecessary confirmation prompts.
- **Elicitation**: MCP feature allowing tools to request more input mid-execution. Powerful for approvals and complex arguments, but limited client support.
- **Code Mode**: Emerging technique where LLMs write code that calls MCP tools in sequence, sidestepping some iteration problems but introducing sandboxing concerns.

## Entities
- [[JeremiahLowin]] — Founder and CEO of Prefect Technologies, creator of FastMCP
- [[PrefectTechnologies]] — Data automation and orchestration software company
- [[FastMCP]] — De facto standard Python framework for building MCP servers, ~1.5M downloads/day
- [[ApacheAirflow]] — Workflow orchestration platform; Lowin was a PMC member
- [[Marvin]] — Agent framework developed by Lowin
- [[Block]] — Company (formerly Square) with an influential MCP best practices playbook
- [[ClaudeDesktop]] — Anthropic's desktop MCP client, criticized for caching tool lists in SQLite
- [[KellyKFL]] — Engineer at Fiverr who curated an MCP server from 188 tools down to 5
- [[Fiverr]] — Freelance marketplace; case study for MCP server curation

## Concepts
- [[AgenticProductDesign]] — Designing interfaces optimized for AI agents rather than humans
- [[OutcomesOverOperations]] — Composing atomic API calls into outcome-oriented agent tools
- [[FlattenArguments]] — Using top-level primitives instead of complex nested arguments in MCP tools
- [[ErrorsAsPrompts]] — Treating error messages as context that becomes part of the agent's next prompt
- [[TokenBudget]] — The finite context window that constrains how much tool documentation agents can consume
- [[CurateRuthlessly]] — Aggressively pruning MCP tools to essential outcomes for agent performance
- [[AgentStory]] — A user story framed for a programmatic autonomous agent with limited context
- [[ReadonlyHint]] — MCP annotation marking tools as read-only for client permission handling
- [[Elicitation]] — MCP mechanism for tools to request additional input mid-execution
- [[CodeMode]] — Technique where LLMs write code calling MCP tools in sequence to reduce iteration
- [[ProgressiveDisclosure]] — Revealing tool information incrementally rather than all at handshake
- [[FiftyToolRule]] — Heuristic that agent performance degrades beyond ~50 tools per agent

## Related
- [[MCP]] — Model Context Protocol
- [[FastMCP]] — framework for building MCP servers
- [[Anthropic]] — company that introduced MCP
- [[summary-20251222 - Amp Code： Next Generation AI Coding – Beyang Liu, Amp Code]] — Amp Code's contrarian take on MCP
