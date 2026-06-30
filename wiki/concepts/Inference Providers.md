---
title: "Inference Providers"
type: concept
tags: [hugging-face, inference, routing, models, providers]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face.md"]
last_updated: 2026-06-30
---

## Definition
Inference Providers is a Hugging Face Hub service that routes model inference requests to the best available provider (Grok, Cerebras, Novita, etc.), offering cost and speed comparison to help users select the optimal option for their use case.

## Key Information
- Routes requests to the best model on the best provider automatically
- Providers include Grok, Cerebras, Novita, and others
- Displays the cheapest and fastest options for each model
- Includes a "tool use" column indicating which models support function/tool calling for agentic use cases
- Enables easy comparison of open models without needing to manage provider relationships
- Can be used with Pi and Hermes Agent as an alternative to local serving
- Part of Hugging Face's mission to make open models as accessible as closed API models

## Related
- [[HuggingFace]] — platform
- [[Pi (coding agent)]] — can use inference providers
- [[Hermes Agent]] — can use inference providers
- [[OpenSourceModels]] — models accessible via the service
- [[summary-20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face]] — source
