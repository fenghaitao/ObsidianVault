---
title: "CharacterLevelTokenization"
type: concept
tags: [tokenization, nlp, llm, training]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
Character-level tokenization is the simplest form of tokenization where each unique character in the training data becomes a separate token. In Angelos Perivolaropoulos's workshop, the Shakespeare dataset had only 65 unique characters, resulting in a vocabulary of just 65 tokens — making training feasible with limited data but limiting the model's ability to understand word-level relationships.

## Key Information
- Each unique character becomes a separate token; the Shakespeare dataset had 65 unique characters
- Results in only 4,225 possible bigrams (65²), making it feasible to train with limited data
- The model needs to see as many bigrams as possible during training; with 200K tokens you'd need 200K² data points
- Trade-off: character-level tokenizers don't scale well because models struggle to understand correlations between individual characters vs. whole words
- Example: "The sky is blue" as words is easy to correlate, but "T-H-E S-K-Y I-S B-L-U-E" as characters is much harder for attention to capture
- Makes inference expensive because many tokens are needed per word
- May never converge to good results for large-scale models
- Used in the workshop because it's the easiest approach for a small model with limited data
- For production models, Byte-Pair Encoding (BPE) is the standard alternative

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[Tokenization]] — general concept
- [[BytePairEncoding]] — production alternative
- [[LLMTrainingFromScratch]] — workshop context
