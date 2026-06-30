---
title: "Cascaded Systems (Voice)"
type: concept
tags: [voice-ai, architecture, speech-to-text, llm, text-to-speech, streaming]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI.md"]
last_updated: 2026-06-29
---

## Definition
Cascaded systems in voice AI refer to the three-stage architecture where audio is processed through separate models: Speech-to-Text (STT) → Large Language Model (LLM) → Text-to-Speech (TTS). Despite being less "elegant" than speech-to-speech models, cascaded systems remain the most practical and reliable approach for production voice AI as of 2026.

## Key Information
- Three sequential stages: STT transcribes audio → LLM generates response → TTS speaks the response
- Gradium's implementation adds: streaming STT, streaming TTS with voice cloning, and semantic VAD
- Neil Zeghidour admits he used to be "at war" against cascaded systems but now sees them as the practical default
- Advantages: reliability, intelligence, personalization, observability, tool calling support
- Main disadvantage: inherently high latency due to three separate processing stages
- Human conversation requires ~200ms for the entire stack; cascaded TTS alone is >200ms
- Tool call latency (500ms-4s via OpenRouter) is now the bigger bottleneck than TTS latency
- Fillers can mitigate tool call latency by keeping conversation flowing during waits
- Anything not in the text (paralinguistic cues) is lost in cascaded systems
- LLM takes majority of latency and cost budget, followed by TTS, then STT
- Model size constrained to 8-30B parameters to meet ~200-300ms TTFT budget
- Network latency between components can add 75ms+ — co-location in same data center is key optimization

## Related
- [[summary-20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI]] — source
- [[summary-20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI]] — source
- [[Speech-to-Speech Models]] — alternative architecture
- [[Voice Agent Pipeline Architecture]] — the full pipeline including orchestrator and infrastructure
- [[Voice AI]] — parent domain
- [[Fillers (Voice AI)]] — latency mitigation technique
- [[Latency]] — key challenge
- [[Tool Calling]] — current bottleneck
- [[Gradium AI]] — implements streaming cascaded systems
- [[Streaming TTS]] — component of cascaded systems
- [[Semantic VAD]] — component of cascaded systems
- [[Co-location (Voice AI)]] — latency optimization strategy
- [[Auto Scaling for Voice Agents]] — scaling infrastructure
