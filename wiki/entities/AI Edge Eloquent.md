---
title: "AI Edge Eloquent"
type: entity
tags: [app, google, ios, transcription, tiny-llm, text-polishing, gemma]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-29
---

## Definition
AI Edge Eloquent is an iOS app from Google AI Edge that provides offline transcription with automatic text polishing. It uses fine-tuned tiny LLMs derived from the Gemma 327M lineage to clean up speech interjections and apply a biasing dictionary for technical terms and uncommon names.

## Key Information
- iOS-only app for transcription with automatic text polishing
- Runs entirely offline
- Two-step pipeline: ASR (Automatic Speech Recognition) engine → Text Polishing Engine (tiny LLM)
- Text polishing removes interjections ("um", "ah"), cleans up speech idioms, and handles corrections ("scratch that", "I forgot to say")
- Biasing dictionary: users can add uncommon names and technical terms (e.g., "LoRA" not "Laura")
- Personalization: can import unusual words from Gmail to build biasing list
- Both ASR and text polishing engines are fine-tuned derivatives of Gemma 327M lineage
- Fine-tuning workflow: larger cloud model generates millions of synthetic examples → fine-tune tiny base model → quantize for deployment
- Demonstrates modularity pattern: separate models for separate tasks, enabling reuse across features
- Example of a production app built with tiny LLMs for in-app GenAI deployment

## Related
- [[summary-20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google]] — source
- [[Google AI Edge]] — creator
- [[Tiny LLMs]] — model category used
- [[Text Polishing]] — core feature
- [[Biasing Dictionary]] — personalization feature
- [[Synthetic Data Generation]] — fine-tuning workflow
- [[FineTuning]] — model customization approach
- [[Gemma]] — base model lineage
- [[iOS]] — platform
