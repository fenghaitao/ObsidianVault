---
title: "ChessAI"
type: concept
tags: [chess, ai, gaming, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take.md"]
last_updated: 2026-06-29
---

## Definition

Chess AI spans from brute-force engines (type A, e.g. Stockfish, Deep Blue) to neural network approaches (type B, e.g. AlphaZero) to LLM-based commentary systems. LLMs alone play chess poorly due to hallucination, but can excel at explaining chess when grounded in structured engine analysis.

## Key Information

- Claude Shannon (1949): type A (brute force) vs type B (selective/intuitive) chess engines
- Deep Blue beat Kasparov (1997) using type A brute force
- AlphaZero (DeepMind, 2017): neural network that learned chess/Go/Shogi via self-play
- Transformers trained on Stockfish evaluations can play at grandmaster level
- LLMs trained on language hallucinate chess moves but can translate structured engine data into natural language commentary
- Kaggle Game Arena: benchmark for LLMs playing chess and other games

## Related

- [[summary-20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take]] — source
- [[Stockfish]] — leading chess engine
- [[AlphaZero]] — DeepMind chess AI
- [[PlayMagnus]] — Magnus Carlsen's chess platform
