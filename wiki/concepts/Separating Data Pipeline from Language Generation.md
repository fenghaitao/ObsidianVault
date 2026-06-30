---
title: "Separating Data Pipeline from Language Generation"
type: concept
tags: [architecture, llm, grounding, pipeline, pattern]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take.md"]
last_updated: 2026-06-30
---

## Definition
An architectural pattern where deterministic analysis produces structured data that is then fed to an LLM whose sole job is to translate that structured information into natural language — the LLM is not asked to reason about the domain, only to articulate pre-computed findings.

## Key Information
- Core insight from the Play Magnus chess coach: LLMs can do many things but if you need high accuracy and low latency, separate the data pipeline from language generation
- In the chess domain: Stockfish provides ground truth analysis, detectors extract tactical/positional patterns, Maya predicts human move difficulty — all deterministic or model-based computation
- The LLM's role is strictly to translate this structured data (JSON) into natural language commentary — it is explicitly not asked to figure out chess on its own because that leads to hallucination
- Everything is "grounded in the information that we give it" — the LLM does not reason about chess positions independently
- Benefits: reduces hallucination, improves accuracy, enables lower latency (no reasoning tokens needed), makes quality predictable and debuggable
- The initial context extraction model is a slow, painful process: starts as a large JSON file that is progressively pruned as quality improves
- Anant Dole listed this as the number one learning: "really important to separate that sort of data pipeline from the language generation"

## Related
- [[Chess Context Extraction]] — the specific detectors and context engine for chess
- [[LLM Hallucination In Chess]] — the problem this pattern solves
- [[Grounding LLM in Structured Data]] — broader concept
- [[Latency vs Quality Trade-offs]] — this separation enables low-latency while maintaining quality
- [[Play Magnus]] — applied this pattern in production
- [[Stockfish]] — deterministic analysis layer
- [[Maya]] — human behavior prediction layer
- [[Gemini 3 Flash]] — the LLM translation layer
- [[summary-20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take]] — source
