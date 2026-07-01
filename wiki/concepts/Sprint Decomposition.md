---
title: "Sprint Decomposition"
type: concept
tags: [ai, agents, planning, harness, long-running-agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson.md"]
last_updated: 2026-06-30
---

## Definition
Sprint Decomposition is a harness technique where a planner agent breaks a high-level prompt into a series of sprints or features, each implemented in a fresh context window by a builder agent. The planner deliberately avoids over-specifying technical details to prevent cascading errors over multi-hour time horizons.

## Key Information
- **Planner Role**: A dedicated planner agent takes a one-line prompt and breaks it into deliberately high-level sprints — it specs the general workflow, not granular technical details
- **Why Not Over-Specify**: If the planner makes an error in technical details, it cascades through every sprint and magnifies over a multi-hour time horizon. High-level specs reduce cascading failure risk
- **Featurelist.json**: Early Anthropic harness used JSON files (not markdown) for feature lists because models are less likely to overwrite JSON files
- **One Feature Per Session**: Each sprint picks exactly one unfinished feature, implements it in a fresh context window, verifies it, commits it, marks it as passed, then continues
- **Model-Dependent Necessity**: Opus 4.5 required sprint decomposition to maintain coherence. Opus 4.6 could hold a 2-hour continuous build coherently without being force-fed one feature at a time
- **Harness Evolution**: As models improve, sprint decomposition becomes less necessary. Anthropic's position: "we don't have a very strong opinion on this" — it was critical for 4.5, optional for 4.6
- **Planner Separation**: The planner sets outer boundaries but doesn't intervene mid-build. Generator and evaluator negotiate exact feature contracts within each sprint
- **Progress Tracking**: Progress file tracks which features are complete, passing tests, and remaining. Fresh context windows read this file to get bearings

## Related
- [[summary-20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson]] — source
- [[GeneratorEvaluator Pattern]] — harness pattern that uses sprint decomposition
- [[Contract Negotiation]] — within-sprint mechanism
- [[Harness Evolution]] — how sprint decomposition changes as models improve
- [[RALPH Loop]] — earlier pattern with similar feature breakdown
- [[PlanBased Approach]] — related planning methodology
- [[Agent Task States]] — progress tracking mechanism
