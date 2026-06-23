---
title: "Mem0"
type: entity
tags: [tool, library, memory, agents, mcp]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20250414 - The ULTIMATE Guide to Building Your Own MCP Servers (Free Template).md"
last_updated: 2026-06-19
---

## Definition

Mem0 is a long-term-memory library for [[AIAgent]]s — a persistent memory layer that lets agents store and recall information across conversations. [[ColeMedin]] uses it as the practical example in his open-source MCP server template, demonstrating how to expose agent memory through [[ModelContextProtocol]].

## Key Information

### What it does

Provides a simple API surface for:
- **Add memory**: store a fact or observation about a user/context.
- **Get all memories**: retrieve all stored memories for a context.
- **Search memories**: query for relevant memories by semantic similarity.
- **Update / delete**: maintain the memory store over time.

Under the hood it uses an LLM to extract memorable facts from conversations and a vector database to store them. Cole's example uses [[Supabase]] as the underlying vector store.

### Role in Cole's MCP template

Mem0 is the *example* in Cole's MCP server template — not the focus. The point of his template is to show how to build production-quality MCP servers (lifespan management, dual transport, proper tool descriptions). Mem0 is just a useful-enough capability to demonstrate the mechanics.

That said, Cole highlights mem0 specifically as a case study in *why you'd build your own MCP server*:

- Mem0 has its own official MCP server.
- Cole considers it not built to best practices: only supports one transport, duplicates tool descriptions, and (more importantly) requires a paid Mem0 API key.
- His template is a free, properly-built alternative — same surface area, no paywall.

### Three tools Cole exposes

The template registers three `@mcp.tool` functions:

1. `save_memory(text)` — store a new memory
2. `get_all_memories()` — retrieve all memories for the user
3. `search_memories(query)` — semantic search over stored memories

The LLM (e.g. Claude in Claude Desktop) decides which to call based on each tool's docstring.

### Why memory matters for agents

Without persistent memory, every conversation starts fresh — the LLM only knows what's in the current context window. Mem0 (or any memory library) gives agents continuity: a user's preferences, ongoing goals, prior decisions, and contextual facts survive across sessions.

This is essentially the same problem the [[KarpathyLLMWiki]] pattern solves at the human-knowledge layer (compile information into a persistent artifact between sessions). Different scale, similar insight.

## Related

- [[ModelContextProtocol]] — protocol Mem0's MCP servers use
- [[ColeMedin]] — built the alternative MCP server
- [[Supabase]] — Cole's vector store backing the example
- [[summary-20250414 - The ULTIMATE Guide to Building Your Own MCP Servers (Free Template)]] — primary source
- [[AIAgent]] — what mem0 augments
