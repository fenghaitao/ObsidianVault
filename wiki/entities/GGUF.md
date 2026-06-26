---
title: "GGUF"
type: entity
tags: [format, model, llama.cpp, quantization, ollama]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han.md"]
last_updated: 2026-06-26
---

## Definition

GGUF (GPT-Generated Unified Format) is the model file format used by llama.cpp for running language models. It supports quantization and is the standard format for models deployed via Ollama.

## Key Information

- **CPU vs GPU Conversion**: When converting models to GGUF, CPU conversion must be used rather than GPU conversion due to floating-point precision differences between CPU float16 and GPU float16
- **Multi-file Support**: Unsloth supports saving to multiple GGUF files simultaneously instead of waiting for sequential conversions
- **Ollama Compatibility**: Ollama model files must embed the correct chat template that matches the fine-tuning template exactly
- Used as the distribution format for locally-run models

## Related

- [[summary-20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han]] — source
- [[Ollama]] — model runner using GGUF
- [[Unsloth]] — tool supporting GGUF export
- [[Llama3]] — commonly exported to GGUF
