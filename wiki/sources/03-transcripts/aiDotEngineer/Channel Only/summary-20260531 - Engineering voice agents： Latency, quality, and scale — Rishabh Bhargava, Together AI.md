---
title: "summary-20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI"
type: source
tags: [source, transcript, voice-agents, voice-ai, latency, pipeline-architecture, speech-to-text, llm, text-to-speech, co-location, auto-scaling, speech-to-speech, turn-detection, word-error-rate, thinker-talker, tool-calling, evals]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI.md"]
last_updated: 2026-06-30
---

## Core Summary
Rishabh Bhargava, leader of the voice AI team at Together AI, delivers a comprehensive engineering talk on building production-grade voice agents. He outlines four core challenges — latency (<500ms response), intelligence (complex workflows and tool calling), naturalness (accent, pronunciation, emotion), and reliability at scale (100-10,000 concurrent calls) — as an "and" problem requiring all to be solved simultaneously. He then walks through the dominant pipeline architecture (STT → LLM → TTS), the performance metrics and trade-offs of each component, the importance of co-locating models to eliminate network latency, auto-scaling nuances for stateful connections, and the emerging direction of pure speech-to-speech models. He also discusses evaluation strategies for voice-to-function-calling and the thinker-talker pattern for managing guardrails within latency budgets.

## Key Points

### Why Voice Matters
- Billions of phone calls annually still handled by humans — customer support, reservations, doctor appointments
- Voice is a natural interface: humans learned to talk before reading
- 2026 is about building rich, high-quality conversations — now an engineering problem, not research
- Early adoption: ChatGPT advanced voice mode, voice interaction with Cursor and Claude Code

### The Four Hard Problems (Must Solve All)
- **Latency**: Human conversation turn-taking is ~300ms; >500ms noticeable; >1-2 seconds users hang up
- **Intelligence**: Real-world workflows require complex instructions, ambiguity handling, and good tool calling
- **Naturalness**: Language, accent, pronunciation, emotion — the voice must sound pleasant enough
- **Reliability at Scale**: Works for one call ≠ works for 10,000 concurrent calls

### Pipeline Architecture (Dominant Production Approach)
- Audio chunks streamed from user → Agent Orchestrator (PipeCat, LiveKit, or homegrown)
- Flow: Audio → Speech-to-Text → LLM → Text-to-Speech → Audio streamed back
- Each component has specific performance metrics and trade-offs

### Speech-to-Text Component
- **Quality**: Word Error Rate (WER) — state-of-the-art ~6%. Errors compound through the pipeline; getting keywords right is critical
- **Latency**: Time to complete transcript after utterance ends. Together achieves P90 ~100ms
- **Turn Detection**: Still somewhat unsolved — detecting whether a pause means end-of-turn or thinking
- **Languages**: Wide language coverage is important depending on customers
- **Architecture Evolution**: Moving from batch models (Whisper, 30-second clips) to streaming-native models (e.g., Nvidia's recent model with look-ahead time and cached activations)

### LLM Component
- **Streaming Latency**: TTFT ~200-300ms is good. This constrains model size to 8-30B parameters
- **Model Size**: Larger burns latency budget; smaller compromises intelligence and tool calling
- LLM takes majority of both latency and cost budget, followed by TTS, then STT

### Text-to-Speech Component
- **TTFA** (Time to First Audio): How fast first audio chunk is produced
- **Real-Time Factor** (RTF): Audio produced per second of processing. Must be <1 to avoid buffering
- **Quality**: Objective measures exist but listening to audio samples is essential
- **Capabilities**: Pronunciation control, emotional tags (happy/angry/sad), multi-language, voice variety

### Co-location and Network Latency
- Engine latency (model processing time) is only part of the picture — network latency matters
- 75ms network hop (e.g., US West to Europe) vs 5ms intra-datacenter is a ~30% reduction in total voice agent latency
- Trend: co-locate all models and orchestrator in the same data center
- Every 10ms matters; deep observability is essential

### Auto Scaling Nuances
- Scale up aggressively to avoid slowdowns (more aggressive than async systems)
- Scale down is tricky: stateful, long-lived connections mean you can't arbitrarily kill pods
- Must wait for conversations to finish before scaling down
- Global deployments matter for latency and data residency

### Speech-to-Speech Models (Next Generation)
- Single model replacing STT → LLM → TTS pipeline
- Preserves paralinguistic information (tone, emotion, hesitation) lost in text conversion
- Enables full-duplex communication and better interruption/barge-in handling
- Current limitation: poor instruction following and tool calling — most move to pipeline architecture in production
- As models improve, they unlock significant benefits for natural conversation

### Evals for Voice-to-Function Calling
- Component-by-component evals: verify STT quality, TTS quality, then LLM tool calling
- Tool call structure should be near 100% correct
- Correctness depends on use case
- Common pattern: fine-tune smaller LLMs on use-case-specific data to improve tool calling while staying within latency budget

### Guardrails and the Thinker-Talker Pattern
- Guardrail/classifier models fit before the main LLM (routing) or after LLM generation (before TTS)
- Each additional model adds latency pressure — need clear SLAs per component
- Thinker-Talker pattern: small LLM handles conversation flow and issues filler responses ("let me think about it"); one big tool call goes to a larger model with better instructions, tools, and guardrails; cleaner response goes to TTS
- Catching errors before TTS is critical — "you can't take back things that are spoken"

### Observability for Speech-to-Speech Models
- Some parts remain the same (transcription model running alongside for auditability)
- Evals shift to full-duplex conversation evals — longer conversations, holistic metrics
- Most evals happen on top of the base inference API

## Related
- [[Rishabh Bhargava]] — speaker, leads voice AI at Together AI
- [[Together AI]] — AI-native cloud company
- [[Refuel]] — company founded by Rishabh, acquired by Together AI
- [[Voice Agent Pipeline Architecture]] — the STT→LLM→TTS pipeline described
- [[Word Error Rate]] — STT quality metric
- [[Turn Detection]] — detecting end-of-speaker-turn
- [[Streaming ASR]] — streaming-native speech-to-text architectures
- [[Time to First Audio]] — TTS latency metric
- [[Real-Time Factor]] — TTS throughput metric
- [[Co-location (Voice AI)]] — reducing network latency by placing models together
- [[Auto Scaling for Voice Agents]] — scaling with stateful connections
- [[Thinker-Talker Pattern]] — small/large LLM pattern for guardrails
- [[Voice-to-Function Calling]] — evals for voice agents with tool calling
- [[Speech-to-Speech Models]] — next-generation single-model architecture
- [[Voice Agents]] — the overall domain
- [[Cascaded Systems (Voice)]] — the STT→LLM→TTS architectural pattern
- [[Full Duplex]] — bidirectional simultaneous audio
- [[Tool Calling]] — LLM function calling capability
- [[aiDotEngineer]] — event host
- [[Nvidia]] — published streaming ASR model and Voice Chat
- [[OpenAI]] — real-time API and advanced voice mode
- [[Whisper]] — canonical batch STT model
- [[Cursor]] — Together AI customer
