---
title: "BERT"
type: entity
tags: [model, encoder, nlp, google, transformer]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero.md"]
last_updated: 2026-06-26
---

## Definition

BERT (Bidirectional Encoder Representations from Transformers) is Google's original bidirectional encoder model that processes text by attending to all tokens in an input sequence simultaneously. It uses global self-attention with quadratic complexity and was originally limited to 512-token context windows with absolute positional encodings.

## Key Information

- Original BERT used global attention where all tokens attend to all tokens, creating O(n²) complexity
- Context window limited to 512 tokens (about half a page to one page)
- Used absolute positional encodings: fixed position index vectors added to token embeddings, which entangles position with token semantics and limits context to training size
- Padding-based batching wasted up to 50% of computation on meaningless padding tokens
- ModernBERT is the advanced successor addressing these limitations

## Related

- [[summary-20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero]] — source
- [[ModernBERT]] — advanced successor model
- [[EncoderModels]] — model class
- [[AlternatingAttention]] — improvement over BERT's global-only attention
