---
title: "Gemini 3 Flash"
type: entity
tags: [model, llm, google, gemini, flash]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take.md"]
last_updated: 2026-06-30
---

## Definition
Gemini 3 Flash is a fast variant of Google's Gemini 3 model used by Play Magnus for generating chess commentary. It was selected for its low latency (~1 second time-to-first-token, ~3 seconds end-to-end) while achieving ~75% accuracy on chess evaluation scenarios.

## Key Information
- Time to first token typically about 1 second; end-to-end latency averaging about 3 seconds
- Meets the Play Magnus team's sub-3 second target for consumer-facing chess commentary
- Achieves approximately 75% accuracy on their 16 chess evaluation scenarios
- Compared against Claude (with more thinking, ~60% accuracy but much higher latency) and GPT-5 Mini (lower accuracy)
- The team continuously re-evaluates as new models are released, using Open Router for easy swapping
- Suitable for instant game review but not for future "chat with coach" features where users may tolerate longer latency

## Related
- [[Play Magnus]] — uses Gemini 3 Flash for commentary generation
- [[Gemini3]] — the full Gemini 3 model family
- [[Open Router]] — used to compare Gemini 3 Flash against other models
- [[Latency vs Quality Trade-offs]] — Gemini 3 Flash chosen for latency over quality
- [[LLM Hallucination In Chess]] — still an issue even at 75% accuracy
- [[summary-20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take]] — source
