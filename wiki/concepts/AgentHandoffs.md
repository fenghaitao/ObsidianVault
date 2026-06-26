---
title: "Agent Handoffs"
type: concept
tags: [agents, openai, orchestration, context-management, handoff]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal.md"]
last_updated: 2026-06-26
---

## Definition
Agent Handoffs are a feature of the OpenAI Agents SDK where one agent transfers control to another agent within the same agentic loop. Unlike starting a new agentic loop, a handoff effectively changes the context/persona of the existing loop — the LLM takes on a different set of instructions and tools without restarting the execution cycle.

## Key Information
- **Single agentic loop**: Handoffs do not create a new agentic loop; they switch the context within the existing loop
- **Context switching**: The agentic loop takes on a different "persona" — different instructions, different tools, different behavior
- **Definition**: Agents define handoffs to other agents in their configuration, alongside name, instructions, and tools
- **Use case**: A triage agent decides which specialized agent should handle a query (e.g., weather vs. local business info) and hands off accordingly
- **Contrast with "just code" orchestration**: In "just code" mode, each `runner.run()` is its own independent agentic loop; handoffs keep everything within one loop
- **Temporal compatibility**: Handoffs work with Temporal's durability layer — the integration supports both orchestration modes
- **LLM agency**: The LLM decides when to hand off, based on the user's query and the agent's instructions

## Related
- [[OpenAIAgentsSDK]] — the framework
- [[MicroAgents]] — the paradigm handoffs enable
- [[AgenticLoop]] — the loop within which handoffs occur
- [[Handoff]] — distinct concept: Amp Code's context management technique (different meaning)
- [[summary-20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal]] — source
