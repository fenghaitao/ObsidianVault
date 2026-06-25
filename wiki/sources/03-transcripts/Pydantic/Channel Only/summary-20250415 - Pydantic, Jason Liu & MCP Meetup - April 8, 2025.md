---
title: "summary-20250415 - Pydantic, Jason Liu & MCP Meetup - April 8, 2025"
type: source
tags: [source, pydantic, meetup, mcp, rag, agents]
sources: ["raw/03-transcripts/Pydantic/Channel Only/20250415 - Pydantic, Jason Liu & MCP Meetup - April 8, 2025.md"]
last_updated: 2026-06-25
---

## Core Summary

Pydantic's April 2025 London meetup at Atomico HQ featuring four lightning talks: Jason Liu on systematically improving RAG applications through data clustering and segmentation, an OpenAI solutions engineer on the Agents SDK and multi-agent workflows, Samuel Colvin demoing PydanticAI with MCP browser control and Logfire observability, and Anthropic's David Soria on MCP. Jason Liu's talk is the centerpiece, arguing that most RAG improvement comes from inventory/capability fixes rather than AI model improvements.

## Key Points

- Jason Liu presents a framework for improving RAG: segment queries by user satisfaction and volume, then prioritize high-volume/low-satisfaction segments
- Most RAG failures are inventory problems (missing data) or capability problems (missing metadata/filters), not AI quality issues
- OpenAI's Agents SDK provides built-in web search, file search, and computer use tools with tracing UI and MCP integration
- Samuel Colvin demos PydanticAI agent using Microsoft's Playwright MCP server for browser control, with Logfire distributed tracing
- Pydantic Graph provides finite state machine functionality for multi-step agent workflows with type-safe node connections
- MCP sampling allows MCP servers to proxy LLM calls through the client, avoiding per-server API key provisioning

## Related

- [[PydanticAI]] — agent framework used throughout the demos
- [[ModelContextProtocol]] — protocol discussed in depth by David Soria
- [[Logfire]] — observability platform demonstrated with distributed tracing
- [[JasonLiu]] — speaker on systematic RAG improvement
- [[SamuelColvin]] — creator of Pydantic, demoing PydanticAI and Logfire
