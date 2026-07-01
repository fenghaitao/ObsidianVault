---
title: "Ollama"
type: entity
tags: [tool, models, local, self-host]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - OpenRAG： An open-source stack for RAG — Phil Nash.md"]
last_updated: 2026-06-26
---

## Definition
Ollama is a local model runner that allows users to download and self-host Gemma 4 models on their own hardware.

## Key Information
- One of three self-host options for Gemma 4 models (alongside Hugging Face and Kaggle)
- Enables running models locally without cloud dependencies
- Exporting fine-tuned models to Ollama requires exactly matching chat templates between training and inference
- Unsloth can automatically generate Ollama model files with correct chat templates
- Supports multiple GGUF format files for model distribution
- Used in OpenRAG as a local embedding and model provider (Granite 4 3B, Qwen 3 embedding 0.6B) for fully offline operation

## Related
- [[Gemma4]] — available on the platform
- [[HuggingFace]] — alternative self-host platform
- [[Kaggle]] — alternative self-host platform
- [[OnDeviceAI]] — related concept
- [[summary-20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind]] — source
- [[summary-20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han]] — source
- [[summary-20260408 - OpenRAG： An open-source stack for RAG — Phil Nash]] — source
- [[OpenRAG]] — uses Ollama for local embeddings and models
- [[Granite]] — Granite 4 3B runs on Ollama in OpenRAG demo
- [[Unsloth]] — tool with automated Ollama export
- [[ChatTemplateMismatch]] — must be avoided for correct export
- [[GGUF]] — model format used by Ollama
