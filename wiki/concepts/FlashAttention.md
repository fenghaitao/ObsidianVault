---
title: "FlashAttention"
type: concept
tags: [optimization, attention, kernel, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Low Level Technicals of LLMs： Daniel Han.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero.md"]
last_updated: 2026-06-26
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
- [[SelfAttentionMechanism]] — the computation FlashAttention optimizes
- [[Triton]] — kernel language for custom attention implementations

- **GPU memory hierarchy**: On-chip memory (~30 TB/s) vs off-chip memory (~10x slower); FlashAttention keeps computation in on-chip memory by processing attention in blocks
- **ModernBERT synergy**: Combined with alternating attention, FlashAttention reduced fine-tuning memory requirements by ~70%
- **Key insight**: The bottleneck is memory transfers between GPU memory levels, not floating-point operations