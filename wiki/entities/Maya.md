---
title: "Maya"
type: entity
tags: [chess, engine, neural-network, research, university]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take.md"]
last_updated: 2026-06-30
---

## Definition
Maya is a novel chess engine developed by the University of Toronto that predicts which moves humans would play at different rating levels, rather than finding the objectively best move. It outputs a probability distribution over all moves given a specific online rating.

## Key Information
- Research project by the University of Toronto with a fundamentally different goal from traditional chess engines: predicting human behavior rather than finding optimal play
- Given a chess position and a rating (e.g., 1500), outputs the probability distribution over all possible moves
- Used in the Play Magnus game review pipeline to determine if a move is hard to find: a move might be the best move (per Stockfish) but also have very low probability of being played at a given rating level
- This enables nuanced commentary like "this was the best move, but it was also extremely difficult to find at your level"
- Complements Stockfish (which provides objective truth) by adding human-relatable context about move difficulty

## Related
- [[Stockfish]] — complementary engine providing objective best moves
- [[Play Magnus]] — uses Maya in their game review pipeline
- [[Chess Context Extraction]] — Maya is part of the context layer fed to LLMs
- [[Separating Data Pipeline from Language Generation]] — Maya contributes to the structured data layer
- [[summary-20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take]] — source
