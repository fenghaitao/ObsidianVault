---
title: "Open Router"
type: entity
tags: [api, gateway, llm, evaluation, infrastructure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take.md"]
last_updated: 2026-06-30
---

## Definition
Open Router is an API gateway that provides unified access to multiple LLM providers, enabling easy model swapping and comparison. The Play Magnus team uses it to benchmark different models for their chess commentary generation.

## Key Information
- Used by Play Magnus to run the same chess evaluation scenarios across different models (Gemini, Claude, GPT-5) without changing integration code
- Enables rapid model comparison as new models are released "so fast so frequently"
- The team runs 16 chess evaluation scenarios through Open Router, comparing models on accuracy, latency, and hallucination rates
- Simplifies the workflow of testing new model versions as they become available

## Related
- [[Play Magnus]] — uses Open Router for model evaluation
- [[Gemini 3 Flash]] — one of the models evaluated via Open Router
- [[LLMAsJudge]] — evaluation technique used with Open Router-routed models
- [[summary-20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take]] — source
