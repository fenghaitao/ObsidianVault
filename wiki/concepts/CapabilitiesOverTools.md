---
title: "CapabilitiesOverTools"
type: concept
tags: [concept, learning, principle, philosophy]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20250526 - How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap).md"
last_updated: 2026-06-19
---

## Definition

"Capabilities over Tools" is [[ColeMedin]]'s heuristic for learning in the AI agent space: focus on *what you can accomplish* (the durable skill) rather than mastering *specific frameworks* (which churn rapidly). Cole calls it the single most important tip in his learning roadmap.

## Key Information

### The principle

> *"Focus on what you're able to accomplish instead of getting into the nitty-gritty details of mastering specific tools. You don't want to get caught in the weeds spending hours and hours mastering very specific tools that might become irrelevant next month."* — Cole Medin

A "capability" is a transferable concept like:
- *"Give an agent tool access"*
- *"Implement RAG with metadata-aware chunking"*
- *"Build a multi-agent workflow with specialization"*
- *"Set up agent observability"*

A "tool" is a specific framework or product:
- [[PydanticAI]], [[LangGraph]], CrewAI, Agno
- [[Cursor]], [[Windsurf]], Cline
- [[N8N]], Flowise, Voiceflow
- Specific MCP servers

### Why it matters in AI

The AI agent space has been churning faster than any prior software ecosystem Cole has worked in. Frameworks people invested heavily in 6 months ago (LangChain agents, AutoGPT, BabyAGI…) have been displaced or quietly deprecated. By contrast, the *concepts* (function calling, RAG, multi-agent specialization, structured outputs, observability) have only deepened.

Investing in concepts pays off across framework migrations. Investing in framework-specific minutiae pays off until the next dominant framework, then resets.

### Practical applications across Cole's roadmap

In every phase of his "[[summary-20250526 - How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap)]]":
- **Phase 2 (no-code)**: prototype in N8N — but learn the *RAG pattern*, not the N8N nodes specifically.
- **Phase 4 (coded agents)**: pick a framework, but understand the *agent definition shape* (LLM + system prompt + tools + dependencies + structured outputs) that translates between PydanticAI/LangGraph/etc.
- **Phase 5 (architecture)**: the [[ParallelAgentArchitecture]] is a concept; how each framework expresses it is implementation detail.

### Connection to Anthropic's framing

Aligns with [[Anthropic]]'s "[[summary-building-effective-agents]]" article, which warns that frameworks are "a level of abstraction that can sometimes be dangerous." Anthropic recommends understanding the underlying building blocks before reaching for framework conveniences — same idea.

### Counterpoint / when to *go deep* on a tool

Cole still goes deep on his preferred tools ([[PydanticAI]], [[LangGraph]], [[Archon]], his [[Crawl4AIRAG]] MCP server). The principle isn't "stay shallow forever" — it's "make the *first* layer of investment portable, then go deep where you've committed long-term."

## Related

- [[ColeMedin]] — author of the heuristic
- [[AIAgent]] — the broader subject
- [[summary-20250526 - How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap)]] — primary source where the principle is articulated
- [[summary-building-effective-agents]] — Anthropic's overlapping warning
