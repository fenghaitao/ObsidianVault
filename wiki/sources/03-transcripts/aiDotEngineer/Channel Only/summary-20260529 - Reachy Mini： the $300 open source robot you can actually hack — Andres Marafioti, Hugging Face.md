---
title: "summary-20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face"
type: source
tags: [source, transcript, robotics, open-source-hardware, voice-agents, tts, speech-to-speech, streaming, cuda, kv-cache, inference-endpoints, hackable, affordable-robotics]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face.md"]
last_updated: 2026-06-30
---

## Core Summary
Andres (Andy) Marafioti, lead of multimodal research at Hugging Face, presents the Reachy Mini — a $300–450 open-source robot designed for hackers, researchers, students, and dreamers. He argues that current robotics is too expensive ($50K+), too complex, and too focused on humanoid imitation rather than creative new forms of interaction. Reachy Mini is Hugging Face's response: an affordable, repairable, hackable, and expressive robot paired with open-source voice AI tools, built to democratize how we interact with robots before the experience is dominated by a few companies.

## Key Points

### The Problem with Current Robotics
- Humanoid robots are in the mid-five-figure range ($50K+); self-driving cars in the mid-six-figure range
- Too expensive for prototyping, too complex to adapt, targeting companies rather than individuals
- Constraining robots to human form limits creativity — a spider form could be more agile and stable
- They don't look friendly or approachable

### Reachy Mini: Design Philosophy
- Two price points: $300 (no Raspberry Pi, no battery) and $450 (includes Raspberry Pi and battery)
- Ships unassembled — users build it themselves, gaining complete repair knowledge
- Everything is replaceable by ordering parts and swapping them
- People 3D-print new parts (antennas, accessories, Halloween pumpkins)
- 7,500 units shipped as of the talk
- The robot is expressive but intentionally non-humanoid to put users in a creative mindset

### Voice AI Integration
- Voice is the primary interface for robots — no one will type on a keyboard to interact with a humanoid
- The speech-to-speech pipeline: VAD → Parakeet (STT, transcribing every 150ms) → LLM with tool calling → Coqui TTS
- Robot-side app handles microphone input, echo cancellation, tool dispatching (movement, emotions), camera with face tracking
- LLM can do tool calling for robot movements and camera use
- Demo shows conversation, photo-taking with description, and emotion display

### Serving Architecture at Scale
- Three-level system: (1) conversation app on robot, (2) speech-to-speech pipeline (open source, maintained by Marafioti for 2 years), (3) Hugging Face Inference Endpoints
- Load balancer dynamically adjusts compute nodes based on connected robots
- LLM inference endpoints separated from conversation nodes for resource efficiency — per-node concurrency varies widely
- Currently using Coqui 3.5 27B as the LLM

### Optimizing Coqui 3 TTS for Real-Time
- Original Coqui 3 TTS model had good quality but poor speed — sub-real-time (0.8x)
- Three optimizations applied:
  1. **Streaming**: Generate and output audio as it's produced instead of waiting for full output
  2. **Static KV Cache + CUDA Graph Capture**: Replaced dynamic KV cache with static (more RAM upfront but faster) to enable CUDA graph captures, keeping all CPU-GPU coordination on GPU
  3. Result: Real-Time Factor improved from 0.8x to 5.8x (200ms per second of audio), Time to First Audio dropped from seconds to milliseconds
- Released as "Faster Coqui 3 TTS" — open source on Hugging Face
- Client-perceived latency includes infrastructure overhead, not just model time

### Democratizing Robot Interaction
- Everything is open source: models, agents, conversation app
- Goal: make how we interact with robots communal, developed by everyone
- Can "vibe code" robot behaviors — one-shot the demo app by describing what you want
- Robots run apps directly (anything that doesn't need GPU), or use a laptop as compute
- Not constrained by language — Java, Python, HTML all work
- Compatible with SO100/SO101 arms and Kiwi mobile base for extensibility

## Related
- [[Andres Marafioti]] — speaker, lead of multimodal research at Hugging Face
- [[Reachy Mini]] — the robot
- [[HuggingFace]] — company behind the project
- [[Coqui]] — TTS model provider (Coqui 3, Coqui 3.5 27B)
- [[Open Source Robotics]] — the movement Reachy Mini represents
- [[Voice Agents]] — primary interaction paradigm
- [[SpeechToSpeech Pipeline]] — Hugging Face's open-source pipeline
- [[RealTime Factor]] — TTS performance metric
- [[Time to First Audio]] — latency metric for voice systems
- [[CUDA Graph Capture]] — optimization technique for TTS acceleration
- [[KV Cache]] — static vs dynamic for inference speed
- [[Hugging Face Inference Endpoints]] — serving infrastructure
- [[Parakeet]] — speech-to-text model used in pipeline
- [[Raspberry Pi]] — onboard compute for $450 version
- [[aiDotEngineer]] — event host
