---
title: "Video Action Language Models"
type: concept
tags: [model-type, multimodal, vision, web-navigation, agent]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum.md"]
last_updated: 2026-06-30
---

## Definition
Video Action Language Models (VALMs) are multimodal models that process video input and produce actions, used for visual web navigation tasks. [[Callosum]] demonstrated that a heterogeneous mixture of open and closed VALMs outperforms any single model, beating GPT-5.2 by 18% and Gemini 2.5 by 25% on Video Web Arena.

## Key Information
- Used for visual web navigation: understanding web pages visually and taking actions
- Problem is inherently heterogeneous: decomposes into visual reasoning and textual reasoning sub-tasks
- [[Callosum]] used a mixture of open and closed VALMs, mapping subtasks to appropriately-sized models
- Simple subtasks (e.g., zooming) offloaded to less intelligent/cheaper models: 11x faster and 43x cheaper than using ChatGPT alone for those subtasks
- Mixture of Quant 3 VL8B-Instruct + Kimi K2.5: 1.3x faster than Kimi alone, 18x cheaper than GPT-5.2 alone
- Mixture of Quant 3 + GPT: 3x faster and 3.7x cheaper
- Demonstrates heterogeneous approach shifting the [[Pareto Frontier]] beyond singular models

## Related
- [[Heterogeneous Intelligence]] — paradigm enabling VALM mixtures
- [[Callosum]] — company that demonstrated heterogeneous VALM composition
- [[Pareto Frontier]] — shifted by heterogeneous VALM mixtures
- [[summary-20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum]] — source
