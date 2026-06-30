---
title: "PlayMagnus"
type: entity
tags: [company, chess, ai, gaming]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take.md"]
last_updated: 2026-06-29
---

## Definition

Play Magnus is a chess platform (iOS/Android) founded by Magnus Carlsen, the world's best chess player. It offers game reviews powered by an AI pipeline combining Stockfish engine analysis with LLM-generated natural language commentary.

## Key Information

- Founded by Magnus Carlsen, widely considered the best chess player in the world
- iOS and Android app for playing chess and getting AI-powered game reviews
- AI pipeline: Stockfish (best moves) + positional/tactical detectors + Maya (human move prediction) + LLM commentary
- Autonomous agent closes the feedback loop: user reports bad commentary → agent fixes via PR
- Uses Gemini 3 Flash for commentary generation (sub-3 second target)

## Related

- [[summary-20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take]] — source
- [[Stockfish]] — chess engine
- [[AlphaZero]] — DeepMind chess AI
- [[ChessAI]] — chess and AI
