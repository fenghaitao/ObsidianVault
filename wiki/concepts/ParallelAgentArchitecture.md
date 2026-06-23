---
title: "ParallelAgentArchitecture"
type: concept
tags: [concept, agents, architecture, parallelism, langgraph]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/02 - 10x Your AI Agents with this ONE Agent Architecture.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
last_updated: 2026-06-19
---

## Definition

The Parallel Agent Architecture is a multi-agent pattern where specialized [[SubAgent]]s execute simultaneously on different sub-problems, then a synthesizer (usually another agent) combines their outputs into a final result. It's [[ColeMedin]]'s preferred name for what [[Anthropic]]'s "[[summary-building-effective-agents]]" article calls **parallelization** (or, when the aggregator is itself an LLM, **orchestrator-workers**).

## Key Information

### Shape

```
                      ┌→ Specialist A ─┐
User input → Router →─├→ Specialist B ─┤→ Synthesizer → Final output
                      └→ Specialist C ─┘
```

- Each specialist gets the same input (or a slice of it) plus a task-specific prompt and tools.
- Specialists run **truly concurrently**, not sequentially-with-aggregation. Total wall-clock = max specialist time, not sum.
- The synthesizer (LLM) reasons over all specialist outputs and produces a coherent final answer. A non-LLM aggregator (just merging text) is also valid for simpler use cases.

### Why it works

- **Smaller per-prompt context.** Each specialist only sees its own task and tools — no LLM-overload.
- **Real parallelism.** Independent sub-problems should not be serialized.
- **Graceful degradation.** If one specialist fails, the synthesizer can note the gap rather than collapse the whole pipeline.

### Implementation in [[LangGraph]]

The mechanism: a conditional-edge function returns a **list of node names** — LangGraph triggers all of them in parallel.

```python
def should_continue(state):
    if state.get("ready"):
        return ["flight_node", "hotel_node", "activity_node"]   # ← parallel
    return ["gather_more_info"]
```

Each parallel node updates its own slice of shared state; LangGraph merges the updates. A downstream node ("synthesizer") reads the merged state once all parallel nodes complete.

### Travel Planner demo

The pedagogical example built across the playlist: info-gatherer (gates on "do we have all required fields?") → 3 parallel sub-agents (flight, hotel, activity) → synthesizer that produces the final travel plan. With [[Streamlit]] streaming, the user watches 3 agents emit results simultaneously, then the synthesizer streams its synthesis.

### Production example: Archon v5+

[[Archon]] applies this pattern to itself. The single Coder agent is split into parallel sub-agents specialized for prompt, tools, dependencies, and agent-definition. Each refines its own slice of the generated agent code; a synthesizer combines them. Result: more consistent and higher-quality agent code than a single fat Coder produces.

### Variants and extensions

- **Synthesizer-as-validator.** The synthesizer can also reject or request retry of specialist outputs that fail validation, blurring with the Anthropic "evaluator-optimizer" pattern.
- **Multi-tier parallelism.** Each specialist can itself be a parallel sub-architecture — fractal composition.
- **Conditional fan-out.** The router can choose *how many* specialists to spawn based on input — not always all of them.

## Related

- [[AIAgent]] — building block
- [[SubAgent]] — what each parallel branch is
- [[AgenticWorkflow]] — superset
- [[LangGraph]] — implementation framework
- [[PydanticAI]] — what each specialist is built with
- [[Archon]] — production example using this pattern
- [[Anthropic]] — source of the original "parallelization" / "orchestrator-workers" naming
- [[summary-building-effective-agents]] — Anthropic article
- [[summary-02 - 10x Your AI Agents with this ONE Agent Architecture]] — primary deep dive
