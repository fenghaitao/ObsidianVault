---
title: "How we solved Context Management in Agents — Sally-Ann Delucia"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - How we solved Context Management in Agents — Sally-Ann Delucia.md"
date: 2026-05-10
ingested: 2026-06-29
tags: [context-management, context-engineering, agents, sub-agents, memory, evals, truncation, arize]
---

## Core Thesis
Context management is a product and UX problem, not just an engineering one. The best context strategy lets agents remember what they need to and forget what they don't. Agents don't fail because of prompts — they fail because of context. Sally-Ann Delucia shares lessons from building Arize's AI agent Alex over the course of a year, focusing on escaping the context window through a combination of smart truncation with memory, long-session evals, and sub-agent delegation.

## Key Topics
- **Context Engineering over Prompt Engineering**: Andrej Karpathy's "context engineering" has become the dominant concern. The stack shifted from prompts to context. Strategic selection of what the model sees is what matters, not just fitting under token limits.
- **The Vicious Loop**: Alex (Arize's agent) would run on trace/span data → spans grow → hit context limit → fail → retry with more data → fail again. The system analyzing the data was constrained by the data itself.
- **Naive Truncation Failed**: Taking only the first 100 characters broke reasoning. Follow-ups looked like new conversations. The agent forgot everything.
- **Summarization Failed**: Using LLMs to summarize context was too inconsistent. No control over what was important. Unreliable.
- **Smart Truncation + Memory (the solution)**: Keep the head (first 100 chars) and tail (last 100 chars), truncate the middle, and store it in a memory store. The agent can retrieve from memory when needed. Deduplicate messages, keep latest tool call results, never reset the system prompt. This has worked for months without needing changes.
- **Long Session Evals**: Long conversations cause failures that appear late and go unnoticed until users report them. Solution: load 10 turns, test the 11th to measure context degradation. Makes these bugs testable.
- **Sub-agents for Heavy Work**: Not all context belongs in the same agent. Offload data-intensive operations (like searching over hundreds of spans) to sub-agents. Main conversation stays light (chat + light context only), delegates to sub-agents for heavy data. Game-changer for Arize.
- **What They're Still Figuring Out**:
  - Huge context still breaks things (large prompts/inputs hit provider limits)
  - Long-term memory is hard — people want to reference issues from previous chats, but Alex currently has no cross-session memory
  - Context selection is still heuristic (first 100, last 100 chars) — no principled context budget or clear quality metrics
  - Claude Code uses a similar truncation/compression strategy, confirming the approach
- **Three Pillars**: Context engineering matters. Memory matters. Evaluation matters.

## Entities
- [[SallyAnnDeLucia]] — speaker, Head of Product at Arize, core contributor to Alex
- [[Arize]] — AI observability platform, parent company of Alex
- [[AlexArizeAgent]] — Arize's internal AI agent, used to build Arize itself

## Concepts
- [[SmartTruncation]] — keeping head + tail, truncating middle with memory store retrieval
- [[LongSessionEvals]] — testing context quality at turn 11 after loading 10 turns
- [[SubAgents]] — offloading heavy data work to sub-agents to keep main context light
- [[ContextManagement]] — the broader discipline of managing agent context windows
- [[ContextEngineering]] — the paradigm shift from prompt engineering to context engineering
- [[AgentMemory]] — memory stores that agents can retrieve from, distinct from context
- [[ContextSelection]] — heuristics for deciding what stays in context
- [[LongTermMemory]] — cross-session memory for agents (still unsolved at Arize)

## Related
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — previous talk by same speaker
- [[summary-20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit]] — context management as a pillar of autonomy
- [[summary-20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is]] — memory vs context distinction
- [[summary-20260506 - The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory]] — sub-agent architecture
- [[summary-20260425 - MCP = Mega Context Problem - Matt Carey]] — context management as the core challenge
- [[summary-20260503 - Context Is the New Code — Patrick Debois, Tessl]] — context engineering as primary discipline
