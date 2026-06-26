---
title: "MemoryLayers"
type: concept
tags: [fine-tuning, architecture, llm, knowledge-injection]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is.md"]
last_updated: 2026-06-25
---

## Definition
Memory layers are a parameter-efficient fine-tuning technique that adds a large differentiable lookup table (similar to an expert in a mixture-of-experts model) to the MLP layer of a transformer. They allow controlled knowledge injection by specifying exactly which parts of the memory get updated.

## Key Information
- Function as a "giant differentiable lookup table" added to the transformer's MLP layer
- Key advantage: controllable — you can specify exactly which parts of the memory layer get updated, keeping changes minimal
- Justin Lin's research showed memory layers "basically don't forget at all" while learning close to as much as full fine-tuning
- On the learning-vs-forgetting trade-off axes, memory layers outperform LoRA, prefix tuning, and full fine-tuning
- Jack Morris considers them potentially the best approach when preserving base model knowledge is critical
- Part of the broader parameter-efficient fine-tuning family alongside LoRA and prefix tuning

## Related
- [[summary-20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is]] — source
- [[JustinLin]] — primary researcher
- [[ParameterEfficientFineTuning]] — broader category
- [[CatastrophicForgetting]] — the problem they solve
- [[LoRA]] — alternative PEFT method
- [[PrefixTuning]] — alternative PEFT method
