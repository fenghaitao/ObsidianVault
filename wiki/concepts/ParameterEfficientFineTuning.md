---
title: "ParameterEfficientFineTuning"
type: concept
tags: [fine-tuning, training, llm, efficiency]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is.md"]
last_updated: 2026-06-25
---

## Definition
Parameter-Efficient Fine-Tuning (PEFT) refers to methods that update only a small subset of a model's parameters during fine-tuning, rather than the entire model. This preserves base model knowledge while enabling domain-specific adaptation, and makes per-user model serving economically feasible.

## Key Information
- Key methods include: LoRA (low-rank adaptation matrices), prefix tuning (training KV cache), memory layers (differentiable lookup tables), and mixture-of-experts extensions
- The core principle: keep the giant base model unchanged and add a tiny controllable component
- Enables serving one model per user at scale — base model is shared, only small adapters are user-specific
- Thinking Machines' Tinker API is built entirely around this concept, batching LoRA inference
- Trade-off: PEFT methods learn less than full fine-tuning but also forget less
- RL (reinforcement learning) requires far fewer trainable parameters than SFT (supervised fine-tuning) — as few as 14 parameters for 91% accuracy on math reasoning
- Prefix tuning is well-supported in existing systems due to KV cache infrastructure; LoRA requires custom kernels for batched serving
- The choice between methods (LoRA vs. prefix tuning vs. memory layers) remains unresolved with conflicting evidence

## Related
- [[summary-20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is]] — source
- [[LoRA]] — most popular PEFT method
- [[PrefixTuning]] — KV cache-based method
- [[MemoryLayers]] — lookup table-based method
- [[CatastrophicForgetting]] — the problem PEFT mitigates
- [[ThinkingMachines]] — company scaling PEFT
