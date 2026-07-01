---
title: "Voice-to-Function Calling"
type: concept
tags: [voice, function-calling, on-device, agents, multimodal]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI.md"]
last_updated: 2026-06-29
---

## Definition
Voice-to-Function Calling is the capability where a voice command is transcribed and then mapped to a specific function call by a tiny LLM. It enables voice-driven app interactions on device, with models like Function Gemma (270M) achieving 85-90% reliability on sets of 10 mobile-relevant functions after fine-tuning.

## Key Information
- Voice command → transcription → function call execution
- Function Gemma (270M params) achieved 85-90% reliability on 10 mobile-relevant functions
- On simple functions (8 of 10), reliability exceeded 90-93%
- Requires fine-tuning for production-level reliability
- Example fine-tuned derivatives: Mobile Actions (10 mobile actions), Tiny Garden (voice-controlled game)
- Modularity pattern: separate transcription and function-calling models often preferred for reusability and debuggability
- Part of the tiny LLM (TLM) in-app GenAI deployment pattern
- Runs on-device for privacy and latency benefits
- For voice agents in production, evals focus on tool call structure correctness (near 100%) and correctness depending on use case
- Fine-tuning smaller LLMs on use-case-specific data is a common pattern to improve tool calling quality while staying within latency budgets

## Related
- [[summary-20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google]] — source
- [[summary-20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI]] — source
- [[Function Gemma]] — model designed for this use case
- [[Function Calling]] — underlying capability
- [[Tiny LLMs]] — model category
- [[FineTuning]] — required for reliability
- [[AI Edge Gallery]] — app where derivatives can be tested
- [[ThinkerTalker Pattern]] — related pattern for voice agent guardrails
