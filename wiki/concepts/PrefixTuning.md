---
title: "PrefixTuning"
type: concept
tags: [fine-tuning, kv-cache, llm, training]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is.md"]
last_updated: 2026-06-25
---

## Definition
Prefix tuning is a parameter-efficient fine-tuning method that trains the KV (key-value) cache of a transformer rather than the model weights themselves. It is well-supported in existing infrastructure due to the widespread use of KV caches.

## Key Information
- Instead of updating model weights, prefix tuning trains the KV cache entries
- Well-supported in existing systems because KV caches are commonly used and system infrastructure is built around them
- Some research (cited by Jack Morris) shows prefix tuning works much better than LoRA; Meta researchers claim the opposite
- Jack Morris considers it a "pretty good candidate" for knowledge injection due to KV cache infrastructure support
- Unlike LoRA, prefix tuning doesn't require custom kernels for batched training/inference
- Part of the parameter-efficient fine-tuning family

## Related
- [[summary-20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is]] — source
- [[ParameterEfficientFineTuning]] — broader category
- [[LoRA]] — alternative PEFT method
- [[MemoryLayers]] — alternative PEFT method
- [[CatastrophicForgetting]] — the problem it mitigates
