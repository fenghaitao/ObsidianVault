---
title: "Traffic Controller vs Dispatcher"
type: concept
tags: [agents, paradigm-shift, metaphor, software-engineering, control]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition

Traffic Controller vs Dispatcher is a metaphor introduced by Philipp Schmid to explain the fundamental paradigm shift from traditional software engineering to building AI agents. A traffic controller has full control over every aspect of the journey (street lights, speed limits, which roads to use). A dispatcher defines only the destination and lets the agent choose the route.

## Key Information

- **Traffic Controller (traditional software)**: The developer controls every step — which functions are called, in what order, with what conditions. The execution path is fully specified. This is the mental model senior engineers have mastered over years
- **Dispatcher (agent engineering)**: The developer defines the goal ("I want to go to London from Germany") but doesn't prescribe the exact steps. The agent might take the train, fly, or drive under the water — it may do something "very weird" but still achieve the outcome
- **The core tension**: Senior engineers are trained to be traffic controllers. Building agents requires becoming dispatchers. This mental model shift is the root cause of the struggle
- **Goal-oriented vs step-oriented**: Traditional engineering focuses on defining steps. Agent engineering focuses on defining goals and constraints, then iterating on prompts and tools based on observed behavior
- **The iterative loop**: Instead of spec → code → test → deploy, agent building is: define instructions → run → observe → adjust prompts/tools → run again. This is an iterative improvement cycle, not a linear construction process
- **Accepting weird paths**: Every coding agent user has seen their agent do something strange that still achieved the correct outcome. This is a feature of the paradigm, not a bug

## Related

- [[summary-20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind]] — source
- [[PhilippSchmid]] — speaker who introduced the metaphor
- [[Handing Over Control]] — the principle this metaphor illustrates
- [[Stop Fighting the Model]] — related principle: don't force rigid workflows
- [[Trust But Verify]] — complementary principle: define goals, validate outcomes
- [[AgenticLoop]] — the execution pattern of the dispatcher model
