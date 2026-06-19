---
title: "LangGraph"
type: entity
tags: [framework, python, agentic-workflow, orchestration, langchain]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/01 - Build an ARMY of AI Agents on Autopilot with Archon, Here's How.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/02 - 10x Your AI Agents with this ONE Agent Architecture.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/03 - Coding Subagents - The Next Evolution of AI IDEs.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
last_updated: 2026-06-19
---

## Definition

LangGraph is a Python framework for orchestrating multi-step [[AgenticWorkflow]]s as state-machine graphs. Built by the [[LangChain]] team but used as a standalone library, it pairs naturally with [[PydanticAI]]: LangGraph handles the "what runs in what order with what state," PydanticAI handles each individual agent invocation. [[ColeMedin]] uses it as the orchestration layer for [[Archon]] and most of his complex agent demos.

## Key Information

### Three-part LangGraph pattern

Cole's pedagogical breakdown of any LangGraph implementation:

1. **State** — a typed dict (or Pydantic model) carrying everything the workflow needs to remember: conversation history, intermediate agent outputs, user preferences, etc.
2. **Nodes** — Python functions, one per logical step. A node receives the state, does work (often invoking a PydanticAI agent), and returns the state updates.
3. **Graph definition** — instantiate `StateGraph(StateClass)`, register nodes, define edges (including conditional ones), set the entry point, and `compile()` to get a runnable graph.

### Key features used in the playlist

- **Parallel execution via list-returning routers** — a conditional edge function that returns a `list` of node names triggers all of them simultaneously. The simplest concurrency primitive in LangGraph; central to the [[ParallelAgentArchitecture]] demo.
- **`interrupt()`** — pauses graph execution mid-flow to wait for user input. Resumed via the `Command(resume=value)` directive on the next graph invocation. The mechanism behind [[HumanInTheLoop]] flows.
- **Custom writer/streaming** — a writer object can be passed into nodes (`stream_mode="custom"`) to stream tokens out to a frontend in real time as the agent generates. Critical for UI responsiveness when running long parallel pipelines.
- **Memory savers** — `MemorySaver` for in-process state persistence; SQLite or Postgres variants for production.
- **LangGraph Studio** — visual editor that reads the Python graph definition and renders nodes/edges, useful for debugging the structure.

### Use in Archon

Archon's entire agent-building flow is a LangGraph graph. As of v6, the graph contains:
- Reasoner node → Advisor node → Coder node → Human-review interrupt → loop back to Coder, with v5+ additionally branching the Coder into parallel sub-agents for prompt/tools/dependencies/agent-definition.

### Use in Travel Planner demo

The pedagogical example built across the playlist. Architecture: info-gatherer agent → conditional edge (gather more or proceed) → parallel flight/hotel/activity sub-agents → synthesizer agent. Shows every LangGraph feature in one ~250-line script.

## Related

- [[LangChain]] — parent project; LangGraph is built by the same team
- [[PydanticAI]] — typical pairing for individual agent calls
- [[Archon]] — uses LangGraph as its core workflow engine
- [[ColeMedin]] — frequent advocate
- [[ParallelAgentArchitecture]] — pattern enabled by LangGraph's list-returning routers
- [[HumanInTheLoop]] — pattern enabled by `interrupt()`
- [[AgenticWorkflow]] — what LangGraph orchestrates
- [[AIAgent]] — what individual nodes typically wrap
