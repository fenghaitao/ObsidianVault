---
title: "LLM Hallucination In Chess"
type: concept
tags: [llm, hallucination, chess, limitation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take.md"]
last_updated: 2026-06-30
---

## Definition
The phenomenon where LLMs fail to play chess correctly despite their language fluency — they can sometimes produce reasonable opening moves but quickly hallucinate illegal or nonsensical moves because they are trained on language, not calculation.

## Key Information
- LLMs are trained on language, not on chess calculation — they lack the ability to search move trees or evaluate positions
- They can sometimes play reasonable openings because opening patterns appear frequently in training data, but they quickly fall apart in middlegame positions
- High reasoning models can "to an extent calculate through the reasoning steps where they can actually play out moves, but they quickly fall apart"
- There is nothing inherently wrong with transformer architecture for chess: DeepMind trained a transformer on chess positions paired with Stockfish evaluations, and it played at grandmaster level — but that model was trained on positions, not language, so it cannot explain chess
- Magnus Carlsen commented on an LLM chess tournament: LLMs "don't really know how to play chess"
- Kaggle's game arena included chess as a benchmark for LLM game-playing ability
- The Play Magnus solution: use deterministic chess engines for analysis and LLMs only for language translation of pre-computed findings

## Related
- [[Separating Data Pipeline from Language Generation]] — the architectural solution to this problem
- [[Chess Context Extraction]] — feeds structured data to LLMs so they don't need to reason about chess
- [[Stockfish]] — deterministic chess engine that provides ground truth, avoiding LLM hallucination
- [[Maya]] — human-move prediction that provides additional grounded context
- [[Magnus Carlsen]] — observed and commented on LLM chess failures
- [[Kaggle]] — organized the LLM chess tournament
- [[Play Magnus]] — built a production system that works around this limitation
- [[summary-20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take]] — source
