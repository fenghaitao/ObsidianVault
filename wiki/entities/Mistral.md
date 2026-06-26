---
title: "Mistral"
type: entity
tags: [company, llm, open-source, ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Low Level Technicals of LLMs： Daniel Han.md"]
last_updated: 2026-06-26
---

## Definition
Mistral AI is a French AI company producing open-source language models. Their model family (Mistral, Mixtral, and Llama variants) exhibits tokenizer inconsistencies across different releases due to varying use of fast vs. slow tokenization implementations.

## Key Information
- Different Mistral model variants produce different tokenization results for the same input text
- The "sun smiley face" tokenization example demonstrates that models from the Mistral family tokenize the same character differently depending on the variant
- According to the HuggingFace team, some of these inconsistencies are correct tokenizer choices while others are bugs where the Mistral team forgot to update models to the fast tokenization variant
- Tokenizer issues exist even before training or inference begins, breaking the pipeline before the model is even loaded

## Related
- [[summary-20240731 - Low Level Technicals of LLMs： Daniel Han]] — source
- [[Tokenization]] — the broader concept of tokenizer inconsistencies
- [[DanielHan]] — researcher who analyzed these inconsistencies
- [[LLMImplementationAnalysis]] — methodology for finding such issues
