---
title: "Agentic Evaluations"
type: concept
tags: [evaluations, agents, quality, tool-calling, intent-resolution]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260525 - Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition
Agentic evaluations are evaluation metrics specifically designed for AI agents, assessing the agent holistically across its entire workflow — not just individual LLM calls. They include intent resolution, tool call evaluation, and task adherence.

## Key Information

### Difference from Model Evaluations
- **Model evaluations**: Assess a single LLM call — coherence, fluency, groundedness
- **Agentic evaluations**: Assess the agent's entire workflow — did it understand intent? Did it call the right tool? Did it complete the task?

### Three Types of Agentic Evaluations (Microsoft Foundry)

**Intent Resolution**
- Evaluates whether the agent correctly understood the user's intent
- Example: User asks "What's the weather in London?" — did the agent understand the user wants local weather and make the correct next decision (tool call)?
- Critical for multi-turn agents where intent may shift across turns

**Tool Call Evaluation**
- Evaluates whether the tool call made was the expected one
- Works with percentages due to agent non-determinism — the expected tool may not always be the only valid one
- Can include operational metrics alongside correctness

**Task Adherence**
- Evaluates how well the agent completed the overall task
- Often the metric that needs most tuning over time
- Example: Groundedness failure when response used 2024 data instead of 2025

### Multi-Point Evaluation
- Agentic evaluations can be applied at multiple points in the agent lifecycle:
  - After intent resolution
  - After tool calls
  - After final response
- This granularity enables pinpointing exactly where quality drops occur

### Practical Usage
- Microsoft Foundry provides built-in agentic evaluators alongside quality and safety evaluators
- Batch evaluations run multiple agentic evaluators against datasets
- Results are trace-linked for rapid diagnosis
- Custom evaluators can be built when built-ins don't fit

## Related
- [[AgentObservability]] — broader observability framework
- [[TraceLinkedEvaluations]] — linking evaluations to traces
- [[EvalEngineering]] — evaluation methodology
- [[Model Evaluation]] — model-level evaluation vs. agent-level
- [[ToolCalling]] — tool call mechanics
- [[Microsoft Foundry]] — platform with built-in agentic evaluators
- [[summary-20260514 - Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft]] — source
- [[summary-20260525 - Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind]] — source
- [[Game Arena]] — Kaggle's PvP unsaturable benchmark
- [[Agent Exams]] — Kaggle's standardized agent testing
- [[Eval Hackathons]] — community-driven benchmark creation
- [[Kaggle]] — platform with multiple eval products
- [[NicholasKang]] — PM for Kaggle Benchmarks
- [[MichaelAaron]] — SWE on Kaggle evaluations
- [[summary-20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind]] — source (mock TPUs, skill-authored evals, meta-evaluation by agents)
- [[KP Sawhney]] — describes evaluation challenges at Google scale
- [[Model Tiering]] — using mock TPUs to save compute during evaluation
