---
title: "SelfAttentionMechanism"
type: concept
tags: [architecture, attention, llm, transformer]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Low Level Technicals of LLMs： Daniel Han.md"]
last_updated: 2026-06-26
---

## Definition
The self-attention mechanism is the core computation in transformer-based LLMs, computing softmax(QK^T/√d)V where Q, K, and V are learned projections of the input, enabling each token to attend to all other tokens in the sequence.

## Key Information
- **Formula**: softmax(QK^T/√d)V — projects input into Query, Key, and Value matrices, computes attention scores via dot products, scales by √d (model dimension), applies softmax for probability distribution, and weights Value vectors
- **Q, K, V projections**: Input is multiplied by learned weight matrices W_Q, W_K, W_V to produce Query, Key, and Value representations
- **Scaling factor (√d)**: Dividing by the square root of the head dimension prevents dot products from growing too large and pushing softmax into regions with tiny gradients
- **Bottleneck**: The softmax is the computational bottleneck because the row sum of exponentials cannot be decomposed — matrix multiplications cannot be pulled outside the softmax, making it harder to optimize with pure matrix math
- **Numerical stability**: The standard trick is to subtract the maximum value from each row before applying exp, preventing one large value from dominating the softmax distribution
- **Repeat-KV optimization**: For inference, key and value heads can be trained in small slices and repeated (e.g., 4 times) to reduce memory with minimal accuracy loss
- **Implementation comparison**: Differences in attention implementations across frameworks (DeepMind, HuggingFace, Keras) are a primary source of bugs in open-source models

## Related
- [[summary-20240731 - Low Level Technicals of LLMs： Daniel Han]] — source
- [[SoftmaxNumericalStability]] — the subtract-max trick for stable attention
- [[RoPE]] — positional embeddings applied to Q and K before attention
- [[LayerNorm]] — normalization applied before/after attention blocks
- [[FlashAttention]] — optimized kernel replacing standard attention
- [[GroupedQueryAttention]] — attention variant sharing KV across query heads
- [[MultiQueryAttention]] — extreme variant with single KV head shared across all queries
- [[RepeatKV]] — inference optimization for KV cache
