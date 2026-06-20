---
title: "summary-10x-your-ai-agents-parallel-architecture"
type: source
tags: [source, transcript, archon, parallel-agents, langgraph, pydantic-ai]
sources: ["raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/02 - 10x Your AI Agents with this ONE Agent Architecture.md"]
last_updated: 2026-06-19
---

## Core Summary

A deep dive on the "[[ParallelAgentArchitecture]]" — a multi-agent pattern where specialized [[SubAgent]]s execute simultaneously on different sub-problems, then a synthesizer agent combines their outputs. The video walks through building a Travel Planner Assistant using [[PydanticAI]] + [[LangGraph]], with parallel flight, hotel, and activity sub-agents fed by a gatekeeper info-gathering agent and consumed by a final synthesizer. Heavy reference to Anthropic's "[[summary-building-effective-agents]]" article for the architectural taxonomy.

## Key Points

- The pattern from Anthropic's article: input → parallel specialists → aggregator. Cole's variant replaces the aggregator with another LLM (synthesizer) for richer combination.
- Why split: LLMs degrade with tool count and prompt length. Specialized parallel agents keep per-prompt context small and run truly concurrently (not sequentially-with-merge).
- LangGraph mechanics covered: graph state (the shared dict carrying conversation history, intermediate results), nodes (one Python function per agent invocation), edges (with conditional routing for the gatekeeper).
- A router function returning a *list* of nodes triggers parallel execution in LangGraph — the simplest concurrency primitive.
- "Human in the loop" via LangGraph's `interrupt()` — pause graph execution, wait for user input, resume.
- PydanticAI structured outputs (`result_type=ClassName`) used to make the gatekeeper agent's output machine-readable (with an `all_details_given: bool` field driving the conditional edge).
- Streaming structured outputs requires special handling — Cole shows the pattern using `run_stream()` + dict-based debounced JSON validation.
- Real production example: Archon itself uses the parallel agent architecture in v5+ to refine generated agent code (one agent per: prompt, tools, dependencies, agent definition).

## Related

- [[Archon]] — production example using this architecture
- [[ColeMedin]] — author
- [[PydanticAI]] — framework for the specialized agents
- [[LangGraph]] — workflow orchestrator
- [[ParallelAgentArchitecture]] — central concept
- [[SubAgent]] — building block
- [[StructuredOutputs]] — used for gatekeeper agent
- [[HumanInTheLoop]] — pattern via LangGraph interrupt
- [[Anthropic]] — source of the original architectural taxonomy
