---
title: "Context Management"
type: concept
tags: [agents, context, architecture, llm, tools]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora.md"]
last_updated: 2026-06-26
---

## Definition
Context management is the third pillar of Replit's autonomy framework, referring to techniques for maintaining an agent's global coherence and alignment with user intent while efficiently managing the context window. It enables long-horizon autonomous tasks without requiring models with massive context windows.

## Key Information
- Most tasks, even ambitious ones, can be accomplished within 200,000 tokens when context is managed correctly.
- Techniques include: using the codebase itself to maintain state (writing documentation as the agent codes), persisting plans and task lists on the file system, and dumping memories to the file system for later retrieval.
- Anthropic evangelized the approach of dumping memories to the file system and having the agent decide when to retrieve them.
- Sub-agent orchestration is the key ingredient: sub-agents start from a blank slate with only the necessary context, run to completion, and return results to the main loop.
- Replit improved memories-per-compression from ~35 to ~45-50 after implementing sub-agent orchestration.
- Sub-agents provide separation of concerns, analogous to software engineering principles.
- Manus AI implements unlimited context management with smart KV caching: when a conversation exceeds a model's context window, Manus handles it automatically with optimized caching for fast responses.
- Manus's context management was described in an article by their CTO on context management and KV caching optimization.
- **Tool curation for context**: Filtering out unnecessary third-party tools reduces context window load by removing irrelevant tool descriptions, giving the agent fewer choices and more room for other information. This is one of the five third-party tool optimization practices.
- **Brendan O'Leary's four habits**: (1) Persist information outside the context window (scratch pads, memory files, agents.md). (2) Be selective about what to pull in — only what's relevant for this step. (3) Summarize, trim, and compress as the window grows. (4) Isolate context across sessions using parallel agents or fresh sessions.
- **Context window degradation**: Quality degrades past ~50% context window fullness (the "dumb zone"). Bad context can poison everything — mixing unrelated tasks, outdated comments, or negative patterns from earlier sessions.
- **Session hygiene**: When things go off the rails, start a new session. Have the agent summarize the session for a new agent, verify the summary, then proceed with clean context. "AI is really great at writing prompts for AI."

## Related
- [[summary-20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit]] — source
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[summary-20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz]] — source (tool curation for context)
- [[Three Pillars of Autonomy]] — parent framework
- [[Sub-agent Orchestration]] — key technique
- [[Autonomous Coding Agents]] — application domain
- [[ManusAI]] — platform with unlimited context management
- [[Agent Memory]] — related concept for persistent user context
- [[ToolCuration]] — practice of reducing context window via tool filtering
- [[summary-20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary]] — source (context engineering habits)
- [[ContextEngineering]] — the deliberate art of curating context
- [[AgentsDotMd]] — file-based context persistence
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — source (context sharing between agents)
- [[Context Sharing Between Agents]] — strategies for sharing context across parallel agents
- [[summary-20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora]] — source (context rot as a failure mode of long-running agents)
- [[Context Rot]] — failure mode where context degrades after extended operation, signaled by compaction
- [[High-Bandwidth Artifacts]] — persistent interfaces that mitigate context rot by not depending on linear chat context
