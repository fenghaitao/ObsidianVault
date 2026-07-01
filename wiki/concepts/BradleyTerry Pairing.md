---
title: "Bradley-Terry Pairing"
type: concept
tags: [statistics, benchmarking, pvp, scheduling, efficiency, elo]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260525 - Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition
Bradley-Terry pairing is a statistical scheduling technique used in Kaggle's Game Arena to minimize the number of model-vs-model game matchups needed to achieve statistical significance in PvP benchmark results.

## Key Information

### Purpose
- Reduces the combinatorial explosion of pairwise model comparisons
- Without it, testing all model pairs across many game variants would require millions of games
- Enables statistical significance with far fewer runs

### Usage in Game Arena
- Used to schedule game runs between AI models in Poker, Werewolf, Chess
- Poker alone required ~400K hands for statistical significance — even with Bradley-Terry, the cost is enormous
- Finding additional ways to reduce the number of required games remains an active challenge

### Context
- Based on the Bradley-Terry model, a probability model for predicting the outcome of paired comparisons
- Essential for making PvP benchmarking economically feasible at scale

## Related
- [[Game Arena]] — primary application
- [[PvP Benchmarking]] — evaluation paradigm
- [[Elo Score]] — rating system fed by Bradley-Terry pairings
- [[Kaggle]] — platform using this technique
- [[MichaelAaron]] — engineer who discussed the technique
- [[summary-20260525 - Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind]] — source
