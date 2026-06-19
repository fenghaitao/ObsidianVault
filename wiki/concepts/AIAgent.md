---
title: "AIAgent"
type: concept
tags: [concept, ai, agents, llm, tool-use]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/01 - Build an ARMY of AI Agents on Autopilot with Archon, Here's How.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/02 - 10x Your AI Agents with this ONE Agent Architecture.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/03 - Coding Subagents - The Next Evolution of AI IDEs.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
last_updated: 2026-06-19
---

## Definition

An AI agent is a large language model that has been given the ability to interact with the outside world — typically through [[ToolUse]] (function calling), often with a system prompt defining its role and behavior, and frequently composed with other agents into [[AgenticWorkflow]]s.

[[ColeMedin]]'s working definition (from the AI Agents Masterclass introduction):
> "All an agent is, is some large language model that is given the ability to interact with the outside world — able to draft emails, create tasks, add contacts to your CRM, whatever it might be."

## Key Information

### Minimum components of an agent

Across [[PydanticAI]] and the Anthropic-style taxonomy, an agent is the combination of:

1. **An LLM** (model selection determines reasoning capability and cost).
2. **A system prompt** defining role, goals, and behavioral constraints.
3. **Tools** — functions the agent can call, each with a description (when to use it) and parameter schema (what to pass).
4. **Optional dependencies** — runtime context (API keys, DB connections, user preferences) injected into tool calls.
5. **Optional structured output schema** — a Pydantic model the agent must conform to.

### Spectrum of agent complexity

| Complexity | Example |
|---|---|
| **Single agent, no tools** | Just an LLM with a system prompt. Useful as a synthesizer. |
| **Single agent, simple tools** | The Travel Planner's flight agent — one LLM, one tool that hits a flight API. |
| **Specialized agent** | An agent dedicated to one domain (e.g., the Brave Search [[SubAgent]] in the MCP Agent Army). |
| **Orchestrator agent** | A primary agent that dispatches to specialized sub-agents based on the request. |
| **Parallel agent system** | Multiple specialists running simultaneously, results combined. See [[ParallelAgentArchitecture]]. |
| **Meta-agent** | An agent whose purpose is to *build* other agents. See [[MetaAgent]] / [[Archon]]. |

### Why specialization matters

A recurring theme: an agent's quality degrades sharply as you give it more tools or more instructions. LLMs "get overwhelmed" — the longer the system prompt and tool list, the more hallucination. The fix throughout the playlist is to split work across specialized agents (the [[SubAgent]] pattern), each with a narrow focus.

### Cole's overarching thesis

> "AI agents will dominate the landscape of software going forward. And if you can create specialized agents on demand that tackle all of your problems, well then you, my friend, own the world."

Specialized, composable, framework-grounded agents (rather than ever-larger generalist prompts) are the trajectory.

## Related

- [[SubAgent]] — specialized agent pattern
- [[MetaAgent]] — agent that builds agents
- [[AgenticWorkflow]] — multi-agent orchestration
- [[ParallelAgentArchitecture]] — concurrent multi-agent execution
- [[ToolUse]] — what gives agents external capability
- [[StructuredOutputs]] — making agent output machine-readable
- [[PydanticAI]] — framework for defining agents
- [[LangGraph]] — framework for orchestrating agents
- [[Archon]] — meta-agent that generates other agents
- [[ColeMedin]] — author of the working definition above
