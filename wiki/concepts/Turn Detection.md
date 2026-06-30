---
title: "Turn Detection"
type: concept
tags: [speech-to-text, voice-agents, conversation, latency, unsolved-problems]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI.md"]
last_updated: 2026-06-30
---

## Definition
Turn detection is the capability of a voice agent to determine when a speaker has finished their turn and is expecting a response, versus when they are simply pausing to think or breathe. It is a critical but still somewhat unsolved problem in voice AI engineering.

## Key Information
- Humans respond to conversational cues in ~300ms — agents must detect turn endings accurately
- Core challenge: distinguishing a pause-for-thinking from an end-of-turn
- Getting it wrong means the agent interrupts the user mid-thought — as frustrating in AI conversations as in human ones
- Incorrect turn detection also adds latency if the agent waits too long before responding
- Still described as "somewhat unsolved" as of 2026
- Related to but distinct from Voice Activity Detection (VAD) — turn detection is about conversational semantics, not just audio presence
- Can be a "20-minute talk in itself" due to its complexity

## Related
- [[Voice Agent Pipeline Architecture]] — turn detection lives in the STT component
- [[Word Error Rate]] — another STT quality concern
- [[Streaming ASR]] — streaming models may improve turn detection
- [[Full Duplex]] — speech-to-speech models handle this differently
- [[Half Duplex]] — limited turn handling
- [[Back Channeling]] — conversational acknowledgments that complicate turn detection
- [[summary-20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI]] — source
