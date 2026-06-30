---
title: "Biasing Dictionary"
type: concept
tags: [transcription, personalization, nlp, speech, on-device]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-29
---

## Definition
A Biasing Dictionary is a list of uncommon words, technical terms, and proper names provided to a transcription system to improve accuracy. Standard transcription services often mis-transcribe technical terms (e.g., "LoRA" becomes "Laura"), and the biasing dictionary corrects this by telling the model to prefer specific spellings.

## Key Information
- List of keywords or technical terms that the transcription model should prefer
- Addresses common failure mode: standard transcription services mis-transcribe technical terms and uncommon names
- Example: "LoRA" (ML technique) would be transcribed as "Laura" without biasing
- Example: team member names "Gianning" and "Surreal" would be mis-transcribed
- Used in AI Edge Eloquent app for offline transcription
- Personalization: can import unusual words from Gmail to automatically build biasing list
- Users can also manually add terms
- Works alongside text polishing in the transcription pipeline

## Related
- [[summary-20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google]] — source
- [[AI Edge Eloquent]] — app using biasing dictionary
- [[Text Polishing]] — complementary feature in transcription pipeline
- [[OnDeviceAI]] — runs entirely offline
