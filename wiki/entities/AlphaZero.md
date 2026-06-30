---
title: "AlphaZero"
type: entity
tags: [chess, ai, neural-network, deepmind, engine]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take.md"]
last_updated: 2026-06-30
---

## Definition
AlphaZero is a neural network-based game-playing system developed by DeepMind that mastered Go, chess, and shogi through self-play reinforcement learning. It represents Claude Shannon's Type B (selective/intuitive) chess engine concept.

## Key Information
- Preceded by AlphaGo, which first demonstrated that Go (too complex for brute force) required neural network approaches
- Represents the Type B engine concept: selectively figures out which lines to calculate rather than brute force searching all moves
- Demonstrated that transformer architectures can play chess at grandmaster strength when trained on chess positions paired with evaluations
- Unlike LLMs, AlphaZero-style models are trained on chess positions, not language — so they can play chess but cannot explain it
- The Play Magnus team's insight was bridging the gap: using traditional engines for analysis and LLMs for explanation

## Related
- [[GoogleDeepMind]] — developer
- [[Deep Blue]] — earlier Type A engine that beat Kasparov
- [[Stockfish]] — modern Type A chess engine
- [[Type A vs Type B Chess Engines]] — AlphaZero is the canonical Type B engine
- [[Claude Shannon]] — originated the Type B classification
- [[Separating Data Pipeline from Language Generation]] — the bridge between AlphaZero-like play and LLM explanation
- [[summary-20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take]] — source
