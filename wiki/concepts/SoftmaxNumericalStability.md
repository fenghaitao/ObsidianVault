---
title: "SoftmaxNumericalStability"
type: concept
tags: [numerical-methods, attention, training, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Low Level Technicals of LLMs： Daniel Han.md"]
last_updated: 2026-06-26
---

## Definition
The softmax numerical stability trick subtracts the maximum value from each row of the attention score matrix before applying the exponential function, preventing any single large value from dominating the softmax distribution and causing training instability.

## Key Information
- **Problem**: Without stabilization, a large attention score produces exp(large) which dominates the sum of exponentials in the softmax denominator, making all other probabilities approach zero
- **The trick**: Subtract the row maximum from each element before exponentiation: softmax(x_i) = exp(x_i - max(x)) / Σexp(x_j - max(x))
- **Effect**: Ensures the largest exponentiated value is always exp(0) = 1, keeping all values in a reasonable range
- **Training impact**: Without this trick, the model effectively stops learning because only one token's probability matters, destroying gradient flow
- **Used in**: Standard practice across all attention mechanism implementations (HuggingFace, DeepMind, Keras, etc.)

## Related
- [[summary-20240731 - Low Level Technicals of LLMs： Daniel Han]] — source
- [[SelfAttentionMechanism]] — the attention mechanism using this trick
- [[LLMImplementationAnalysis]] — comparison across implementations checking for this
