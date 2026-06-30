---
title: "TauBench"
type: entity
tags: [benchmark, agents, multi-turn, policy, evaluation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260604 - The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI.md"]
last_updated: 2026-06-30
---

## Definition
TauBench is a benchmark for evaluating multi-turn AI agents on both task completion and adherence to policy constraints. It was built with a user simulator and evaluates agents holistically — a model that completes the task but violates policy rules still fails.

## Key Information
- Evaluates multi-turn agents on task completion
- Built with a clever user simulator for realistic interaction scenarios
- Goes beyond accuracy to measure policy constraint adherence
- Example: a model that books the right flight but violates fare class rules still fails
- Has had multiple evolutions over the years
- Cited by [[VincentChen]] as an exemplar of [[Robust Eval Methodology]]

## Related
- [[Benchmarking Agents]] — framework that cites TauBench as exemplar
- [[Robust Eval Methodology]] — the concept TauBench exemplifies
- [[Policy Constraint Adherence]] — key evaluation dimension pioneered by TauBench
- [[summary-20260604 - The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI]] — source transcript
