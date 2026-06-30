---
title: "Hardware Lottery"
type: concept
tags: [ai-research, hardware, bias, optimization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs.md"]
last_updated: 2026-06-30
---

## Definition
The hardware lottery is the thesis, articulated by Sarah Hooker, that AI research directions succeed or fail based on compatibility with available hardware rather than theoretical merit, leaving many promising approaches unexplored due to hardware inertia.

## Key Information
- Coined by Sarah Hooker (formerly Google Brain, Cohere)
- The current hardware stack (Nvidia GPUs) was primarily built around training, creating bias toward training-compatible research
- Many ideas remain unexplored because they don't fit well with current hardware — creating "low-hanging fruit" for inference-specific optimization
- Alex Cheema cites this as foundational to EXO Labs' thesis: there are massive untapped gains in inference-specific hardware and software
- Example given: Qwen 3.5 running 50% slower than theoretical maximum on Apple Silicon due to inefficient kernel launches, fixed with basic kernel fusion for 30% improvement
- Implies that the "best" research is not necessarily the most correct but the most compatible with current hardware economics

## Related
- [[summary-20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs]] — source
- [[Sarah Hooker]] — originator of the concept
- [[Full-Stack Co-Design]] — approach that overcomes the hardware lottery
- [[EXO Labs]] — cites this concept as foundational
