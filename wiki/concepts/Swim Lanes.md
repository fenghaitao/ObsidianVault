---
title: "Swim Lanes"
type: concept
tags: [ai, agents, engineering, workflow, parallelism, open-claw]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Dark Factory： OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw.md"]
last_updated: 2026-06-30
---

## Definition
Swim lanes are a parallel agent management pattern where an engineer runs multiple concurrent agent sessions, each dedicated to a distinct category of work. Each lane operates semi-autonomously with different levels of human oversight, analogous to production lines in a factory. Vincent Koc uses this pattern to manage the extreme velocity of OpenClaw development, running 5-20+ swim lanes simultaneously.

## Key Information

- **Origin**: Vincent Koc's personal workflow pattern for managing parallel agent sessions in OpenClaw development
- **Lane types**: Typically organized by work category — CI, features, bugs, refactoring, P0/P1 monitoring, specific channels (Docker, messaging)
- **Low-touch lanes** (e.g., test refactoring): Agents are told "Take your time. Make sure tests pass. Just push them through." — minimal babysitting required
- **High-touch lanes** (e.g., features, Docker, messaging channels): Conversational interaction — agents investigate, do work, come back with results
- **Monitor lanes**: Agents running in Discord channels, reporting on releases — "What's happened in the last 2 hours that I need to pay attention to?"
- **Scaling**: Lanes scale up and down based on current needs and stability of the codebase
- **Bottleneck**: Not tokens or compute — "my brain space in order to sort of keep an eye on all of these sessions"
- **Relationship to dark factory**: Swim lanes are the operational implementation of the dark factory concept — they are the "production lines" the factory manager oversees

## Related
- [[summary-20260605 - Dark Factory： OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw]] — primary source
- [[VincentKoc]] — originator of the pattern
- [[Dark Factory]] — the overarching concept swim lanes implement
- [[Agent Parallelism]] — running multiple agents simultaneously
- [[Bot Looping]] — the agent loop approach used within swim lanes
- [[OpenClaw]] — the project where this pattern is applied
- [[AgentHarness]] — the infrastructure running these sessions
- [[Codex]] — the agent coding tool used for swim lane sessions
- [[Soft Skills for Agent Management]] — required for managing multiple lanes
