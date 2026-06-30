---
title: "Thinker-Talker Pattern"
type: concept
tags: [voice-agents, architecture, guardrails, llm, latency, tool-calling]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI.md"]
last_updated: 2026-06-30
---

## Definition
The Thinker-Talker pattern is a voice agent architecture that splits LLM responsibilities between a small, fast "talker" model and a larger, more capable "thinker" model. The talker handles real-time conversation flow while the thinker processes complex tool calls and guardrails in parallel, enabling rich functionality without compromising conversational latency.

## Key Information
- Small LLM ("talker") handles ongoing conversation: receives STT output, produces filler responses like "let me think about it" or "let me get back to you"
- Talker issues one big tool call to a much larger model ("thinker") with better instructions, all tools, and more guardrails
- Thinker produces a clean, verified response that goes to TTS
- Addresses the problem of catching guardrail violations before TTS speaks — "you can't take back things that are spoken"
- Keeps the small model within latency budget for real-time interaction while accessing bigger model intelligence for correctness
- Related to the general pattern of guardrail/classifier models inserted at various points in the voice agent pipeline

## Related
- [[Voice Agent Pipeline Architecture]] — the pipeline this pattern extends
- [[Voice-to-Function Calling]] — the evaluation domain this pattern supports
- [[Tool Calling]] — capability enabled by the thinker model
- [[summary-20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI]] — source
