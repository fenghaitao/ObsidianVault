---
title: "Cascading Failures"
type: concept
tags: [agent, failure, debugging, multi-step]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md"]
last_updated: 2026-06-30
---

## Definition
Cascading failures occur in AI agents when an early misstep propagates through subsequent steps, leading to radically incorrect outputs. Unlike single LLM calls where you test one output, agents have multiple steps where each step's correctness depends on the previous step.

## Key Information
- Agents make evaluation harder because they have multiple decision points, not just one output
- Must test at each step: did the agent pick the right tool? Send the right parameters? Correctly understand the tool output? Correctly use that output in the next step?
- Each tool call relies on the output of the previous tool call — errors compound
- Multi-agent systems add more complexity: did the routing LLM choose the right sub-agent? Did the sub-agent understand the task? Pass info back correctly? Stop when supposed to?
- Example: agent asked to "write a report on Tesla" — research agent assumes Nikola Tesla (18th century inventor), writes report on him, investment case goes to boss based on wrong Tesla. Nobody notices because the agent ran autonomously
- The opposite is also possible: agents can get things right in unexpected ways — too-prescriptive evals that expect specific tool call sequences will break when agents find cleverer paths
- Best practice: test outcomes, not paths. Don't write evals that say "must call tool A then tool B then make decision C" — the agent might find a faster way
- Tracing is essential: you need to see every step the agent took to understand where cascading failures began

## Related
- [[AgentObservability]] — tracing to diagnose cascading failures
- [[TracesAndSpans]] — the data structure that reveals failure propagation
- [[Swiss Cheese Model]] — layered defense against cascading failures
- [[FailureModeAnalysis]] — systematic approach to identifying failure patterns
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
