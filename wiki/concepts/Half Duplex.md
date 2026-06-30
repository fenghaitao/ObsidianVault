---
title: "Half Duplex"
type: concept
tags: [voice-ai, conversation, speech, architecture, limitation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI.md"]
last_updated: 2026-06-29
---

## Definition
Half duplex in voice AI means the model can either listen or speak at any given moment, but not both simultaneously. This is the current state of every speech-to-speech model except Moshi, including OpenAI's advanced voice mode and Sesame AI's voice model. Half duplex systems break on overlapping speech, back-channeling, coughing, and other natural conversational behaviors.

## Key Information
- Model is either in listening mode or speaking mode — never both
- Cannot handle: simultaneous speaking, back-channeling ("mhm"), coughing, interruptions
- Demo showed a half-duplex model constantly interrupting when the user tried to back-channel
- User: "Yeah, exactly" → Model treats it as an interruption and stops → User: "No, I didn't mean to interrupt"
- Half duplex is why most voice AI demos are shot in quiet rooms next to the phone
- Full duplex is needed for truly natural conversation
- Even the "best" speech-to-speech models (OpenAI, Sesame AI) are half duplex as of May 2026
- Cultural implications: makes voice AI unusable in cultures where back-channeling is essential (e.g., Japanese)

## Related
- [[summary-20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI]] — source
- [[Full Duplex]] — the desired alternative
- [[Back Channeling]] — conversational behavior that breaks half duplex
- [[Speech-to-Speech Models]] — model category with this limitation
- [[Voice AI]] — parent domain
- [[Moshi]] — the only full-duplex exception
