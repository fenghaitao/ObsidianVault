---
title: "Stockfish"
type: entity
tags: [chess, engine, open-source, ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take.md"]
last_updated: 2026-06-30
---

## Definition
Stockfish is the leading classical chess engine that calculates the best move in any given chess position through brute force search. It serves as the ground truth reference for chess analysis.

## Key Information
- Type A chess engine in Claude Shannon's 1949 classification (brute force search through possible moves)
- Used as the foundational analysis layer in the Play Magnus game review pipeline — runs through the entire game to establish the objective best moves
- Provides the "solution" for any chess position, against which human moves and LLM commentary are evaluated
- Combined with tactical detectors and Maya (human-move prediction engine) to provide rich context that is then translated into natural language by an LLM

## Related
- [[Play Magnus]] — uses Stockfish in their game review pipeline
- [[Maya]] — complementary engine predicting human moves by rating
- [[AlphaZero]] — neural network alternative to classical engines like Stockfish
- [[Deep Blue]] — historical predecessor to modern chess engines
- [[Claude Shannon]] — originated the Type A classification that Stockfish embodies
- [[Type A vs Type B Chess Engines]] — Stockfish is the canonical Type A engine
- [[Chess Context Extraction]] — detectors that augment Stockfish analysis
- [[summary-20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take]] — source
