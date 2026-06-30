---
title: "Trust But Verify"
type: concept
tags: [agents, verification, trust, evals, guardrails]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition

Trust But Verify is a core principle for building AI agents: give the LLM autonomy to make decisions and choose execution paths (trust), but validate outcomes through evals, guardrails, and measurement (verify). It balances the need to hand over control with the need to ensure reliability.

## Key Information

- **Articulated by Philipp Schmid** as one of the core principles for building agents
- **Trust**: Hand over control to the LLM. Don't predefine every step. Let the agent choose its path. Accept that it may take unexpected routes to achieve the goal
- **Verify**: Don't assume the agent did the right thing. Measure outcomes through evals. Validate results with guardrails. Use LLM-as-judge or human experts for subjective outputs
- **The balance**: Too much control (no trust) means you're building traditional software, not leveraging agent capabilities. Too little verification means unreliable systems that fail in production
- **Statistical verification**: Unlike traditional software where you assert `input A → output C`, agent verification is statistical — you measure how often the agent succeeds across many runs
- **Context**: This principle is especially important because agents are non-deterministic — the same input can produce different paths and results. Trust enables flexibility; verification ensures reliability

## Related

- [[summary-20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind]] — source
- [[PhilippSchmid]] — speaker
- [[Handing Over Control]] — the "trust" side of the equation
- [[Evaluate Dont Just Assert]] — the "verify" side of the equation
- [[EvalPrimitives]] — the measurement tools for verification
- [[Non-Deterministic Agents]] — why verification must be statistical
- [[Bounded Autonomy]] — related concept: balancing freedom and constraints
- [[Verification in Agentic Loops]] — implementing verification in agent systems
