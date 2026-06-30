---
title: "summary-20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take"
type: source
tags: [source, transcript, chess, ai-pipeline, agents, gaming]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take.md"]
last_updated: 2026-06-29
---

## Core Summary

Anant Dole and Asbjorn Steinskog from Play Magnus (Magnus Carlsen's company) present their AI chess coach pipeline: Stockfish engine analysis + positional/tactical detectors + LLM commentary translation. They close the feedback loop with an autonomous agent that triages bad commentaries via Slack, Cloud Code channels, and automated PRs.

## Key Points

- Play Magnus (iOS/Android) offers a game review after each chess match, powered by a multi-stage AI pipeline.
- Pipeline: Stockfish for best-move evaluation → detectors (forks, pins, skewers, doubled pawns, etc.) → Maya (human-like move prediction by rating) → LLM translates structured data into natural language commentary.
- LLMs alone are bad at chess (hallucinate moves), but transformers trained on Stockfish evaluations can play at grandmaster level without language ability. Their system bridges both worlds.
- Feedback loop: users report bad commentary → posted to Slack → injected into Cloud Code channel → agent runs commentary triage skill → modifies prompts/detectors → regenerates → asks questions back to Slack → submits PR.
- Latency target: sub-3 seconds for commentary generation, using Gemini 3 Flash (~1s TTFT).
- History: Claude Shannon (1949), Deep Blue vs Kasparov (1997), AlphaZero (2017), Kaggle Game Arena LLM chess tournaments.

## Related

- [[PlayMagnus]] — Magnus Carlsen's chess company
- [[Stockfish]] — leading chess engine
- [[AlphaZero]] — DeepMind's neural network chess engine
- [[Gemini]] — Google model used for commentary generation
- [[CloudCode]] — Claude Code channel feature for autonomous agent workflows
- [[ChessAI]] — chess and AI intersection
- [[AgentFeedbackLoop]] — closing the loop from user feedback to automated fixes
