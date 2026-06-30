---
title: "Play Magnus"
type: entity
tags: [company, chess, app, mobile, ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take.md"]
last_updated: 2026-06-30
---

## Definition
Play Magnus (also known as Take Take Take) is an iOS and Android chess application founded by world champion Magnus Carlsen. It features an AI-powered game review system that generates grounded, nuanced commentary on chess games by combining traditional chess engine analysis with LLM-based language generation.

## Key Information
- Founded by Magnus Carlsen, widely considered the best chess player in the world
- Core feature: after playing a game, users receive an AI-powered game review with commentary explaining the "why" behind each move
- Game Review pipeline: Stockfish provides ground truth, tactical/positional detectors extract context, Maya predicts human move probabilities, and an LLM translates all structured data into natural language commentary
- Also provides personalized insights about player performance: accuracy by game phase, estimated rating, opening depth
- Uses Gemini 3 Flash for commentary generation, targeting sub-3 second end-to-end latency
- Closed the feedback loop with autonomous agents: users report bad commentary, which triggers a Cloud Code Channel agent to triage, investigate, and submit fixes via PR
- Employs Anant Dole and Asbjorn Steinskog, who presented the system at AI Engineer conference

## Related
- [[Magnus Carlsen]] — founder
- [[Anant Dole]] — employee and speaker
- [[Asbjorn Steinskog]] — employee and speaker
- [[Stockfish]] — chess engine used for ground truth analysis
- [[Maya]] — human-move prediction engine used in the pipeline
- [[Gemini 3 Flash]] — LLM used for commentary generation
- [[Autonomous Agent Feedback Loop]] — feedback mechanism for improving commentary
- [[Separating Data Pipeline from Language Generation]] — core architectural pattern
- [[summary-20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take]] — source
