---
title: "Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind.md"
date: 2026-04-20
ingested: 2026-06-26
---

## Core Thesis
Gemma is Google DeepMind's family of open models designed to run on consumer hardware (phones, laptops, desktop GPUs), with Gemma 4 representing the most capable generation yet — featuring a new Apache 2.0 license, novel per-layer embeddings architecture for on-device efficiency, native multimodality, and a thriving community ecosystem (the "Gemmaverse") with over 500 million downloads and 100,000+ community models.

## Key Points
- **Gemma 4 family**: Models from 2B to 32B parameters, all fitting on consumer GPUs; includes E2B/E4B (per-layer embeddings for on-device), 26B MoE (low latency), and 31B (maximum intelligence)
- **Per-layer embeddings (E2B)**: Novel architecture where embedding tables act as lookup tables stored in CPU/disk rather than GPU, with only 2B effective parameters loaded into GPU despite 4B+ total parameters — optimized for mobile/on-device use cases
- **License change**: Gemma 4 adopted Apache 2.0 license, addressing community feedback about previous restrictive licensing
- **Multimodality**: Smallest models support image, video, and audio understanding (speech recognition, speech-to-translated-text); larger models handle fine-grained visual details and object detection
- **Multilingual**: Trained on 140+ languages with a Gemini-based tokenizer optimized for multilingual use cases, enabling fine-tuning for low-resource languages
- **Community ecosystem ("Gemmaverse")**: 500M+ total downloads, 100K+ community models (quantizations, fine-tunes), 10M Gemma 4 downloads in first week; collaborations with Unsloth, MLX, llama.cpp, Hugging Face, vLLM, C Lang
- **On-device demos**: Android phone running agentic skills (piano playing), coding on device in airplane mode, 10 parallel Gemma instances generating SVGs on laptop at 100 tokens/sec via llama.cpp
- **Product integrations**: Android Studio agent mode with offline Gemma support via llama.cpp/vLLM; model trained with Android-specific datasets
- **Official variants**: Shield Gemma (safety/guardrail models), Med-Gemini (multimodal medical model for radiology, chest X-ray)
- **Community research**: AI Singapore (Southeast Asian languages), Sarvam (Indian national languages/sovereign AI), cancer therapy pathway discovery research using Gemma 3
- **LM Arena performance**: Strong Pareto frontier — very small models achieving high capability scores, continuing multi-year trend of capability improvement without size increase

## Entities
- [[OmarSanseviero]] — Presenter, Google DeepMind
- [[Gemma4]] — Latest open model family from Google DeepMind
- [[Gemma3]] — Previous generation (released ~1 year prior)
- [[GoogleDeepMind]] — Google's AI research division
- [[AndroidStudio]] — Google's IDE with offline Gemma agent mode
- [[ShieldGemma]] — Safety/guardrail model family
- [[MedGemini]] — Multimodal medical model based on Gemma 3
- [[AISingapore]] — Research group training models for Southeast Asian languages
- [[Sarvam]] — Indian startup building national language models
- [[Unsloth]] — Fine-tuning tool collaborating on Gemma support
- [[LlamaCpp]] — Inference framework for on-device Gemma demos
- [[HuggingFace]] — Model hosting and fine-tuning platform
- [[vLLM]] — Inference engine collaborating on Gemma support
- [[Keras]] — Framework mentioned for fine-tuning
- [[Raspberry Pi]] — Target device for smallest Gemma models
- [[HuggingFaceTransformers]] — Fine-tuning framework

## Concepts
- [[PerLayerEmbeddings]] — Novel architecture for on-device efficiency (E2B/E4B)
- [[OnDeviceAI]] — Models running locally on phones, laptops, Raspberry Pi
- [[OpenSourceModels]] — Downloadable, self-hostable, customizable models
- [[Apache2License]] — Permissive license adopted by Gemma 4
- [[MixtureOfExperts]] — Architecture for 26B low-latency model
- [[EffectiveModels]] — Models with fewer operating parameters than total parameters
- [[MultilingualTokenizer]] — Gemini-based tokenizer optimized for 140+ languages
- [[SovereignAI]] — National/regional AI model development for local languages
- [[OnDeviceAgentic]] — Agentic capabilities running entirely on-device without API calls
- [[OpenModelEcosystem]] — Community-driven model customization and distribution
- [[GemmaVerse]] — Community ecosystem of fine-tuned Gemma models (100K+ models)
- [[AgenticWorkflows]] — Autonomous task execution supported by Gemma models

## Related
- [[summary-20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind]] — technical deep dive on Gemma 4 architecture
- [[summary-20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI]] — small model training comparison
- [[summary-20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han]] — earlier Gemma bug fixes
