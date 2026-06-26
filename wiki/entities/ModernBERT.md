---
title: "ModernBERT"
type: entity
tags: [model, encoder, bert, nlp, classification, open-source]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero.md"]
last_updated: 2026-06-26
---

## Definition

ModernBERT is an advanced version of the BERT encoder model incorporating architectural improvements including alternating attention, rotary positional encoding (RoPE), flash attention, unpadding with sequence packing, and a deep-and-narrow design. It comes in base (22 layers, ~150M parameters) and large (28 layers, 1024 hidden dimensions) versions.

## Key Information

- **Alternating attention**: Two local attention layers with 128-token sliding window followed by one global attention layer with 8192 tokens, reducing memory requirements by ~70% when combined with FlashAttention
- **Unpadding and sequence packing**: Eliminates wasted computation on padding tokens (up to 50% in original BERT) by concatenating semantic tokens to fill the context window
- **Deep-and-narrow architecture**: 22 layers (base) or 28 layers (large) with narrow hidden dimensions, determined by systematic grid search balancing task performance and inference speed
- **RoPE**: Uses different rotation speeds for local (faster) and global (slower) attention to avoid completing full cycles that would make distant tokens appear close
- **FlashAttention**: Processes attention in blocks within on-chip GPU memory (~30 TB/s) rather than materializing the full attention matrix in slower off-chip memory
- **Other improvements**: GeLU activation, bias terms disabled except in final decoder, normalization layer after embedding, dimensions aligned with tensor ops (multiples of 64), BF16 training support
- **Vocabulary**: ~50,000 tokens using a modified byte-pair encoding (BPE) with CLS and SEP special tokens
- **Context window**: Up to 8192 tokens, handling approximately 10-20 pages per safety check

## Related

- [[summary-20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero]] — source
- [[BERT]] — predecessor model
- [[EncoderModels]] — model class
- [[AlternatingAttention]] — key architectural innovation
- [[RoPE]] — positional encoding used
- [[FlashAttention]] — hardware optimization used
- [[SequencePacking]] — efficiency technique used
- [[CLSToken]] — classification token
