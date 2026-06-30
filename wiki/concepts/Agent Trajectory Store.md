---
title: "Agent Trajectory Store"
type: concept
tags: [agents, observability, debugging, coding-agents, tracing]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition
An Agent Trajectory Store is a custom observability system for coding agents that records the full sequence of agent steps and decisions. It enables diagnosis of exactly when looping started, when the model went off the rails, or where failures occurred during long-running agent sessions with many steps.

## Key Information
- **Purpose**: Diagnose specific failure points in agent execution — "at what exact point looping started happening or the model went off the rails"
- **Coding agent focus**: Designed for coding agents where a huge number of steps can occur, making it critical to pinpoint specific failure moments
- **Google's implementation**: Built as a custom internal tool alongside a web app for agent observability with hierarchical drill-down to raw predict requests
- **Hierarchical observability**: The companion web app allows drilling down at various levels of hierarchy, all the way to raw predict requests made to the model
- **Automatic capture**: When a user issues a query to an agent hosted on the backend system, the trajectory automatically appears in the observability UI
- **Contrast with general observability**: While the web app covers all agent types, the trajectory store is specifically focused on coding agent sessions with many steps

## Related
- [[AgentObservability]] — broader observability concept
- [[Trajectories]] — agent execution paths
- [[AgentDebuggability]] — the problem trajectory stores solve
- [[AgentLoop]] — the loop being traced
- [[TracesAndSpans]] — related observability primitives
- [[TraceReading]] — skill for analyzing traces
- [[GoogleDeepMind]] — organization that built it
- [[KP Sawhney]] — engineer describing the system
- [[summary-20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind]] — source
