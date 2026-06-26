---
title: "GradientOffloading"
type: concept
tags: [training, fine-tuning, memory, optimization, long-context]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han.md"]
last_updated: 2026-06-26
---

## Definition

Gradient offloading is a memory optimization technique that moves gradient tensors from GPU memory to system RAM during training to enable longer context windows without increasing GPU memory requirements. Non-blocking (asynchronous) offloading is critical for maintaining training speed.

## Key Information

- **RAM vs Disk**: Offloading to system RAM is vastly preferable to offloading to disk, which makes training extremely slow
- **Non-blocking is essential**: Offloading calls must be non-blocking (asynchronous); blocking calls to system RAM will actually slow down training
- **Performance**: Unsloth achieves 4× longer context with only 1-2% slowdown using this technique
- **Gradient Checkpointing**: A related technique that trades compute for memory by recomputing activations during backpropagation
- **Contrast with other systems**: Some systems offload to disk, which dramatically increases training time

## Related

- [[summary-20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han]] — source
- [[Unsloth]] — tool implementing this technique
- [[LoRA]] — fine-tuning method that works with offloading
- [[ParameterEfficientFineTuning]] — broader category
