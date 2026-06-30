---
title: "TopKSampling"
type: concept
tags: [inference, llm, decoding, generation, sampling]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
Top-K sampling is an inference technique that restricts token selection to only the K most probable tokens, then samples among them using temperature. This prevents the model from ever selecting very unlikely tokens — even if temperature-based randomness would otherwise hit them — improving generation quality and stability.

## Key Information
- Restricts the sampling pool to only the K most probable tokens at each step
- Prevents the model from selecting very unlikely tokens that temperature might randomly hit
- Example: if 5 tokens are reasonable and the 6th is nonsensical, top-K prevents the 6th from ever being selected
- Used in combination with temperature sampling for best results
- Temperature controls randomness within the top-K set; top-K controls which tokens are eligible
- Helps prevent the model from going into "weird loops" or generating nonsense
- Also helps prevent accidentally hitting an end-of-text token and stopping generation prematurely
- The workshop's inference function combined temperature, top-K, and softmax for generation

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[TemperatureInAI]] — used in combination with top-K
- [[GreedyDecoding]] — simpler alternative (not recommended for LLMs)
- [[DeterministicVsStochasticSampling]] — broader concept
- [[LLMTrainingFromScratch]] — workshop context
