---
title: "SequencePacking"
type: concept
tags: [efficiency, training, optimization, transformer, batching]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero.md"]
last_updated: 2026-06-26
---

## Definition

Sequence packing is an efficiency technique that concatenates the semantic tokens of multiple input sequences to fill the full context window, processing them in a single forward pass with masking attention to prevent cross-sequence contamination. It eliminates the wasted computation on padding tokens that occurs in traditional fixed-length batching.

## Key Information

- **Problem**: Traditional batching pads all sequences to the length of the longest one, wasting up to 50% of computation on meaningless padding tokens (as measured on the Wikipedia dataset used to train original BERT)
- **Unpadding**: Remove all padding tokens before they enter the embedding layer
- **Packing**: Concatenate semantic tokens from multiple sequences until the context window (8192 tokens in ModernBERT) is filled; only add padding at the end if truly needed
- **Masking attention**: Critical implementation detail — ensures tokens only attend to other tokens from the same original sequence, preventing cross-sequence information leakage
- **Single forward pass**: The packed sequence becomes a single batch, allowing all original sequences to be processed in one forward pass
- **Production benefit**: Efficiently handles the heterogeneous input sizes expected in real-world safety check pipelines

## Related

- [[summary-20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero]] — source
- [[ModernBERT]] — model using this technique
- [[AlternatingAttention]] — complementary efficiency technique
- [[FlashAttention]] — complementary hardware optimization
