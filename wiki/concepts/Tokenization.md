---
title: "Tokenization"
type: concept
tags: [nlp, preprocessing, llm, encoding]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Low Level Technicals of LLMs： Daniel Han.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-26
---

## Definition
Tokenization is the process of splitting text into discrete tokens (subwords, characters, or words) and assigning each a numerical ID so that language models — which only understand numbers — can process text input. It is foundational to all LLM pipelines but is also a persistent source of bugs and inconsistencies across implementations.

## Key Information
- **Industry standard algorithms**: Byte-Pair Encoding (BPE) and WordPiece build token vocabularies by starting from individual characters and merging them based on co-occurrence statistics
- **Simple tokenizer example**: Treating punctuation as combined with words and ignoring spaces produces a trivial tokenizer with fundamental problems (separate tokens for "hello" vs "hello,")
- **Punctuation handling**: Whether punctuation is combined with words or separated is a key design decision that varies across implementations
- **Stemming**: Reducing words to roots (e.g., "skipping" → "skip") is a classical NLP technique that can reduce vocabulary size
- **Lowercasing**: Converting all text to lowercase reduces vocabulary but loses information about sentence boundaries (capitalized words often mark sentence starts)
- **Implementation inconsistencies**: Different model variants from the same provider (e.g., Mistral, Mixtral, Llama family) produce different tokenization results for identical input due to fast vs. slow tokenizer implementations
- **Pre-inference failure**: Tokenizer bugs break the pipeline before training or inference even begins — the model receives wrong token IDs and produces garbage regardless of architecture quality
- **Numerical mapping**: Each unique token receives an integer ID; the model operates on these IDs, not on text directly

## Related
- [[summary-20240731 - Low Level Technicals of LLMs： Daniel Han]] — source
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source (character-level vs BPE, tokenizer trade-offs)
- [[LLMImplementationAnalysis]] — methodology for finding tokenizer inconsistencies
- [[Mistral]] — company with known tokenizer inconsistencies across model variants
- [[DanielHan]] — researcher who analyzed tokenization issues
- [[CharacterLevelTokenization]] — simplest approach, used in the workshop
- [[BytePairEncoding]] — production standard for LLM tokenization
- [[EmbeddingLayer]] — converts token IDs to vectors
