---
title: "Handing Over Control"
type: concept
tags: [agents, non-determinism, llm, trust, workflows]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition

Handing Over Control is the principle that agent builders must trust the LLM to make dynamic decisions rather than predefining every possible state and workflow branch. It represents the shift from purely deterministic environments where all outcomes are pre-modeled to non-deterministic environments where the LLM interprets intent and adapts in real time.

## Key Information

- **Traditional approach**: Classification model detects intent → predefined workflow executes. Example: detect "churn" intent → run cancellation flow. Every possible branch must be pre-modeled
- **Agent approach**: The LLM understands semantic meaning and can dynamically offer alternatives. A user trying to cancel a subscription might be offered a downgrade instead, changing the entire conversation intent — without any predefined branch for that path
- **Why it's hard for senior engineers**: Experienced engineers are trained to control every execution path. Handing over control means accepting that the agent may take unexpected (even "weird") paths to achieve the goal
- **The dispatcher metaphor**: Traditional software is a traffic controller (control every light, speed, road). Agents are a dispatcher (define the destination, the agent chooses the route)
- **Customer support example**: Instead of classification → cancellation flow, the agent understands the user's frustration, offers a retention discount, and the user changes their mind — creating a new intent that was never explicitly modeled
- **All stateful workflow branches cannot be pre-modeled**: The combinatorial explosion of possible conversation paths makes traditional workflow modeling impractical for agent systems
- **Trust is required**: You must trust the LLM to make reasonable decisions, while verifying outcomes through evals and guardrails

## Related

- [[summary-20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind]] — source
- [[PhilippSchmid]] — speaker
- [[Traffic Controller vs Dispatcher]] — the metaphor for this paradigm shift
- [[Trust But Verify]] — the complementary principle: give autonomy but validate
- [[Stop Fighting the Model]] — related principle: don't force rigid workflows
- [[Non-Deterministic Agents]] — the technical reality driving this shift
- [[Bounded Autonomy]] — related concept: balancing freedom and control
- [[AgenticLoop]] — the execution pattern where the LLM has agency
