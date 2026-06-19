---
title: "AgenticWorkflow"
type: concept
tags: [concept, agents, orchestration, workflow]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/02 - 10x Your AI Agents with this ONE Agent Architecture.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/03 - Coding Subagents - The Next Evolution of AI IDEs.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
last_updated: 2026-06-19
---

## Definition

An agentic workflow is a multi-step orchestration of one or more [[AIAgent]]s, with explicit control flow connecting them. Different agents (or different invocations of the same agent) handle different sub-problems, with state passed between them and conditional branching driving the path through the system.

## Key Information

### Why workflows over single agents

A single agent with a long system prompt and many tools is brittle. Splitting the work across an orchestrated workflow yields:

- **Smaller per-agent prompts** → fewer hallucinations.
- **Specialization** → each agent focused on one task it does well.
- **Parallelism** → independent steps run concurrently.
- **Auditability** → each step's input/output is visible in the workflow state.
- **Targeted iteration** → revise one node without disrupting the rest.

### Common workflow patterns (Anthropic-derived taxonomy)

These are the patterns from [[Anthropic]]'s "[[BuildingEffectiveAgents]]" article that Cole repeatedly references:

| Pattern | Shape |
|---|---|
| **Prompt chaining** | A → B → C, sequential |
| **Routing** | Router agent dispatches to one of several specialists |
| **Parallelization** | Multiple agents on the same input, results aggregated. See [[ParallelAgentArchitecture]]. |
| **Orchestrator-workers** | Orchestrator dynamically spawns and coordinates workers |
| **Evaluator-optimizer** | Generator + critic loop, iterating until quality threshold |

### Implementation in this playlist

[[LangGraph]] is the orchestration layer. Each agent invocation is a "node"; control flow is "edges"; shared data is "state." [[PydanticAI]] handles each individual agent call. Together they cover the workflow primitives needed for all five Anthropic patterns.

### Archon as a workflow

[[Archon]] itself is an agentic workflow: Reasoner → Advisor → Coder → human-review interrupt → loop back. v5+ replaces the single Coder with parallel sub-agents (one each for prompt, tools, dependencies, agent definition) that synthesize together — a self-application of [[ParallelAgentArchitecture]].

## Related

- [[AIAgent]] — the building block
- [[ParallelAgentArchitecture]] — one specific workflow pattern
- [[SubAgent]] — pattern for specialization within a workflow
- [[HumanInTheLoop]] — common workflow pause/resume pattern
- [[LangGraph]] — orchestration layer
- [[PydanticAI]] — per-agent layer
- [[Archon]] — example workflow that builds agents
- [[Anthropic]] — author of the taxonomy Cole cites
