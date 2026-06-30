---
title: "Chess Context Extraction"
type: concept
tags: [chess, context, detectors, pipeline, analysis]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take.md"]
last_updated: 2026-06-30
---

## Definition
The process of running specialized detectors on chess positions to extract structured information about tactics, threats, plans, and positional themes. This structured context is fed to an LLM so it can generate grounded commentary without needing to reason about chess itself.

## Key Information
- Detectors identify tactical patterns: forks, pins, skewers, discovered attacks, and other tactical motifs
- Detectors identify positional and structural themes: doubled pawns (a disadvantage), pawn structure weaknesses, piece activity, king safety
- Detectors identify threats and plans: what each side is threatening, what plans could arise from the position
- Combined with Stockfish analysis (best move, evaluation) and Maya predictions (human move probability by rating level)
- All of this information is structured and fed to the LLM as context — the LLM's job is only translation
- Building the context extraction model is described as "a very slow sort of painful process" — starts as a large JSON file that is progressively pruned
- The commentary triage skill in the autonomous agent feedback loop can modify detectors and create new ones to fix bad commentary
- Anant Dole emphasized: "always try to build a very clear sort of context extraction model"

## Related
- [[Separating Data Pipeline from Language Generation]] — the architectural pattern this enables
- [[Stockfish]] — provides the objective best move analysis
- [[Maya]] — provides human move probability context
- [[Play Magnus]] — implements this in production
- [[Autonomous Agent Feedback Loop]] — can modify these detectors to fix issues
- [[LLM Hallucination In Chess]] — the problem this approach solves
- [[summary-20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take]] — source
