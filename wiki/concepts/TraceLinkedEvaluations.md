---
title: "Trace-Linked Evaluations"
type: concept
tags: [observability, evaluations, tracing, debugging, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft.md"]
last_updated: 2026-06-30
---

## Definition
Trace-linked evaluations combine agent traces (showing how an agent executed) with evaluation results (showing what the outcome was) in a single unified view, dramatically shortening the time between detecting a problem and diagnosing its root cause.

## Key Information

### Core Value
- Traditional approach: detect a metric regression → separately investigate traces to find the cause
- Trace-linked approach: see both together — when a metric fails, immediately inspect the relevant trace to see what changed
- Shortens the loop from detection to diagnosis, enabling faster fixes

### How It Works (Microsoft Foundry)
- Every agent invocation produces a trace (sequence of steps, tool calls, messages)
- Evaluations are linked to specific traces, showing metric results alongside execution details
- When an eval metric drops (e.g., tool calling accuracy), the developer can immediately drill into the trace to see which tool didn't get called or why

### Use Cases
- **Model change regression**: Switched from GPT-4 1 to GPT-4 mini — eval shows tool calls are less efficient, trace reveals which tool failed
- **Prompt optimization**: After changing instructions, compare trace-linked evals before and after to see if intent resolution improved
- **Cost optimization**: When optimizing for cost, ensure accuracy doesn't regress by comparing trace-linked evals

### Importance for Multi-Agent Systems
- With workflow agents, a single invocation spawns multiple sub-agent traces
- Trace-linked evaluations pinpoint which specific sub-agent is underperforming
- Enables targeted optimization: only fix the underperforming agent, not the entire system

## Related
- [[AgentObservability]] — broader observability framework
- [[TracesAndSpans]] — tracing fundamentals
- [[Custom Tracing Tools]] — building custom trace attributes
- [[OnlineEvals]] — evaluation of production traffic
- [[Microsoft Foundry]] — platform implementing trace-linked evaluations
- [[summary-20260514 - Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft]] — source
- [[summary-20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop]] — related observability talk
