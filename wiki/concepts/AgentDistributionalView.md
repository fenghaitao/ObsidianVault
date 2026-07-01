---
title: "AgentDistributionalView"
type: concept
tags: [observability, agent, distribution, trajectories, arize]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260607 - LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize.md"]
last_updated: 2026-06-30
---

## Definition
Agent Distributional View is an observability technique that looks across all instantiations of an agent to understand the distribution of paths, branches, and loops it takes, rather than examining a single invocation. It enables answering questions about traffic distribution, latency per branch, and comparative signal quality across different agent trajectories.

## Key Information
- Introduced by Dat Ngo (Arize) as a complement to single-trace inspection
- Instead of looking at one agent run, view all instantiations to get a distributional perspective
- **Traffic distribution**: What percentage of traffic goes down one branch versus another?
- **Latency analysis**: Was there a particular component in a specific branch that caused significant latency?
- **Loop detection**: Identify where agents are looping across multiple runs
- **Comparative signal quality**: When evals drop on a particular trajectory, compare against other trajectories to identify the root cause
- Works hand-in-hand with trajectory analysis: find problematic branches, then drill into the specific trajectory to identify root cause (e.g., component ordering issues)
- Part of the broader observability toolkit alongside traces, spans, and sessions

## Related
- [[DatNgo]] — speaker who introduced this concept
- [[Arize]] — platform providing this view
- [[Trajectory Analysis]] — complementary technique for root cause
- [[TracesAndSpans]] — underlying observability primitives
- [[AgentObservability]] — broader observability context
- [[EvalScopes]] — trajectory evals leverage distributional views
- [[summary-20260607 - LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize]] — source
