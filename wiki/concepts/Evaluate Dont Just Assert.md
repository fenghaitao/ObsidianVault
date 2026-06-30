---
title: "Evaluate Dont Just Assert"
type: concept
tags: [agents, evals, testing, non-determinism, reliability]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition

Evaluate Don't Just Assert is the principle that agent systems cannot be validated through traditional deterministic assertions (`input A → output C`). Instead, they require statistical evaluation — measuring how often the agent succeeds across many runs, with subjective quality assessment for open-ended outputs.

## Key Information

- **Articulated by Philipp Schmid** as a core principle for agent building
- **Traditional testing**: Unit tests, integration tests, smoke tests — all assume deterministic behavior. Given input A and code B, you always get output C. Assertions are binary pass/fail
- **Agent testing**: Agents are non-deterministic. The same input can produce different steps and results. Success must be measured statistically: "Does this work 9 out of 10 times? 99 out of 100?"
- **The reliability threshold**: A customer-facing agent that works 1 out of 10 times is useless in production. Finding the right reliability balance is essential — what pass rate is acceptable for the use case?
- **Subjective outcomes**: Many agent outputs are inherently subjective. A research report, a customer response, or a creative output can't be evaluated with a simple assertion. Requires LLM-as-judge, human expert review, or rubric-based evaluation
- **Trace and measure outcomes**: Trace everything the agent does during execution, but measure success based on the final outcome. One user's agent run might take 4 extra steps and more tokens — that's fine if the outcome is correct
- **Evals over unit tests**: The shift is from "does this code path work?" to "how often does this agent succeed?" — a fundamentally different testing philosophy

## Related

- [[summary-20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind]] — source
- [[PhilippSchmid]] — speaker
- [[Trust But Verify]] — the broader principle this implements
- [[EvalPrimitives]] — the measurement infrastructure for evaluation
- [[Non-Deterministic Agents]] — why assertions don't work
- [[AgenticEvaluations]] — the practice of evaluating agent systems
- [[LLM as Judge]] — evaluation method for subjective outputs
- [[Rubric-Based Evaluation]] — structured evaluation approach
- [[Eval-Driven Development]] — development methodology based on evaluation
