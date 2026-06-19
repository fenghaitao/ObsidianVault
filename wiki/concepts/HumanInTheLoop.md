---
title: "HumanInTheLoop"
type: concept
tags: [concept, agents, workflow, langgraph, hitl]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/02 - 10x Your AI Agents with this ONE Agent Architecture.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/03 - Coding Subagents - The Next Evolution of AI IDEs.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
last_updated: 2026-06-19
---

## Definition

Human-in-the-loop (HITL) is an [[AgenticWorkflow]] pattern where the workflow pauses at designated points to wait for human input — confirmation, correction, or additional information — before resuming. It's how agentic systems remain steerable when full autonomy would be risky or premature.

## Key Information

### Implementation in [[LangGraph]]

LangGraph provides a first-class primitive: `interrupt()`. Inside a node, calling `interrupt()` halts the graph and surfaces the pending value to the caller. Resumption happens by re-invoking the graph with `Command(resume=user_input)`, which sets the interrupted value and lets the graph continue from where it stopped.

```python
def get_next_user_message(state):
    user_input = interrupt(value="awaiting user response")
    return {"user_input": user_input}
```

Combined with a memory saver (`MemorySaver`, `SqliteSaver`, etc.), the graph state survives across the pause — you can resume in the same process or a different one with the same `thread_id`.

### Concrete examples in this playlist

| Workflow | Pause point | What the human provides |
|---|---|---|
| **Travel Planner** (info-gatherer agent) | After agent emits "I need more details" | The missing trip details |
| **[[Archon]]** (after Coder generates agent code) | After initial code emission | Approval, correction, or "iterate on X" |
| **Windsurf + Archon over MCP** | Each Archon iteration round | "Ask Archon to fix the model field" — the user's natural-language refinement |

### Why HITL matters for current agents

- LLMs still hallucinate, especially on framework-specific details. HITL is the cheap insurance.
- Specifying tasks fully up front is hard; interactive refinement is more natural.
- Critical actions (writing files, calling external APIs with side effects) benefit from explicit approval.
- When the agent doesn't have enough context, HITL lets it ask rather than guess.

### Trade-offs

- **Pro**: caps blast radius from agent errors.
- **Pro**: lets agents start producing value before they're fully autonomous.
- **Con**: latency — waiting for a human is slow.
- **Con**: doesn't scale — you can't HITL every step in a 10,000-step pipeline.

The Archon roadmap (v8 self-feedback loops, v9 self-execution) explicitly aims to *reduce* HITL touchpoints over time as autonomous capabilities mature. HITL is a stepping stone, not the destination.

### MCP version of HITL

In the Windsurf-calls-Archon pattern, HITL is *layered*: Windsurf is itself running a HITL conversation with the user, and within each Windsurf turn, Archon may run its *own* internal loop. Each level can pause and resume.

## Related

- [[AgenticWorkflow]] — superset
- [[LangGraph]] — provides `interrupt()`
- [[Streamlit]] — typical UI surface for HITL
- [[Archon]] — uses HITL between iterations
- [[ParallelAgentArchitecture]] — orthogonal pattern, often combined
- [[ColeMedin]] — author of the demos
