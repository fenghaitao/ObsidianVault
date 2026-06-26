---
title: "LoRA"
type: concept
tags: [fine-tuning, training, llm, efficiency]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is.md"]
last_updated: 2026-06-25
---

## Definition
LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning technique that trains small low-rank matrices to adapt the linear layers of a pre-trained model. It is the most popular PEFT method, enabling per-user model customization with minimal storage and compute overhead.

## Key Information
- Trains small matrices (e.g., 10M parameters for a 10B parameter model) that control the base model's behavior
- "Learns less and forgets less" compared to full fine-tuning — a deliberate trade-off that preserves base capabilities
- Thinking Machines built their entire Tinker API around scaling LoRA for per-user model serving
- For RL (reinforcement learning), LoRA can be about as good as full fine-tuning due to sparse reward signals
- For SFT (supervised fine-tuning), LoRA has lower capacity than full fine-tuning
- Extreme variants exist: "tiny LoRA" can train as few as 14 parameters and achieve 91% accuracy on GSM8K math reasoning with RL
- Even 1 parameter can yield 5% improvement through random projections controlled by a single number
- Batching LoRA inference requires custom kernels not yet available in open source

## Related
- [[summary-20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is]] — source
- [[ParameterEfficientFineTuning]] — broader category
- [[ThinkingMachines]] — company scaling LoRA
- [[PrefixTuning]] — alternative PEFT method
- [[MemoryLayers]] — alternative PEFT method
- [[CatastrophicForgetting]] — the problem it mitigates
