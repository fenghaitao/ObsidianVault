---
title: "CLSToken"
type: concept
tags: [architecture, classification, encoder, transformer, nlp]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero.md"]
last_updated: 2026-06-26
---

## Definition

The CLS (classification) token is a special token placed at the beginning of an input sequence in encoder models. As it passes through each transformer layer, it progressively accumulates contextual information from the entire sequence via the bidirectional attention mechanism, ultimately serving as a dense representation of the full input for downstream classification tasks.

## Key Information

- Placed at the beginning of every input sequence; paired with a SEP (separator) token at the end
- Refined across all layers: in ModernBERT-base (22 layers) or ModernBERT-large (28 layers), each layer captures a different level of semantic abstraction
- The final CLS token representation is fed into a classification head (feedforward layer) to produce predictions (e.g., safe/unsafe)
- For very long sequences, mean pooling (averaging all token representations) can be used as an alternative to CLS pooling
- The SEP token is primarily relevant for next-sentence-prediction tasks and is less important for pure classification use cases
- The CLS token mechanism is what enables encoder models to achieve 35ms classification latency — the entire context is condensed into a single vector in one forward pass

## Related

- [[summary-20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero]] — source
- [[EncoderModels]] — model class using CLS tokens
- [[ModernBERT]] — model with 22-28 layer CLS token refinement
- [[BERT]] — original model introducing the CLS token
