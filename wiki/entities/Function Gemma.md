---
title: "Function Gemma"
type: entity
tags: [model, google, deepmind, function-calling, tiny-llm, fine-tuning]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-29
---

## Definition
Function Gemma is a 270 million parameter model from Google DeepMind, purpose-built for function calling. It is designed as a base model for further fine-tuning on specific function-calling tasks and can be deployed widely on iOS and Android devices.

## Key Information
- 270 million parameter model dedicated to function calling
- Published in partnership between Google AI Edge and Google DeepMind (December 2024)
- Achieved 85-90% reliability on an internal eval set of 10 different mobile-relevant functions
- On simple functions (8 of 10), reliability exceeded 90-93%
- Designed as a base model for further fine-tuning on specific function-calling tasks
- Instruction fine-tuned (IT suffix) with function-calling personality already built in
- Collab notebooks available for formatting datasets and fine-tuning workflows
- Example fine-tuned derivative: Mobile Actions (10 mobile actions at 86-87% reliability)
- Example fine-tuned derivative: Tiny Garden (voice-to-function-calling game)
- Deployable on both iOS and Android devices
- Part of the tiny LLM (TLM) category: models under 1B parameters for in-app deployment

## Related
- [[summary-20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google]] — source
- [[Gemma]] — model family
- [[GoogleDeepMind]] — creator
- [[Tiny LLMs]] — model category
- [[Function Calling]] — core capability
- [[FineTuning]] — required for production use
- [[VoiceToFunction Calling]] — key use case
- [[AI Edge Gallery]] — app where derivatives can be tested
