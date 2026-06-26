---
title: "ContextEngineering"
type: concept
tags: [ai, context, prompt-engineering, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary.md"]
last_updated: 2026-06-26
---

## Definition
Context engineering is the deliberate art and science of curating what goes into an AI agent's context window. Coined by Andrej Karpathy, it involves filling the context window with just what the agent needs for the current step — no more, no less — because context is expensive, excess context degrades quality, and bad context can poison outputs.

## Key Information
- Andrej Karpathy: "Context engineering is a delicate art and science of filling the context window with just what needs to happen for the agent to have the right context for the right iteration for the next step."
- Context is expensive: every token added to context is sent as input tokens on every subsequent interaction, accumulating cost rapidly
- More context doesn't always mean better results — quality degrades past ~50% context window fullness (the "dumb zone")
- MCP servers add hidden context overhead: each enabled MCP server loads tool descriptions into the system prompt on every interaction
- Bad context can poison everything: mixing unrelated tasks, outdated comments, or negative patterns from earlier in a session can corrupt outputs
- Four key habits: (1) persist information outside the context window (scratch pads, memory files, agents.md), (2) be selective about what to pull in, (3) summarize/trim/compress as the window grows, (4) isolate context across sessions using parallel agents or fresh sessions
- When things go off the rails: start a new session, have the agent summarize the session for a new agent, verify the summary matches your understanding, then proceed with clean context
- "AI is really great at writing prompts for AI" — use agents to compress and summarize context for new sessions

## Related
- [[summary-20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary]] — source transcript
- [[AndrejKarpathy]] — coined the term
- [[AgenticEngineering]] — the parent paradigm
- [[Context Management]] — related techniques for maintaining coherence
- [[MCP]] — protocol whose servers add context overhead
- [[Parallel Agents]] — context isolation strategy
- [[AgentsDotMd]] — file-based context persistence
- [[ContextRot]] — degradation of context quality over time
