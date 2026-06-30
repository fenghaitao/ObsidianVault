---
title: "LayerNorm"
type: concept
tags: [architecture, training, stability, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Low Level Technicals of LLMs： Daniel Han.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-26
---

## Definition
Layer Normalization (LayerNorm) is a normalization technique that stabilizes LLM training by normalizing each row of activations — squaring elements, summing them, dividing by the square root, taking the mean, and multiplying by learned weight vectors — to keep values in a stable numerical range across many layers.

## Key Information
- **Purpose**: Prevents activation values from diverging (exploding to infinity or vanishing to zero) across 32+ transformer layers by rescaling to a stable range
- **Computation**: For each row of the input matrix X, compute the row sum of squares, take the mean, divide by that, then multiply by learned weight vector W
- **Training stability**: The primary reason for LayerNorm is training stability — it makes optimization converge more reliably, with no deeper semantic meaning
- **Placement rule**: Daniel Han recommends "LayerNorms everywhere" — before attention, after attention, after MLP blocks, after inputs. More LayerNorms always improve stability at the cost of slightly slower training
- **Residual connections**: LayerNorm is typically paired with residual connections (save state before LN, apply LN, add back residual) for further stability
- **Ordering**: Whether LayerNorm comes before or after attention/MLP blocks has minimal impact (≈0.01% accuracy difference); both orders work
- **Forward kernel**: Writing the forward pass in Triton is straightforward (few computation lines, mostly data loading)
- **Backward kernel**: Differentiation through LayerNorm is significantly complex due to derivatives through row sums and normalization — much harder than the forward pass
- **Numerical divergence**: Without LayerNorm, a value of 2 multiplied by 2 through 32 layers becomes approximately 2^32, exceeding float32 range; LayerNorm divides it back to ~1 each layer

## Related
- [[summary-20240731 - Low Level Technicals of LLMs： Daniel Han]] — source
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source (prevents activation explosion across layers)
- [[SelfAttentionMechanism]] — attention blocks wrapped in LayerNorm
- [[Triton]] — GPU kernel language for writing LayerNorm operations
- [[BatchNormalization]] — related technique, reduces internal covariate shift
- [[ResidualConnections]] — paired stability mechanism
