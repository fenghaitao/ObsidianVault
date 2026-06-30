---
title: "GPT-3"
type: entity
tags: [model, llm, openai, transformer]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
GPT-3 is a large language model released by OpenAI that, like GPT-2, was built on the same fundamental transformer architecture — just with more data and a bigger model. Angelos Perivolaropoulos referenced it to illustrate that the code shown in his workshop (a few hundred lines) is essentially what powered GPT-2 and GPT-3.

## Key Information
- Built on the same fundamental transformer architecture as GPT-2, just scaled up with more data and parameters
- The code that powered GPT-3 is essentially the same few hundred lines of transformer implementation shown in the workshop
- GPT-3.5 had a 16K context size; researchers then worked on scaling to 1M context, which required architectural changes beyond just increasing the block_size parameter
- The workshop illustrates that even state-of-the-art models are built on the same core principles taught in the session

## Related
- [[GPT-2]] — predecessor, same fundamental architecture
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[TransformerArchitecture]] — underlying architecture
- [[LLMTrainingFromScratch]] — workshop context
