---
title: "ThinkingMachines"
type: entity
tags: [company, fine-tuning, lora, training-api]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is.md"]
last_updated: 2026-06-25
---

## Definition
Thinking Machines is a company building Tinker, a training API that enables serving one fine-tuned model per user by batching LoRA adapters. Their architecture is predicated on the idea that parameter-efficient methods allow personalized models at scale without duplicating the base model.

## Key Information
- Tinker API enables per-user model serving through batched LoRA inference
- The base model is shared across all users; only small LoRA adapters are user-specific
- Training and inference can be done with "basically no cost" because the base model doesn't change
- Their research shows LoRA is about as good as full fine-tuning when using RL (reinforcement learning)
- Designing their entire organization around scaling LoRA, which is complex and not yet feasible in open source

## Related
- [[summary-20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is]] — source
- [[LoRA]] — the technique they scale
- [[ParameterEfficientFineTuning]] — the broader category
