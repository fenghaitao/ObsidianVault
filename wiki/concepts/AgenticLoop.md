---
title: "Agentic Loop"
type: concept
tags: [agents, llm, loop, temporal, openai, architecture]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal.md"]
last_updated: 2026-06-26
---

## Definition
The agentic loop is the core execution pattern where an LLM has agency — it decides the flow of the application by choosing which tools to call and when to stop. Each `runner.run()` call in the OpenAI Agents SDK corresponds to an independent agentic loop: the LLM is called, it may decide to invoke tools, the tool results are routed back to the LLM, and the cycle continues until the LLM decides it's done.

## Key Information
- **LLM agency**: The defining characteristic — the LLM, not the developer, decides the application flow
- **Distinction from GenAI apps**: A GenAI application becomes an agent when the LLM has agency over the flow
- **Standard pattern**: The agentic loop is fairly standardized across frameworks; what varies is what gets inserted into the loop (tools, guardrails, handoffs)
- **Loop structure**: Call LLM → LLM decides to invoke tools or finish → if tools, execute them → route results back to LLM → repeat
- **Runner.run()**: In the OpenAI Agents SDK, each `runner.run()` is its own independent agentic loop
- **Handoffs**: When using handoffs, there is still only one agentic loop — the context/persona changes but the loop continues
- **Temporal integration**: By wrapping the agentic loop in a Temporal Workflow and tool calls in Temporal Activities, the loop becomes durable — crash recovery, retries, and scaling are automatic
- **Generic implementation**: Using Temporal's dynamic activities, a single agentic loop workflow can work with any set of tools by looking up tool handlers by name at runtime

## Related
- [[AgentLoop]] — distinct concept: Claude Agent SDK's three-part loop (gather, act, verify)
- [[DurableAgenticLoop]] — the Temporal-durable version
- [[OpenAIAgentsSDK]] — the framework
- [[MicroAgents]] — multiple agentic loops orchestrated together
- [[AgentHandoffs]] — context switching within a single agentic loop
- [[DynamicActivity]] — enabling generic tool sets in the loop
- [[summary-20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal]] — source
