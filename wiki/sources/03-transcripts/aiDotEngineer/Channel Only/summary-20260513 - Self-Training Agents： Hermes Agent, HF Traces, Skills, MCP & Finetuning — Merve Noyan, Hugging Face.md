---
title: "Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face.md"
date: 2026-05-13
ingested: 2026-06-30
tags: [self-training-agents, hugging-face, hermes-agent, agent-traces, skills, mcp, finetuning, open-source, local-agents, open-models, vlm]
---

## Core Thesis
Merve Noyan presents the Hugging Face open agent ecosystem as a comprehensive stack for building, running, and improving agents using open models. The thesis spans three layers: (1) local coding agents like Hermes Agent and Pi that run open models via LlamaCPP or inference providers, (2) Hugging Face Traces — a new dataset repository type for capturing agent sessions that can later be used for fine-tuning (self-training agents), and (3) Hugging Face Skills and MCP server that allow agents to train models, launch demos, query spaces, and manage HF Hub resources. The overarching vision is "having an AI engineer at your fingertips" — where agents can self-improve by training on their own traces using open infrastructure.

## Key Topics
- **Open Source vs Open Weights vs Open Everything**: Noyan draws a spectrum: open weights models with non-commercial licenses → open source models with commercially available licenses (MIT, Apache 2.0) → fully open models where code, agent harnesses, and everything are open. This matters because open infrastructure means "nothing changes without you knowing" — no hidden performance degradation, full privacy for edge deployment, and the ability to quantize, shrink, or fine-tune models. The 2026 AI Index shows open models (green) have caught up to closed models (black).
- **Hugging Face Hub as Agent Infrastructure Layer**: The Hub hosts ~3 million models, datasets, and spaces. Agentic models can be filtered and discovered. Two types of agentic models: (1) vision LLMs that act as computer-use agents via screenshots, (2) standard LLMs for text-based agent tasks. Trend: labs are releasing LLMs with vision capabilities day zero (Gemini 4, Qwen 3.5, Chimera 2.5).
- **Local Coding Agents**: Multiple options exist for running coding agents locally. Pi is highlighted for simplicity — serve a model via LlamaCPP and Pi directly consumes it. Llama Agent is baked into LlamaCPP as a binary that starts a model by Hugging Face Hub ID. Models are easily found via the "Apps" filter on the Hub showing LM Studio, LlamaCPP, and other local serving options. The "Use this model" button provides ready-to-run commands.
- **Hermes Agent**: Described as "one step further from OpenClaw" with superior memory management. Features a setup wizard that handles key configuration and integrates with Slack, WhatsApp, etc. Noyan strongly recommends GLM 5.1 as the open model to use with Hermes Agent — she used it to fix her own Slack integration failure autonomously. Also plans to test with Gemma 4 and rumored MiniMax models.
- **Hugging Face Traces**: A new dataset repository type for storing agent execution traces (Codex, Claude Code, Pi traces). Traces are parsed nicely in the dataset viewer, making it easy to explore agent behavior. The self-training loop: capture agent traces → explore them → use them to fine-tune a model for better agent performance. Hermes Agent support for traces is coming soon.
- **GGUF and Hardware Compatibility**: GGUF format (supported by LlamaCPP, LM Studio, etc.) with hardware compatibility info on model pages. Example: Gemma 4 quantized to 4-bit fits in an L4 GPU with 24GB VRAM. MLX repositories also served.
- **Hugging Face Skills**: A suite of skills for coding agents to manage HF Hub resources. HF CLI Skill allows agents to manage repositories, run jobs, launch demos. LLM Trainer Skill handles end-to-end fine-tuning — the agent calculates VRAM requirements, batch sizes, instance types, and kicks off jobs remotely or locally. Works for LLMs, VLMs, object detectors, and segmentation models. Gradio Skill builds demos. Dataset Skill explores datasets via the dataset viewer API. Noyan describes training models by simply telling the agent "train Qwen-2-VL on Lava-Instruct-MiX" as "absolute sci-fi."
- **Hugging Face MCP Server**: MCP integration exposing models, datasets, spaces, semantic search for spaces, and jobs (one-off paid compute that ends on success/failure). Plays nicely with all major platforms (Claude, Gemini, etc.). The "Dynamic Spaces" setting (experimental) exposes all spaces for broader querying. Example: asking the model to generate an image of "baklava made of yarn" routes through the Qwen image generation space.
- **End-to-End Use Case — OCR 30,000 Papers**: Niels (colleague) used Hugging Face infrastructure end-to-end: (1) used the OCR benchmark dataset to pick Chandr OCR, (2) asked an LLM to write and kick off a processing job via Hugging Face Jobs, (3) used skills to set up hosting instances. All through prompting — no manual infrastructure work.
- **Hugging Face Buckets**: Recently launched S3-compatible storage that is cheaper and faster than S3, usable with mounting for job data persistence.

