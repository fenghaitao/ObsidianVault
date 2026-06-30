---
title: "Text Polishing"
type: concept
tags: [nlp, transcription, llm, post-processing, speech]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-29
---

## Definition
Text Polishing is a post-processing step in transcription pipelines where a dedicated tiny LLM cleans up raw speech-to-text output by removing interjections ("um", "ah"), correcting speech idioms, handling self-corrections ("scratch that"), and applying a biasing dictionary for technical terms and uncommon names.

## Key Information
- Post-processing step after ASR (Automatic Speech Recognition) transcription
- Removes interjections and filler words ("um", "ah", "you know")
- Cleans up speech idioms and lack of clarity
- Handles self-corrections ("scratch that", "I forgot to say")
- Applies biasing dictionary for technical terms and uncommon names
- Implemented as a dedicated tiny LLM (not part of the main transcription model)
- Used in AI Edge Eloquent app (iOS)
- Model is a fine-tuned derivative of Gemma 327M lineage
- Instruction fine-tuned with system prompt specifying special words and correction rules
- Demonstrates modularity pattern: separate model for polishing enables reuse across features

## Related
- [[summary-20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google]] — source
- [[AI Edge Eloquent]] — app using text polishing
- [[Biasing Dictionary]] — complementary feature
- [[Tiny LLMs]] — model category used
- [[FineTuning]] — model customization approach
- [[Synthetic Data Generation]] — training data workflow
