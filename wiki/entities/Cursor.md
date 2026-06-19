---
title: "Cursor"
type: entity
tags: [tool, ai-coding-assistant, ai-ide, mcp-client]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/03 - Coding Subagents - The Next Evolution of AI IDEs.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
last_updated: 2026-06-19
---

## Definition

Cursor is a popular AI-powered IDE (a fork of VS Code) and one of the dominant [[AICodingAssistant]]s. In [[ColeMedin]]'s Archon playlist, Cursor is treated as functionally equivalent to [[Windsurf]] — both are MCP-aware generalist AI coders that can be paired with [[Archon]] as a specialized PydanticAI/LangGraph [[SubAgent]].

## Key Information

### Role in the playlist

Cole consistently lists Cursor and Windsurf together as the two primary integration targets for Archon's MCP server. The setup steps are nearly identical:

1. Run Archon as an MCP server (FastAPI endpoint or local Python).
2. Add the MCP server config to Cursor's settings (the `setup_mcp.py` script emits the right JSON).
3. Cursor's underlying LLM (Claude or GPT) sees the Archon tools and invokes them when generating PydanticAI / LangGraph code.

### Differences vs Windsurf

Cole doesn't dwell on differences — both are described as generalist AI coders that "hallucinate awful code all of the time" on framework-specific work, motivating the same fix (specialized sub-agents over MCP).

The primary demo throughout the playlist is in Windsurf, but Cursor is mentioned in nearly every "and you can do the same with Cursor" sentence — the pattern is portable.

### Notable mentions

- "Cline" (also referred to in the auto-transcripts as "Klein") is mentioned as a third comparable AI IDE alongside Cursor and Windsurf, though demoed less.
- Cursor and Windsurf are both classed by Cole as "generalists" in his "[[AICodingAssistant]]" framing — the foil to Archon's "specialist."

## Related

- [[Windsurf]] — direct competitor; functionally equivalent in this playlist
- [[Archon]] — used as Cursor's specialized PydanticAI sub-agent
- [[ModelContextProtocol]] — integration mechanism
- [[AICodingAssistant]] — Cursor's category
- [[SubAgent]] — pattern enabled when Cursor calls Archon
- [[summary-coding-subagents-mcp-evolution]] — primary context
