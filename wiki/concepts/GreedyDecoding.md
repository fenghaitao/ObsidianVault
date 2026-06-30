---
title: "GreedyDecoding"
type: concept
tags: [inference, llm, decoding, generation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
Greedy decoding is an inference strategy that always selects the highest-probability token at each generation step. While it works well for deterministic tasks like transcription (where there's only one correct output), it makes LLMs boring and uncreative — Angelos Perivolaropoulos stated you should "pretty much never use greedy decoding for LLMs."

## Key Information
- Always picks the token with the highest probability from the model's output distribution
- Example: if token T has 80% probability and token H has 15%, greedy always picks T
- Works well for transcription models where there's only one correct output
- Makes LLMs "very boring and not very creative in what they generate"
- "Pretty much never want to use greedy decoding for LLMs" — Angelos Perivolaropoulos
- For generative LLMs, temperature-based sampling produces better, more natural results
- Can cause repetitive loops and lack of diversity in generated text
- The workshop used temperature + top-K sampling instead of greedy decoding

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[TemperatureInAI]] — preferred alternative for LLMs
- [[TopKSampling]] — combined with temperature for better generation
- [[DeterministicVsStochasticSampling]] — broader concept
- [[LLMTrainingFromScratch]] — workshop context
