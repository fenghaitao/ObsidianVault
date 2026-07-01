---
title: "Full Duplex"
type: concept
tags: [voice-ai, conversation, speech, architecture, interaction]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI.md"]
last_updated: 2026-06-29
---

## Definition
Full duplex in voice AI refers to true bidirectional conversation where both the user and the AI can speak simultaneously, with the system handling overlapping speech, interruptions, back-channeling ("mhm", "uh huh"), coughing, and other natural conversational phenomena. It mimics human conversation patterns where overlap is common and often meaningful.

## Key Information
- Human conversation is full duplex: people overlap, interrupt, back-channel, and speak simultaneously
- Back-channeling ("mhm", "uh huh") is a sign of active listening and politeness in many cultures
- In Japanese conversation, up to 20% of the time involves overlapping speech due to back-channeling as politeness
- Every speech-to-speech model except Moshi is half duplex — either listening or speaking, not both
- Half duplex breaks on: simultaneous speaking, coughing, back-channeling
- Moshi (2 years old as of May 2026) is still the only full-duplex model
- Moshi can: start answering before user finishes, handle user talking over it, process what was said during overlap
- Moshi's conversational flow is described as "impossible to match"
- Full duplex alone is insufficient — Moshi lacked intelligence, tool calling, and observability
- Nvidia's PersonalPlex is based on Moshi's full-duplex architecture
- Speech-to-speech models natively enable full-duplex and better handling of interruptions/barge-ins compared to pipeline architectures

## Related
- [[summary-20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI]] — source
- [[summary-20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI]] — source
- [[Half Duplex]] — the current limitation of most models
- [[Back Channeling]] — key conversational phenomenon
- [[Moshi]] — only full-duplex implementation
- [[PersonalPlex]] — Nvidia model based on Moshi
- [[SpeechToSpeech Models]] — model category
- [[Voice AI]] — parent domain
- [[Her Moment]] — full duplex is required for this
