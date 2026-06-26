---
title: "Thinking Levels"
type: concept
tags: [gemini, reasoning, configuration, token-budget]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Thinking Levels are configurable reasoning depth settings (minimal, low, medium, high) available in Gemini 3.1 models that control how many tokens the model spends on planning and reasoning before generating a response.

## Key Information
- Available for all Gemini 3.1 series models in AI Studio
- Four levels: minimal, low, medium, high
- Higher thinking levels cause the model to spend more tokens on planning and reasoning
- Paige Bailey recommends minimal or low for time-sensitive tasks
- High thinking level demonstrated for complex tasks like SVG generation from images
- Higher thinking = more tokens consumed = higher cost but potentially better results for complex tasks
- Configurable in the thinking config section of AI Studio

## Related
- [[summary-20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind]] — source
- [[AI Studio]] — platform where it's configurable
- [[Gemini 3.1 Pro]] — model supporting thinking levels
- [[ReasoningBudgets]] — related concept
- [[ChainOfThought]] — related reasoning technique
