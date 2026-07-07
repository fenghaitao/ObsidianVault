---
title: "AgenticSurfaces"
type: concept
tags: [agent-architecture, api-design, platform-evolution, managed-agents]
sources: ["raw/01-articles/claude/2026-06-10 - The evolution of agentic surfaces building with Claude Managed Agents.md"]
last_updated: 2026-07-07
---

## Definition

Agentic surfaces are the interfaces and infrastructure layers through which developers build, deploy, and interact with AI agents. They represent the evolving boundary between application logic and agent infrastructure, progressing from simple API contracts to fully managed platforms that handle orchestration, execution, and observability.

## Key Information

### Evolution of Agentic Surfaces

The article traces a four-stage evolution of the surface developers build on:

1. **API (2023)**: Tokens in, tokens out. One request, one model turn. The developer builds all harness and infrastructure themselves. Suitable for single-turn tasks like summarization, classification, and text rewriting.

2. **Claude Code harness (2025)**: An internal harness powering Claude Code — the agentic loop, tool execution, subagents, context management. Developers saw the value but couldn't reuse it for their own agents.

3. **Claude Agent SDK (2025)**: Exposes the same harness machinery that runs Claude Code as a programmable SDK. Developers get a pre-tuned harness that evolves alongside Claude, with infrastructure primitives for filesystem access, session persistence, and OpenTelemetry observability. Eliminates the need to maintain a homegrown agent loop.

4. **Claude Managed Agents (2026)**: A fully managed platform where Anthropic runs the agent infrastructure. The brain (harness/orchestration) is decoupled from the hands (sandbox execution), connected by an append-only session event log. Developers define the task, tools, and guardrails; Anthropic handles hosting, scaling, credential management, session persistence, and observability.

### Why Surfaces Evolve

As models become more capable, the tasks people hand off stop fitting in single turns. They want agents that carry tasks through, look things up, act, observe changes, and decide next steps — operating in real systems like codebases, wikis, and ticketing systems. Each evolution of the agentic surface removes infrastructure overhead so teams can focus on what differentiates their agents: context management and domain expertise.

### The Harness Evolution Problem

When the harness doesn't evolve alongside model intelligence, agents break down. A fix added for one model generation (e.g., context resets for [[ContextAnxiety]] on [[Claude4.5Sonnet|Claude Sonnet 4.5]]) can become pure overhead on the next ([[Claude4.7Opus|Claude Opus 4.5]]). With a managed surface, the harness evolves alongside the model, and teams update their agent configuration without touching the architecture underneath.

## Related

- [[summary-2026-06-10 - The evolution of agentic surfaces building with Claude Managed Agents]] — source article
- [[ClaudeManagedAgents]] — the managed platform at the current frontier of this evolution
- [[ClaudeAgentSDK]] — the programmable harness stage
- [[ClaudeCode]] — the agentic coding tool whose harness informed later surfaces
- [[AgenticLoop]] — the core operational pattern these surfaces implement
- [[ContextAnxiety]] — a model behavior that motivated harness adaptation
- [[Sandboxing]] — execution isolation that Managed Agents decouples from orchestration
