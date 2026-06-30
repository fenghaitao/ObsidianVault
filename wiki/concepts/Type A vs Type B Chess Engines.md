---
title: "Type A vs Type B Chess Engines"
type: concept
tags: [chess, ai, history, classification, engines]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take.md"]
last_updated: 2026-06-30
---

## Definition
Claude Shannon's 1949 classification of chess engines into two types: Type A (brute force search through all possible moves to find the best one) and Type B (selective, intuitive engines that pick promising moves without exhaustive search). This framework remains relevant for understanding the evolution of chess AI.

## Key Information
- Proposed by Claude Shannon in his 1949 paper "Programming a Computer to Play Chess"
- Shannon assumed Type B would be necessary because early computers were too weak for exhaustive search — but computers improved rapidly, making Type A viable
- Type A lineage: early chess programs → Deep Blue (beat Kasparov in 1997) → Stockfish (modern leading engine)
- Type B lineage: long neglected → AlphaGo (Go is too complex for brute force) → AlphaZero (neural network mastering chess, Go, shogi)
- Modern LLMs represent a third category: they can explain chess but cannot play it (trained on language, not positions)
- DeepMind demonstrated that transformers can play grandmaster-level chess when trained on positions (not language) paired with Stockfish evaluations
- The Play Magnus team bridges both worlds: Type A engines for analysis, LLMs for explanation

## Related
- [[Claude Shannon]] — originated this classification
- [[Stockfish]] — canonical modern Type A engine
- [[Deep Blue]] — first Type A engine to beat a world champion
- [[AlphaZero]] — canonical Type B (neural network) engine
- [[Garry Kasparov]] — world champion beaten by a Type A engine
- [[Separating Data Pipeline from Language Generation]] — modern approach bridging both engine types with LLM explanation
- [[LLM Hallucination In Chess]] — why LLMs are neither Type A nor Type B
- [[summary-20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take]] — source
