---
title: "TauBench"
type: entity
tags: [benchmark, agents, multi-turn, policy, evaluation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260604 - The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260410 - Judge the Judge： Building LLM Evaluators That Actually Work with GEPA — Mahmoud Mabrouk, Agenta AI.md"]
last_updated: 2026-06-30
---

## Definition
TauBench is a benchmark for evaluating multi-turn AI agents on both task completion and adherence to policy constraints. Built by Sierra, it features a customer support airline agent with complex policy rules, multiple tool integrations, and 599 annotated conversation traces (62% compliant / 38% non-compliant). It was built with a user simulator and evaluates agents holistically — a model that completes the task but violates policy rules still fails.

## Key Information
- Built by [[Sierra]], a customer support scaleup
- Evaluates multi-turn agents on task completion and policy constraint adherence
- Built with a clever user simulator for realistic interaction scenarios
- The airline agent benchmark features: complex policy rules for reservation changes and information provision, multiple tool integrations (reservations, flights, user data), and 599 conversation traces with annotations
- Data distribution: 62% compliant, 38% non-compliant, generated with multiple models and trials
- Data caveats noted by [[Mahmoud Mabrouk]]: AI-generated annotations (derived from assertions, not human-labeled), small dataset, redundancies from same tasks with same models, complex policy making it a realistic but challenging test case
- Has had multiple evolutions over the years
- Cited by [[VincentChen]] as an exemplar of [[Robust Eval Methodology]]
- Used by [[Mahmoud Mabrouk]] to demonstrate GEPA-based LLM-as-judge optimization — accuracy improved from 61% to 74% on this benchmark

## Related
- [[Sierra]] — the company that built TauBench
- [[Benchmarking Agents]] — framework that cites TauBench as exemplar
- [[Robust Eval Methodology]] — the concept TauBench exemplifies
- [[Policy Constraint Adherence]] — key evaluation dimension pioneered by TauBench
- [[LLMAsJudge]] — evaluation technique optimized on TauBench data
- [[GEPA]] — algorithm used to optimize LLM judges on TauBench
- [[Mahmoud Mabrouk]] — used TauBench in his GEPA workshop
- [[summary-20260604 - The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI]] — source transcript
- [[summary-20260410 - Judge the Judge： Building LLM Evaluators That Actually Work with GEPA — Mahmoud Mabrouk, Agenta AI]] — source
