---
title: "Trajectories"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.md"]
last_updated: 2026-06-29
---

# Trajectories

## Definition

Trajectories are visual representations of agent tool call topology — the sequence and structure of tools an agent calls during a session, including which tools were called, in what order, which had errors, and how different trajectories compare to each other. Raindrop provides trajectory visualization as a core feature for debugging agent behavior.

## Key Information

### What Trajectories Show

- The full sequence of tool calls in an agent session
- Which tools were called and in what order
- Which tool calls had errors (color-coded)
- Input and output for each specific tool call
- The overall "shape" and topology of the agent's behavior

### Search and Discovery

- Natural language search: describe the type of trajectory you want to find (e.g., "traces with three different tool call failures")
- Similarity matching: find trajectories that "look similar" to a problematic one
- Pattern recognition: identify recurring failure patterns across sessions

### Use Cases

- Debugging: click into a specific tool call to see what input caused the error
- Pattern discovery: find all sessions where a particular tool failed in a particular sequence
- Root cause analysis: the Triage Agent uses trajectory data to investigate signal spikes
- Topology understanding: get a "shape and understanding" of what the agent is doing

### Comparison to Traditional Tracing

Traditional observability tools show spans and logs; trajectories add a visual, topological layer specifically designed for agent tool calls. This is described as "pretty much the only place where you can visualize tools like this."

## Related

- [[AgentObservability]] — parent concept
- [[Raindrop]] — platform providing trajectory visualization
- [[TriageAgent]] — uses trajectory data for root cause analysis
- [[TracesAndSpans]] — traditional tracing concept
- [[summary-20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop]] — source transcript
