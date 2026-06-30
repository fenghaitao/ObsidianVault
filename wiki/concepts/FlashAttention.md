---
title: "FlashAttention"
type: concept
tags: [optimization, attention, kernel, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Low Level Technicals of LLMs： Daniel Han.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow.md"]
last_updated: 2026-06-29
---

## Definition
FlashAttention is an optimized attention kernel implementation that computes the softmax(QK^T/√d)V operation more efficiently than standard PyTorch attention, serving as a drop-in replacement that model code can simply ignore when reading architecture.

## Key Information
- A faster, native PyTorch version of scaled dot-product attention that replaces standard attention computation
- When reading model architecture code, FlashAttention-specific code paths should be ignored — they are optimization details, not architectural decisions
- The optimization primarily addresses the memory bottleneck of materializing the full attention matrix (QK^T) which is O(n²) in sequence length
- Related to Triton kernel programming for writing custom attention implementations
- NVIDIA's scaled_dot_product_attention is the PyTorch-native equivalent

## Related
- [[summary-20240731 - Low Level Technicals of LLMs： Daniel Han]] — source
- [[summary-20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow]] — source (vision impact)
- [[SelfAttentionMechanism]] — the computation FlashAttention optimizes
- [[Triton]] — kernel language for custom attention implementations
- [[Hera]] — vision model whose speed advantage FlashAttention eliminated
- [[ViT (Vision Transformer)]] — benefited from FlashAttention speedups

- **GPU memory hierarchy**: On-chip memory (~30 TB/s) vs off-chip memory (~10x slower); FlashAttention keeps computation in on-chip memory by processing attention in blocks
- **ModernBERT synergy**: Combined with alternating attention, FlashAttention reduced fine-tuning memory requirements by ~70%
- **Key insight**: The bottleneck is memory transfers between GPU memory levels, not floating-point operations
- **Vision impact**: FlashAttention from the LLM world eliminated the speed advantage of architectures like Hera that reduced attention complexity for vision, making plain ViT competitive again