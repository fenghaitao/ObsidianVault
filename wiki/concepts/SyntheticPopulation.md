---
title: "SyntheticPopulation"
type: concept
tags: [synthetic-data, simulation, forecasting, polling, agentic-workflow]
sources: ["raw/01-articles/claude/2026-06-17 - Meet the winners of our Claude Opus 4.8 Build Day hackathon.md"]
last_updated: 2026-07-07
---

## Definition

Synthetic population modeling creates a large set of artificial residents drawn from real demographic data, each with their own demographics, personal history, and worldview, used to simulate and forecast collective behavior at scale. It was demonstrated by [[SimFrancisco]] at [[Anthropic]]'s [[ClaudeOpus4.8]] Build Day hackathon.

## Key Information

- **Demonstrated in Sim Francisco**: 10,000 synthetic residents drawn from US Census data, placed on a map of San Francisco and reacting to the news in real time. Polling the synthetic electorate produced forecasts matching real-world outcomes within a few percentage points.
- **Accuracy results**: forecast the 2024 presidential vote at 81.3% Democratic (actual 83.8%) and San Francisco's March 2024 Prop A at 70% (actual 70.38%). Tracks prediction markets like [[Kalshi]] and [[Polymarket]] within a couple of points.
- **Cost optimization via clustering**: the initial approach of making a separate inference call per resident was cost-prohibitive. [[Claude]] created an evolutionary clustering algorithm that batched 10,000 residents into ~300 representative personas, preserving accuracy while cutting inference cost 10-100x.
- **Verification**: the team used a verifier and an adversarial agent alongside Claude to ensure the backend reproduced the city's real demographic distributions.
- **Broader applications**: beyond election forecasting, synthetic populations can be used for policy simulation, market research, urban planning, and testing AI systems against diverse demographic perspectives. [[TejasPrabhune]] is exploring whether simulated personas can stay consistent enough to train models on long-horizon tasks.

## Related

- [[summary-2026-06-17 - Meet the winners of our Claude Opus 4.8 Build Day hackathon]] — source article
- [[SimFrancisco]] — the project that demonstrated synthetic population modeling
- [[ClaudeOpus4.8]] — the model used to build the system
- [[SyntheticData]] — the broader category of synthetic data generation
- [[Kalshi]] — prediction market benchmark
- [[Polymarket]] — prediction market benchmark
