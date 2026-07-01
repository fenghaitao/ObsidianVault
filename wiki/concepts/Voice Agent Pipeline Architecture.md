---
title: "Voice Agent Pipeline Architecture"
type: concept
tags: [voice-agents, architecture, speech-to-text, llm, text-to-speech, pipeline, streaming]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI.md"]
last_updated: 2026-06-30
---

## Definition
The Voice Agent Pipeline Architecture is the dominant production approach for building voice AI agents, consisting of a cascading three-stage pipeline: Speech-to-Text (STT) → Large Language Model (LLM) → Text-to-Speech (TTS). Audio chunks are streamed from the end user to an agent orchestrator, which coordinates the flow through each model, ultimately streaming synthesized speech back to the user.

## Key Information
- Three sequential stages: STT (ears) → LLM (brain) → TTS (voice)
- Audio is chunked and streamed bidirectionally through the pipeline
- Agent orchestrators like PipeCat or LiveKit coordinate the flow; some teams build homegrown orchestrators
- Latency budget is dominated by the LLM, followed by TTS, then STT
- Co-locating all models in the same data center significantly reduces network latency (~75ms → ~5ms)
- Additional components like classifiers, guardrails, and routing models can be inserted at various points in the pipeline
- Each added component increases latency pressure and requires clear SLAs
- The pipeline can be extended with the thinker-talker pattern: a small LLM handles conversation flow while a larger model handles complex tool calls

## Related
- [[Cascaded Systems (Voice)]] — closely related architectural concept
- [[SpeechToSpeech Models]] — alternative single-model architecture
- [[Time to First Audio]] — TTS latency metric
- [[RealTime Factor]] — TTS throughput metric
- [[Word Error Rate]] — STT quality metric
- [[Turn Detection]] — STT capability for detecting end of utterance
- [[Streaming ASR]] — streaming-native speech-to-text
- [[CoLocation (Voice AI)]] — latency optimization strategy
- [[Auto Scaling for Voice Agents]] — scaling the pipeline
- [[ThinkerTalker Pattern]] — pattern for managing guardrails in the pipeline
- [[ToolCalling]] — core LLM capability
- [[Voice Agents]] — parent domain
- [[summary-20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI]] — source
