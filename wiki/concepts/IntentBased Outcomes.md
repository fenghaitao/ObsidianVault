---
title: "Intent-Based Outcomes"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests — Vincent Koc, OpenClaw.md"]
last_updated: 2026-06-30
---

## Definition

Intent-based outcomes are an evaluation approach where assessment is based on whether the agent achieves the desired end state, rather than comparing its output to a predetermined "correct" answer. Instead of testing "1 + 1 = 2" or a specific question-answer pair, the evaluation defines what success looks like and lets the agent determine how to get there.

## Key Information

- **Shift from path to destination**: Traditional evals test whether the agent followed the expected path. Intent-based evals test whether the agent reached the right destination, regardless of how it got there
- **Handling ambiguity**: This approach accommodates agent personality, varied user experiences, and ambiguous situations — dimensions that static benchmarks cannot capture
- **Rubric-based evaluation**: Similar to how art is evaluated in schools — not a single correct answer, but assessment against defined criteria of quality
- **Auto-optimization alignment**: Mirrors Karpathy-style auto-optimization research where you set a goal, set a target, and let the system tune itself toward the reward signal
- **Key insight**: The eval becomes the goal definition, not the dataset. Users define the intended outcome, and the machine works backward to achieve it.

## Related

- [[summary-20260512 - Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests — Vincent Koc, OpenClaw]] — primary source
- [[VincentKoc]] — proposed the concept
- [[Malleable Evals]] — broader framework
- [[Intent Engineering]] — the paradigm that enables intent-based outcomes
- [[AndrejKarpathy]] — auto-optimization methodology referenced
- [[Static Benchmarks]] — the traditional approach being superseded
