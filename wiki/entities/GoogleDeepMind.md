---
title: "GoogleDeepMind"
type: entity
tags: [company, ai, google, frontier-models, coding-agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Welcome to AIE CODE - Jed Borovik, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Low Level Technicals of LLMs： Daniel Han.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - The Future of MCP — David Soria Parra, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260525 - Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition
Google DeepMind is Google's AI research division and the presenting sponsor of the 2025 AI Engineering Code Summit. It develops frontier AI models including Gemini 3 and Nano Banana Pro, builds coding agent products like Jules, and serves as the reference implementation (via JAX) in LLM architecture bug comparison.

## Key Information
- Presenting sponsor of the 2025 AI Engineering Code Summit in New York
- Launched Gemini 3 and Nano Banana Pro the same week as the Summit (early January 2026)
- Employs Raia Hadsell, VP of Research overseeing ~1200 scientists/engineers across 10 labs, who presented on Frontier AI research (embeddings, weather, world models)
- Employs Jed Borovik, who leads the Jules coding agent product engineering team
- Employs Paige Bailey, DevRel lead who demonstrates the latest models at conferences
- Released a rapid succession of models in early 2026: Gemini 3.1 Flash Live, Gemini 3.1 Pro, Gemini 3.1 Flash Light, Nano Banana 2, Lyra 3, Genie 3, Gemma 4, VEO 3.1 Light
- Research philosophy: find root nodes (deepest unsolved problems), partner broadly, solve problems worth solving for humanity
- AI Studio platform provides free access to experiment with all DeepMind models
- Positioned as a leader in the AI coding industry alongside other frontier model providers
- DeepMind's JAX implementations serve as the canonical reference in Daniel Han's three-way model comparison methodology (DeepMind vs HuggingFace vs Keras)
- Employs Omar Sanseviero, who presented on Gemma 4 at the AI Engineering conference
- Gemma 4 ecosystem strategy: collaborate with open-source community (Unsloth, MLX, llama.cpp, Hugging Face, vLLM, C Lang) to ensure tools work at launch
- Gemma family has 500M+ total downloads and 100K+ community models ("Gemmaverse")
- Official Gemma variants: Shield Gemma (safety/guardrails), Med-Gemini (medical/multimodal)
- **BullshitBench performance**: Gemini models score ~50/50 on BullshitBench — they go along with nonsense questions about half the time. Example response starts by acknowledging the question doesn't make sense, then pivots to "however, both act as strong proxy variables for engineering culture." Google models show no clear upward trend in nonsense detection over time.

## Related
- [[summary-20260105 - Welcome to AIE CODE - Jed Borovik, Google DeepMind]] — source
- [[summary-20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research]] — source
- [[summary-20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind]] — source
- [[summary-20240731 - Low Level Technicals of LLMs： Daniel Han]] — source
- [[RaiaHadsell]] — VP of Research
- [[JedBorovik]] — product engineering leader
- [[Paige Bailey]] — DevRel lead
- [[Gemini3]] — frontier model launched same week
- [[NanoBananaPro]] — product launched same week
- [[Jules]] — coding agent product
- [[AIECodeSummit]] — event they sponsored
- [[AIStudio]] — platform for model experimentation
- [[Gemma4]] — open model family with Apache 2.0 license
- [[Gemma3]] — previous generation open model family
- [[Genie 3]] — world model
- [[Lyra 3]] — music generation model
- [[CassidyHardin]] — researcher who presented Gemma 4 deep dive
- [[OmarSanseviero]] — presenter on Gemma 4 overview
- [[ShieldGemma]] — official safety variant
- [[MedGemini]] — official medical variant
- [[GeminiEmbeddings2]] — omnimodal embedding model
- [[GraphCast]] — weather prediction model
- [[GenCast]] — probabilistic weather model
- [[FGN]] — cyclone prediction model
- [[summary-20260420 - Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind]] — source
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — source (contributed stateless transport protocol proposal for MCP)
- [[SanderDieleman]] — research scientist, generative media team
- [[Veo]] — video generation model series
- [[NanoBanana]] — image generation model
- [[JAX]] — primary ML framework
- [[TPU]] — AI accelerator hardware
- [[StatelessTransportProtocol]] — Google's proposal for scalable MCP transport
- [[summary-20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench]] — source (BullshitBench ~50/50 performance)
- [[BullshitBench]] — benchmark where Gemini models are mid-tier
- [[Nonsense Detection]] — capability where Gemini models struggle
- [[Peter Gostev]] — BullshitBench creator
- [[summary-20260505 - Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind]] — source (Lite RT, Gemma 4 Edge, on-device AI)
- [[Chintan Parikh]] — product manager for Lite RT
- [[Weiyi Wang]] — colleague
- [[Lite RT]] — on-device inference framework
- [[Google AI Edge]] — division
- [[NPU Acceleration]] — hardware acceleration for on-device AI
- [[summary-20260525 - Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind]] — source
- [[NicholasKang]] — PM for Kaggle Benchmarks
- [[MichaelAaron]] — SWE on Kaggle evaluations and benchmarks
- [[Game Arena]] — PvP unsaturable benchmark on Kaggle
- [[Agent Exams]] — standardized agent testing on Kaggle
- [[Eval Hackathons]] — community-driven benchmark creation on Kaggle
- [[summary-20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind]] — source
- [[KP Sawhney]] — software engineer on AI platform team
- [[Ian Ballantyne]] — developer relations engineer
- [[Antigravity]] — agentic IDE and platform
- [[Agent Quota Management]] — scaling challenge for token-hungry agents
- [[Model Tiering]] — seamless model fallback strategy
- [[Agent Trajectory Store]] — internal observability for coding agents
- [[Agentic Code Review]] — automated PR review with fine-tuned models
