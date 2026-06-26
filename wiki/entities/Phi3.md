---
title: "Phi3"
type: entity
tags: [model, microsoft, llm, small-model, fine-tuning]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han.md"]
last_updated: 2026-06-26
---

## Definition

Phi-3 is Microsoft's small language model that has several known issues affecting fine-tuning quality, including an incorrect sliding window size and a pad/EOS token conflict that causes infinite generations.

## Key Information

- **Sliding Window Bug**: The sliding window should be 2048, not 2047 — an off-by-one error in the original implementation
- **Pad/EOS Token Conflict**: By default, Phi-3 uses the same token for both padding and end-of-sequence, which causes infinite generations during fine-tuning because the EOS token gets masked during loss calculation
- **QKV Fusion Issue**: The q, k, v matrices should be unfused for LoRA fine-tuning, otherwise LoRA tuning will not work optimally
- **Common Fine-Tuning Target**: Frequently used as a fine-tuning base model

## Related

- [[summary-20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han]] — source
- [[Microsoft]] — company behind Phi-3
- [[PadTokenEOSTokenConflict]] — infinite generation bug
- [[Unsloth]] — tool that automatically fixes Phi-3 bugs
- [[SlidingWindowAttention]] — attention mechanism used in Phi-3
- [[LoRA]] — fine-tuning method requiring unfused QKV matrices
