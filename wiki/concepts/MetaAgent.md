---
title: "MetaAgent"
type: concept
tags: [concept, agents, meta, agent-builder, archon]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/03 - Coding Subagents - The Next Evolution of AI IDEs.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
last_updated: 2026-06-19
---

## Definition

A meta-agent is an [[AIAgent]] whose purpose is to design, generate, or orchestrate *other* AI agents. [[ColeMedin]] coined a synonym in this playlist — "**agenteer**" — and [[Archon]] is presented as the first widely-shared, open-source instance of the pattern.

## Key Information

### What makes an agent a "meta-agent"

The defining property: its tool surface is itself agent-construction. Specifically:
- It can write the code for new agents (system prompts, tool definitions, agent configurations).
- It optionally runs/tests the agents it created (Archon's planned v9+).
- It iteratively refines its outputs based on feedback (autonomous self-feedback loops).

A meta-agent is recursive — it could in principle build other meta-agents. (Cole alludes to this as "very meta" without diving in.)

### Specialization vs. generalist coding agents

The motivation for meta-agents like Archon over generalist [[AICodingAssistant]]s like [[Windsurf]] / [[Cursor]]:

| Property | Generalist AI coder | Meta-agent (Archon) |
|---|---|---|
| Knowledge of [[PydanticAI]] / [[LangGraph]] | Generic doc retrieval | Curated RAG over the specific docs |
| Output structure | Inconsistent run-to-run | Consistent (multi-step pipeline enforces structure) |
| Self-correction | One-shot or simple loop | Multi-stage with parallel refinement |
| Iteration support | Per-conversation chat | Stateful agent-construction sessions with thread IDs |

### Meta-agent as a sub-agent

The killer pattern from this playlist: wrap the meta-agent as an [[ModelContextProtocol]] server, then a generalist AI IDE can invoke it as a [[SubAgent]] when it needs framework-specific code generation. The IDE writes the files; the meta-agent writes the agent inside them. Cole calls this "the next evolution of AI IDEs."

### Roadmap of meta-agent capabilities (per Archon's plan)

1. **Pure code generation** — produce the agent code, hand off to a human or IDE.
2. **+ Self-feedback loops** — autonomously iterate on the produced code based on internal critique.
3. **+ Self-execution** — spin up an isolated environment (Docker, vector DB, web search), run the agent, observe errors, refine.
4. **+ Self-improvement** — successful agents and tools are added to the meta-agent's own example library, making future builds better.
5. **+ Marketplace** — meta-agent publishes its agents as reusable MCP servers; ecosystem effects compound.

This roadmap is currently aspirational; v9+ items are not yet implemented as of the playlist's recording.

### Why this matters strategically

If meta-agents like Archon mature, software development reorganizes around "describe the agent you want, run the meta-agent, get a working specialized agent." The bottleneck shifts from coding to specifying the right agent — Cole's stated bet for the future of software.

## Related

- [[AIAgent]] — base concept
- [[Archon]] — primary example
- [[SubAgent]] — pattern Archon plays for AI IDEs
- [[ModelContextProtocol]] — transport layer making this composable
- [[ColeMedin]] — author of the "agenteer" framing
- [[AICodingAssistant]] — the generalist counterpart
- [[summary-introducing-archon-ai-agent-builder]] — Archon intro that articulates the vision
- [[summary-coding-subagents-mcp-evolution]] — meta-agent-as-sub-agent thesis
