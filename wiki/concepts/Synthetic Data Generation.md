---
title: "Synthetic Data Generation"
type: concept
tags: [training, fine-tuning, data, llm, distillation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-29
---

## Definition
Synthetic Data Generation is the workflow of using a much stronger cloud-based LLM to generate millions of training examples, which are then used to fine-tune a smaller model for a specific task. This is the primary approach for creating production-quality tiny LLMs for on-device deployment.

## Key Information
- Primary workflow for creating tiny LLMs for on-device deployment
- Uses a much stronger cloud LLM to generate low-digit millions to tens of millions of synthetic examples
- Synthetic data corresponds to the specific task the tiny model needs to perform
- The synthetic dataset is then used to fine-tune a tiny base model (e.g., Gemma 327M)
- After fine-tuning, quantization is applied for deployment
- Used internally by Google AI Edge for products like AI Edge Eloquent
- Collab notebooks available for Gemma 327M and Function Gemma fine-tuning workflows
- Enables narrow, reliable features powered by LLMs on a very wide set of devices

## Related
- [[summary-20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google]] — source
- [[Tiny LLMs]] — target model category
- [[FineTuning]] — training method
- [[Quantization]] — deployment optimization
- [[AI Edge Eloquent]] — production app using this workflow
- [[ModelDistillation]] — related concept
