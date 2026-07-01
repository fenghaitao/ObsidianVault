---
title: "Opic"
type: entity
tags: [tool, observability, monitoring, evals, ai-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi.md"]
last_updated: 2026-06-26
---

## Definition
Opic is an observability platform used for monitoring AI agents and workflows. It captures threads (full workflow conversations), traces (individual LLM and tool calls), latency, cost, token usage, and metadata. It also supports AI evals with experiment tracking, LLM-as-judge calibration, and online evaluation on production traces.

## Key Information
- Used by the Towards AI team to monitor both their deep research agent and writing workflow
- Core concepts: threads (full workflow conversations), traces (individual LLM/tool calls within a thread)
- Captures latency, cost, token usage, input/output, and metadata per trace
- Supports experiment tracking for AI evals: dev/test split experiments, F1 score computation, LLM-as-judge calibration
- Provides an experiments tab similar to fine-tuning experiment trackers
- Enables online evaluation: running LLM-as-judge on live production traces
- Used to debug agentic systems where raw terminal logs are insufficient
- Stores traces for building AI eval layers on top of production data

## Related
- [[summary-20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi]] — source
- [[AgentObservability]] — the practice Opic enables
- [[EvalEngineering]] — evals workflow supported by Opic
- [[LLMAsJudge]] — evaluation technique tracked in Opic experiments
- [[Towards AI]] — company using Opic