## Entities
- [[Merve Noyan]] — speaker, Hugging Face open source team
- [[HuggingFace]] — platform hosting 3M+ models, datasets, spaces
- [[Hermes Agent]] — personal AI agent framework with memory management, one step beyond OpenClaw
- [[GLM 5.1]] — open model recommended for Hermes Agent, top of SWE-Bench
- [[OpenClaw]] — personal agent framework, baseline for Hermes Agent comparison
- [[Pi (coding agent)]] — local coding agent for running with open models
- [[LlamaCpp]] — local serving framework with built-in Llama Agent binary
- [[Qwen]] — model family used with HF Skills for fine-tuning
- [[Gemma4]] — model planned for Hermes Agent testing
- [[MiniMax]] — rumored new model for future testing
- [[DeepSeek]] — example of open source model with MIT license
- [[aiDotEngineer]] — conference where talk was presented
- [[GGUF]] — file format for quantized models, supported across local serving tools
- [[MLX]] — Apple Silicon framework with quantized models on HF Hub

## Concepts
- [[Self-Training Agents]] — agents that improve by training on their own traces
- [[Hugging Face Traces]] — dataset repository type for agent execution traces
- [[Hugging Face Skills]] — skill suite for agents to manage HF Hub (train, deploy, explore)
- [[Hugging Face MCP Server]] — MCP integration for HF Hub resources
- [[Local Coding Agents]] — running coding agents locally with open models
- [[Benchmark Datasets]] — HF feature for comparing open models on standard benchmarks
- [[Inference Providers]] — HF routing service for best models to best providers
- [[Open Weights]] — models with publicly available weights, distinct from fully open source
- [[Vision Language Models]] — VLMs as computer-use agents via screenshots
- [[Agent Traces]] — captured agent execution data for analysis and fine-tuning
- [[Hugging Face Jobs]] — one-off paid compute jobs on HF infrastructure
- [[Hugging Face Spaces]] — app store of AI, queriable via MCP
- [[Hugging Face Buckets]] — S3-compatible cheaper/faster storage
- [[Computer Use]] — VLM-driven GUI interaction capability
- [[FineTuning]] — process enabled by agent traces and HF Skills
- [[Model Quantization]] — shrinking models for local deployment
- [[OpenSourceModels]] — broader ecosystem of open models

## Related
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — OpenClaw as personal agent
- [[summary-20260420 - Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind]] — open model ecosystem
- [[summary-20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind]] — model capabilities
- [[summary-20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI]] — fine-tuning
- [[summary-20260504 - Skill Issue： How We Used AI to Make Agents Actually Good at Supabase — Pedro Rodrigues, Supabase]] — skills for agents
- [[summary-20260506 - Full Walkthrough： Writing & Using Skills — Nick Nisi and Zack Proser]] — skills
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — MCP ecosystem
- [[summary-20260503 - Context Is the New Code — Patrick Debois, Tessl]] — context as code
