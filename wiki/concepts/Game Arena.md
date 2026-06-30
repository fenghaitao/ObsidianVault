---
title: "Game Arena"
type: concept
tags: [benchmark, pvp, elo, games, unsaturable, kaggle, evaluation, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260525 - Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition
Game Arena is Kaggle's PvP (player-versus-player) benchmark platform where AI models compete against each other in games, producing unsaturable Elo score ratings. Because models always face a winner and a loser, the benchmark remains evergreen and cannot be saturated.

## Key Information

### Purpose
- Addresses benchmark saturation by using PvP competition instead of static tests
- Models can always compete against each other — there is always a winner and a loser
- Produces Elo score ratings for model comparison

### Current Games
- **Werewolf**: Tests deception capabilities
- **Poker**: Tests randomization and deception. Reveals model personalities — Grok loves going all-in, newer generation models are more risk-averse and conservative
- **Chess**: Standard ML analysis staple

### Engineering Pipeline
1. Design and iterate on game selection to analyze separate AI capabilities
2. Spend significant time iterating prompts to ensure fairness across models
3. Build harness — mostly using OpenSpiel RL framework
4. Test whether models play better than random, observe emergent properties
5. Run simulations via LLM model proxy (available on Colab) on Kaggle simulation platform (originally an RL platform)
6. Schedule game runs using Bradley-Terry pairwise to minimize the number of games needed
7. Publish results: Elo scores on benchmarks, LLM conversation datasets on Kaggle, and game visualizer

### Key Challenges
- **Cost**: Poker required ~400K hands for statistical significance — API bills are enormous. Bradley-Terry pairing helps but finding ways to achieve significance with fewer games is critical
- **Community engagement**: Watching LLMs play each other gets repetitive. Exploring models like prompt-engineering hackathons where the community provides prompts to play games and climb leaderboards
- **Comparison over time**: Old models disappear, new models arrive, endpoint providers aren't always transparent about which model is actually running behind an endpoint

### Open Source
- All games, prompts, and results are open source with a public GitHub repository
- Conversation datasets from model games are published on Kaggle for community analysis

## Related
- [[BenchmarkSaturation]] — problem Game Arena addresses
- [[PvP Benchmarking]] — evaluation paradigm
- [[Elo Score]] — rating system used
- [[Bradley-Terry Pairing]] — statistical scheduling technique
- [[OpenSpiel]] — RL framework for games
- [[Kaggle]] — platform hosting Game Arena
- [[GoogleDeepMind]] — parent organization
- [[NicholasKang]] — presenter
- [[MichaelAaron]] — presenter, deep-dived into Game Arena
- [[AgenticEvaluations]] — broader evaluation context
- [[summary-20260525 - Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind]] — source
