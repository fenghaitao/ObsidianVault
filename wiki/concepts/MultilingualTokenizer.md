---
title: "MultilingualTokenizer"
type: concept
tags: [tokenization, multilingual, gemma, gemini]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
A multilingual tokenizer is a tokenization system designed from the ground up for multilingual use cases, as exemplified by Gemma 4's Gemini-based tokenizer trained on 140+ languages, which enables effective fine-tuning even for low-resource languages independently of the model's raw capabilities.

## Key Information
- Gemma 4 uses a tokenizer based on Gemini, inheriting all multilingual research that powers Gemini
- Trained with over 140 languages
- Designed for multilingual use cases from the start, not retrofitted
- Enables fine-tuning for low-digital-resource languages (e.g., Quechua, indigenous languages, Indian official languages)
- Tokenizer quality matters independently of model capabilities — good tokenization enables effective training even on limited data
- Combined with multimodal capabilities, enables tasks like explaining images with Japanese text
- Key enabler for the Gemma community ecosystem: AI Singapore (Southeast Asian languages), Sarvam (Indian languages)

## Related
- [[Gemma4]] — model using this tokenizer
- [[Tokenization]] — general concept
- [[SovereignAI]] — use case enabled by multilingual tokenization
- [[summary-20260420 - Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind]] — source
