---
title: "HuggingFace"
type: entity
tags: [platform, models, open-source, hosting]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Low Level Technicals of LLMs： Daniel Han.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - FLUX, Open Research, and the Future of Visual AI — Stephen Batifol, Black Forest Labs.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face.md"]
last_updated: 2026-06-30
---

## Definition
Hugging Face is a model hosting platform and library (Hugging Face Transformers) used as one of three reference implementations for comparing LLM architecture correctness alongside DeepMind and Keras.

## Key Information
- One of three self-host options for Gemma 4 models (alongside Kaggle and Ollama)
- Platform for sharing and discovering open-source AI models
- Transformers library is one of the "three screens" in Daniel Han's LLM implementation comparison methodology (HuggingFace, DeepMind, Keras)
- Implementation discrepancies between HuggingFace Transformers and other frameworks reveal bugs, tokenization issues, and precision inconsistencies in model implementations
- MLX community on Hugging Face hosts 4,000-5,000 quantized models for Apple Silicon, with new models uploaded within ~30 minutes of release
- MLX Swift LM integrates directly with Hugging Face to download models by ID
- Flux 1 was the most liked model on Hugging Face at its launch (August 2024), a notable achievement for a new company

- **Hugging Face Traces**: New dataset repository type for storing agent execution traces (Codex, Claude Code, Pi) with parsed trace columns for analysis and fine-tuning
- **Hugging Face Skills**: Suite of agent skills (HF CLI, LLM Trainer, Gradio, Dataset) enabling agents to manage Hub resources, train models, and build demos via natural language
- **Hugging Face MCP Server**: MCP integration exposing models, datasets, spaces, semantic search, and jobs to agents
- **Inference Providers**: Routing service connecting to Grok, Cerebras, Novita and others with cost/speed comparison and tool-use indicators
- **Benchmark Datasets**: Feature aggregating model rankings on SWE-Bench Pro, Humanity's Last Exam, AIMEE for easier model selection
- **Hugging Face Jobs**: One-off paid compute jobs ending on success/failure, accessible via MCP
- **Hugging Face Buckets**: S3-compatible storage cheaper and faster than S3 for job data persistence
- **GGUF**: File format for quantized models with hardware compatibility info on model pages
- Hosts ~3 million models, datasets, and spaces as of May 2026
- Agentic models can be filtered; VLMs act as computer-use agents via screenshots

## Related
- [[Gemma4]] — available on the platform
- [[Kaggle]] — alternative self-host platform
- [[Ollama]] — alternative self-host platform
- [[LiquidAI]] — distributes LFM models on the platform
- [[MLX]] — Apple framework with community models on Hugging Face
- [[Hugging Face Traces]] — agent trace dataset type
- [[Hugging Face Skills]] — agent skills for Hub management
- [[Hugging Face MCP Server]] — MCP integration
- [[Inference Providers]] — model routing service
- [[Benchmark Datasets]] — model comparison feature
- [[Hugging Face Jobs]] — one-off compute
- [[Hugging Face Buckets]] — S3-compatible storage
- [[Hermes Agent]] — agent framework using Hub inference
- [[GGUF]] — quantized model format
- [[summary-20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind]] — source
- [[summary-20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI]] — source
- [[summary-20240731 - Low Level Technicals of LLMs： Daniel Han]] — source
- [[summary-20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI]] — source
- [[summary-20260508 - FLUX, Open Research, and the Future of Visual AI — Stephen Batifol, Black Forest Labs]] — source
- [[summary-20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face]] — source
- [[LLMImplementationAnalysis]] — methodology using HuggingFace as reference
- [[HuggingFaceTransformers]] — the Transformers library specifically
- [[Flux]] — most liked model on the platform at launch
- [[Black Forest Labs]] — creator of Flux
