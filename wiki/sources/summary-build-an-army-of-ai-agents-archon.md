---
title: "summary-build-an-army-of-ai-agents-archon"
type: source
tags: [source, transcript, archon, mcp, sub-agents, ai-agents]
sources: ["raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/01 - Build an ARMY of AI Agents on Autopilot with Archon, Here's How.md"]
last_updated: 2026-06-19
---

## Core Summary

Cole Medin demonstrates how he used [[Archon]] to build an "MCP AI Agent Army" — a primary [[PydanticAI]] agent dispatching to specialized [[SubAgent]]s, each owning one [[ModelContextProtocol]] server (Brave search, GitHub, Slack, Airtable, Filesystem, Firecrawl). The architecture solves the problem of LLMs being overwhelmed by too many tools: instead of one agent juggling 30+ tools, the primary agent picks among 6 sub-agents, each holding a focused 4–6 tool surface for one external service.

## Key Points

- "Specialized agents over fat agents" — splitting tool surface across sub-agents keeps individual prompts small and reduces hallucinations from tool-overload.
- Primary agent uses tool descriptions (docstrings) to decide which sub-agent to invoke; the sub-agent then picks among its own narrow tool set.
- Each sub-agent uses PydanticAI's MCP integration: a `mcp_servers` parameter on the agent connects it to one server's tool inventory.
- Demo: agent army handled compound requests like "search the web for top AI agent frameworks → add results to my Airtable base → send the link to Slack" — calling Brave, Airtable, and Slack sub-agents in sequence.
- Reusable as a personal-assistant template: drop in any MCP server config, define a sub-agent for it, register it as a tool on the primary agent.
- Archon itself produced the army's code in a few iterations (not one-shot, but far better than generalist AI IDEs would).
- Showcases Archon's v6 features: tool library, MCP examples, advisor agent that picks relevant examples for the primary coder.

## Related

- [[Archon]] — used to build the agent army
- [[ColeMedin]] — author
- [[PydanticAI]] — framework underlying every sub-agent
- [[ModelContextProtocol]] — protocol the sub-agents speak
- [[SubAgent]] — core architectural pattern
- [[AIAgent]] — base concept
- [[ToolUse]] — function-calling pattern that powers sub-agents
- [[summary-introducing-archon-ai-agent-builder]] — companion source
