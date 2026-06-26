---
title: "SubAgents"
type: concept
tags: [ai-agents, context-management, architecture]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - No More Slop – swyx.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - Amp Code： Next Generation AI Coding – Beyang Liu, Amp Code.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md"]
last_updated: 2026-06-25
---

## Definition
Sub-agents are specialized AI agents that handle bounded subtasks within a larger system. They are used as an architectural pattern to manage context windows, fight "context rot," and prevent quality degradation when a single agent handles too much information over time.

## Key Information
- One of the biggest themes observed at the AI Engineer Summit (swyx keynote)
- Used to fight "context rot" — the degradation of context in AI systems over extended interactions
- By delegating tasks to specialized sub-agents, the main agent maintains cleaner context and produces higher quality output
- Represents a structural approach to fighting slop in AI systems
- Amp Code uses isolated sub-agents to manage context windows in coding agents, preventing context exhaustion and doom loops
- Part of agent-oriented architecture: purpose-built agents rather than monolithic model selectors
- Claude Agent SDK has best-in-class sub-agent support with bash — agents can spin up parallel sub-agents that each have their own bash access
- Adam Wolfe solved complex race condition challenges for parallel sub-agents with bash
- Sub-agents are great for tasks where a lot of work needs to happen but only the final result matters to the main agent (e.g., search across multiple data sources)
- For verification: sub-agents can adversarially check the work of the main agent by starting a fresh context session, avoiding context pollution
- Example pattern: main agent dispatches read sub-agents to summarize different sheets/sources in parallel, then dispatches more sub-agents based on results

## Related
- [[summary-20251222 - No More Slop – swyx]] — source
- [[summary-20251222 - Amp Code： Next Generation AI Coding – Beyang Liu, Amp Code]] — source
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[ContextRot]] — the problem sub-agents solve
- [[ContextExhaustion]] — failure mode sub-agents prevent
- [[DoomLoop]] — failure mode sub-agents prevent
- [[Modularity]] — related architectural principle
- [[AgentOrientedArchitecture]] — broader design philosophy
- [[Slop]] — sub-agents help fight this
- [[ClaudeAgentSDK]] — framework with best-in-class sub-agent support
- [[BashTool]] — enables sub-agents to operate independently
