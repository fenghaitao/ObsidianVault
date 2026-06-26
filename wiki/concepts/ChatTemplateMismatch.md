---
title: "ChatTemplateMismatch"
type: concept
tags: [fine-tuning, llm, bug, chat-template, tokenization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han.md"]
last_updated: 2026-06-26
---

## Definition

Chat template mismatch is a fine-tuning bug where the chat template designed for an instruct model is applied to a base model, or the template used during training differs from the one used during inference/Ollama export. This causes NaN gradients or degraded performance.

## Key Information

- **Base vs Instruct**: Llama 3 instruct chat template references special tokens (end-of-turn, start/end header) that are untrained (zero embeddings) in the base model — using it on the base model causes NaN gradients
- **Training vs Inference**: If the chat template used during fine-tuning doesn't exactly match the template used during inference (e.g., in Ollama), accuracy degrades
- **Ollama Export**: The chat template in the Ollama model file must be exactly the same as the fine-tuning template
- **Unsloth Fix**: Automatically generates the correct Ollama model file with matching chat template
- **Custom Templates**: When creating custom chat templates, two iterations of the template must be specified to handle dangling newlines

## Related

- [[summary-20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han]] — source
- [[Llama3]] — model with this issue
- [[UntrainedTokens]] — root cause of the base/instruct mismatch
- [[DoubleBOSTokens]] — related template bug
- [[Ollama]] — requires matching chat templates
- [[Unsloth]] — tool that auto-fixes this
