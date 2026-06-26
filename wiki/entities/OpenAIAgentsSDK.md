---
title: "OpenAIAgentsSDK"
type: entity
tags: [tool, agent-framework, openai, python, typescript]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal.md"]
last_updated: 2026-06-26
---

## Definition
The OpenAI Agents SDK is an agent framework launched around May 2025, available in Python and TypeScript. It provides primitives for building agents with tools, handoffs, guardrails, and tracing. It integrates with Temporal for durability via a plugin that makes the Runner class abstract.

## Key Information
- **Launch**: Around May 2025
- **Languages**: Python and TypeScript
- **Core primitives**:
  - **Agents**: Defined with a name, instructions, model, tools, handoffs, and guardrails
  - **Runner.run()**: Each call corresponds to an independent agentic loop — the LLM decides the flow
  - **Tools**: Functions the agent can invoke; doc strings are used to generate JSON tool descriptions
  - **Handoffs**: Transfer control from one agent to another within the same agentic loop (context switching)
  - **Guardrails**: Input/output validation rules
  - **Tracing**: Built-in observability features integrated with Temporal's UI
- **Temporal integration**: OpenAI made the `Runner` class abstract to allow Temporal to provide a durable implementation. The integration provides `activity_as_tool()` to convert Temporal activities into agent tools, and a plugin configures LLM retry policies.
- **Two orchestration modes**:
  - **"Just code"**: Sequential, parallel, or loop-based orchestration of agents using standard programming constructs
  - **Handoffs**: Agent-to-agent transfer within a single agentic loop, effectively changing the context/persona
- **Tool generation**: The Agents SDK automatically generates JSON tool descriptions from function doc strings, unlike the raw OpenAI API which requires manual JSON blob construction

## Related
- [[OpenAI]] — parent company
- [[Temporal]] — integration partner for durability
- [[summary-20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal]] — source
- [[AgenticLoop]] — the core execution pattern
- [[AgentHandoffs]] — the handoff orchestration mode
- [[MicroAgents]] — the small, single-purpose agent paradigm
