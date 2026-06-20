---
title: "AgentObservability"
type: concept
tags: [concept, observability, monitoring, production, agents]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20250526 - How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260129 - Claude Skills Aren't Just for Claude - Here's How to Build Them for ANY Agent.md"
last_updated: 2026-06-20
---

## Definition

Agent observability is the production-side practice of capturing, indexing, and querying every piece of an [[AIAgent]]'s runtime behavior — input prompts, model calls, tool invocations and their arguments, intermediate reasoning, final outputs, latency, costs, errors. [[ColeMedin]] frames it as **100% necessary for production**.

## Key Information

### Why "100% necessary for production"

Without observability you cannot answer questions every production agent generates daily:
- *"Why did this user get a bad answer?"*
- *"How often does the agent call this tool incorrectly?"*
- *"Did the prompt change yesterday make things better or worse?"*
- *"Which model + prompt combination is cheapest while staying above quality threshold X?"*
- *"What patterns are the most common failure modes I should add to my [[AgentEvaluation]] set?"*

Without observability the answer is "I don't know" and your iteration loop stalls.

### What's typically captured

| Layer | Examples |
|---|---|
| **Inputs** | User prompts, conversation history, system prompts, retrieved context |
| **Model calls** | Provider, model ID, parameters (temperature, max_tokens), latency, token counts, cost |
| **Tool calls** | Tool name, arguments, result, success/failure, tool-call latency |
| **Reasoning traces** | Thinking blocks (where exposed), chain-of-thought |
| **Outputs** | Final agent response, structured fields, refusals |
| **Metadata** | User/session ID, agent version, deployment env, timestamps |

### Tools Cole recommends

| Tool | Origin | Notes |
|---|---|---|
| **Langfuse** | Independent OSS | Self-hostable; broad framework support; Cole's most-mentioned choice |
| **Helicone** | Independent | OpenAI-compatible proxy approach |
| **Langsmith** | LangChain | Strong if you're already in LangChain ecosystem |
| **Logfire** | Pydantic team | Built into PydanticAI; fits well with the [[PydanticAI]] + [[LangGraph]] stack. Cole's go-to in his Jan 2026 skills-agent demo: a few lines of config instrument every agent run, sending tool calls, LLM interactions, token usage, and cost as **traces** — inspectable locally and in production to see exactly where an agent went wrong (e.g. a bad tool parameter). |

The tools differ in integration model (proxy vs. SDK callbacks vs. native), self-hosting options, and pricing — but the underlying signal each captures is similar.

### Observability vs. [[AgentEvaluation]]

These are complementary, not duplicative:

- **Observability**: passive, continuous, captures *what actually happened* in production runs.
- **Evaluation**: active, periodic, measures *how well* the agent performs against a curated set of cases.

The feedback loop: observability finds real-world failure modes → those become eval cases → eval cases drive iteration → improved agent ships → observability watches it.

### Setup heuristic

Cole says it's "not that hard to set up" — most observability tools are a single SDK install + API key + a callback registration in your agent framework. The cost of setting it up is typically a single afternoon; the cost of not having it is debugging blind for the lifetime of the agent.

## Related

- [[AIAgent]] — what's being observed
- [[AgentEvaluation]] — companion practice
- [[PydanticAI]] — Logfire's native home
- [[ColeMedin]] — author of the framing here
- [[summary-how-to-learn-ai-agents-roadmap]] — primary source (phase 7)
- [[summary-build-skills-for-any-agent]] — Logfire tracing demo
