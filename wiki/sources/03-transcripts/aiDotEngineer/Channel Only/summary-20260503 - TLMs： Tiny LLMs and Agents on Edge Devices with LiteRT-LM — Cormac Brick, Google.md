---
title: "summary-20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google"
type: source
tags: [source, transcript, ai, edge-ai, tiny-llms, tlm, gemma, liteRT, on-device, agent-skills, fine-tuning, quantization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-29
---

## Core Summary
Cormac Brick, tech lead for Google AI Edge, presents two major trends in on-device AI: tiny LLMs (TLMs) for in-app deployment and agent skills running on larger on-device models like Gemma 4. He covers Google's edge AI stack (MediaPipe, LiteRT-LM, LiteRT), the distinction between system-level GenAI (2-5B parameter models built into the OS) and in-app GenAI (100-500M parameter fine-tuned models), the new Gemma 4 E2B/E4B models with per-layer embeddings, the agent skills architecture using progressive disclosure and constrained decoding, the open-source Google AI Gallery app, and a real-world tiny LLM app (AI Edge Eloquent) for transcription with text polishing.

## Key Points

### Edge AI Benefits and Stack
- Four key benefits of edge AI: latency/UX improvements, privacy (data stays on device), offline use, and cost savings
- Google's edge AI stack: MediaPipe (ML pipelines), LiteRT-LM (LLM runtime for mobile/edge), LiteRT (general inference framework, formerly TensorFlow Lite)
- Single LiteRT file deploys on CPU and GPU across Android, iOS, macOS, Linux, Windows, web, and IoT devices
- NPU requires special AOT compilation producing a device-specific file
- Underlying optimization libraries: XNNPACK (CPU) and ML Drift (GPU)

### Two Trends: System-Level vs In-App GenAI
- **System-level GenAI**: Larger models (2-5B parameters) built into the OS (Android AI Core, Apple Intelligence). Customized via prompting or skills. Available on premium devices
- **In-app GenAI**: Tiny models (100-500M parameters) loaded with the app. Customized via fine-tuning for specific tasks. Works on all devices for wider reach
- Function Gemma (270M parameters) achieved 85-90% reliability on 10 function-calling tasks via fine-tuning
- Below 500M parameters, fine-tuning is necessary for production-level reliability

### Gemma 4 Models
- E2B: 2 billion effective parameters (5.1B representational), optimized for on-device
- E4B: 4 billion effective parameters, optimized for on-device
- Per-layer embeddings (PLE): extra parameters stored in flash, only small portions loaded during inference
- Built-in function calling and thinking capabilities enable agent skills on device
- Multimodal: support audio, image, and text input
- Released under Apache 2.0 license
- Performance: thousands of tokens/sec on high-end Android phones (GPU), ~133 tok/sec on Raspberry Pi
- On AI Core roadmap for future Android integration

### Agent Skills on Device
- Skills use progressive disclosure: one-line descriptions visible to the agent, full details loaded on demand
- Architecture: skill.md (metadata + instructions) + optional scripts/assets (JavaScript)
- Three predefined tools: load_skill, run_javascript, run_intent
- Constrained decoding applied during tool calls for reliability on small models
- Skills can extend both input (Wikipedia, weather, CRM) and output (maps, cards, music)
- Skills can run fully offline (local JavaScript) or call web APIs with API keys
- Google AI Gallery is open source, builds on LiteRT-LM
- Community skills shared via GitHub discussions; featured skills promoted in the app
- Team internally built ~80 skills, many "vibe coded" using Gemini CLI or Claude Code
- Skills work with both 2B and 4B models; simpler skills and fewer concurrent skills work better on 2B

### Tiny LLM Workflow
- LiteRT-LM: open-source C++/Java/Swift/Python APIs for running LLMs on device
- Workflow: start from HuggingFace Transformers → LiteRT Torch (with PyTorch native optimizations and quantization) → LiteRT-LM file → deploy
- LiteRT Torch Generative API for building custom models from scratch
- Supports third-party models (Qwen, FastVLM from Apple, etc.)
- Gallery app can load any LiteRT-LM file for benchmarking
- FastVLM (500M params, Apple) runs real-time video scene description on Qualcomm hardware

### AI Edge Eloquent (Real-World Tiny LLM App)
- iOS app for transcription with automatic text polishing
- Two-step pipeline: ASR engine (transcription) → Text Polishing Engine (tiny LLM)
- Text polishing removes interjections ("um", "ah"), cleans up speech idioms
- Biasing dictionary: users can add uncommon names and technical terms (e.g., "LoRA" not "Laura")
- Personalization: imports unusual words from Gmail to build biasing list
- Both ASR and text polishing engines are fine-tuned derivatives of Gemma 327M lineage
- Modularity pattern: separate models for separate tasks, enabling reuse across features
- Fine-tuning workflow: use a larger cloud model to generate millions of synthetic data examples, then fine-tune the tiny base model

### Synthetic Data Fine-Tuning Workflow
- Use a much stronger cloud LLM to generate low-digit millions to tens of millions of synthetic examples
- Fine-tune a tiny base model (e.g., Gemma 327M) on that synthetic data
- Apply quantization for deployment
- Collab notebooks available for Gemma 327M and Function Gemma fine-tuning

## Related
- [[Cormac Brick]] — speaker, Google AI Edge tech lead
- [[Google AI Edge]] — Google's edge AI division
- [[LiteRT-LM]] — LLM runtime for mobile and edge
- [[LiteRT]] — general inference framework (formerly TensorFlow Lite)
- [[MediaPipe]] — ML pipeline framework
- [[Gemma4]] — E2B and E4B models
- [[Function Gemma]] — 270M parameter function-calling model
- [[Embedding Gemma]] — 300M parameter text embedding model
- [[AI Core]] — Android system-level GenAI
- [[AI Edge Gallery]] — open-source app for experimenting with on-device models
- [[AI Edge Eloquent]] — transcription + text polishing app
- [[Tiny LLMs]] — models under 1B parameters for in-app deployment
- [[System-level GenAI]] — large models built into the OS
- [[In-app GenAI]] — tiny models loaded with the app
- [[Agent Skills]] — progressive disclosure skill architecture
- [[ProgressiveDisclosure]] — design pattern for context efficiency
- [[ConstrainedDecoding]] — technique for reliable tool calling
- [[EffectiveModels]] — models with fewer effective than representational parameters
- [[PerLayerEmbeddings]] — key enabling technique for on-device models
- [[OnDeviceAI]] — running AI locally on consumer hardware
- [[Edge AI]] — AI on edge devices
- [[Synthetic Data Generation]] — using large models to generate training data
- [[FineTuning]] — customizing models for specific tasks
- [[Quantization]] — reducing model size for deployment
- [[Cross-platform deployment]] — single file across multiple platforms
- [[NPU]] — neural processing unit for hardware acceleration
- [[AOT Compilation]] — ahead-of-time compilation for NPU
- [[Text Polishing]] — cleaning up transcribed speech
- [[Biasing Dictionary]] — custom word lists for transcription accuracy
- [[Voice-to-Function Calling]] — voice commands to function execution
- [[Skill Architecture]] — structure of agent skills
- [[Function Calling]] — model capability to invoke tools
- [[Intel]] — previous employer, NPU architecture
- [[Qualcomm]] — hardware partner
- [[MediaTek]] — hardware partner
- [[Raspberry Pi]] — edge deployment platform
- [[Google]] — parent company
- [[Google DeepMind]] — Gemma model team
- [[Android]] — target platform
- [[iOS]] — target platform
- [[aiDotEngineer]] — event host
