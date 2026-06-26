---
title: "AlternatingAttention"
type: concept
tags: [architecture, attention, efficiency, transformer, modernbert]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero.md"]
last_updated: 2026-06-26
---

## Definition

Alternating attention is a transformer architecture pattern that combines local sliding-window attention layers with periodic global attention layers, mimicking how humans switch between focused reading (a page) and linking information to broader context (the whole story). It reduces the quadratic complexity of full self-attention while preserving the ability to capture long-range dependencies.

## Key Information

- **Local attention layers**: Each token attends to 64 tokens on the left and 64 on the right (128-token sliding window), capturing locally concentrated patterns like gibberish suffix attacks and short prompt injections
- **Global attention layers**: Every third layer uses full attention across up to 8192 tokens, capturing long-range patterns like creative writing generation, MCP tool descriptions, and agentic plans
- **Memory savings**: Combined with FlashAttention, reduces memory requirements for fine-tuning by approximately 70% compared to full global attention
- **ModernBERT implementation**: 2 local layers followed by 1 global layer, repeated; RoPE rotation speeds differ between local (faster) and global (slower) to avoid completing full cycles
- **Design intuition**: Many attack patterns are locally concentrated, but some require understanding of longer context — alternating attention handles both without forcing truncation or explicit input segmentation

## Related

- [[summary-20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero]] — source
- [[ModernBERT]] — model using this architecture
- [[SlidingWindowAttention]] — the local attention mechanism
- [[FlashAttention]] — complementary optimization
- [[RoPE]] — positional encoding with different rotation speeds per attention type
