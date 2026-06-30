---
title: "Granola"
type: entity
tags: [product, company, meeting-notes, ai, transcription, desktop-app]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - Feedback Loops are All You Need — Mehedi Hassan, Granola.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260516 - How to Leverage Domain Expertise — Chris Lovejoy, Notius Labs.md"]
last_updated: 2026-06-30
---

## Definition
Granola (formerly known as Cronulla) is a meeting notes app that provides real-time transcription and AI-generated summaries. It sits on your desktop, captures system audio and microphone audio for transcription, and allows users to write their own notes on top of the transcription for personalized meeting summaries.

## Key Information
- **Product philosophy**: Best-in-class meeting notes that "don't get in your way" — the product stays unobtrusive
- **Real-time transcription**: Captures system transcription audio and microphone audio simultaneously
- **AI-generated notes**: At the end of a meeting, generates comprehensive summaries aligned to what the user would normally write on a notepad
- **User co-authoring**: Users can write their own notes alongside the transcription, and the AI incorporates those into the final summary
- **AI chat feature**: Users can ask questions about meetings across shared context
- **Desktop app**: Built with [[Electron]], which means only one instance can run at a time
- **Custom tracing tools**: Built in-house tracing system with full visibility over LLM tool calls, reasoning, and costs, accessible to product, data, and CX teams — not just engineers
- **Web shell approach**: Turned the Electron front-end into a web shell for rapid parallel testing with PR preview links
- **Evaluated Tauri**: Considered migrating from Electron to Tauri but didn't see massive performance gains, which is their primary concern
- **Multi-persona outputs**: Different roles (sales, engineering, HR) need different summary styles from the same meeting data
- **Domain expert model (Oracle)**: Joe (first employee, writer/journalist background) serves as primary gatekeeper of AI quality — wrote all prompts, did extensive user research, and directly iterates on outputs. This is a classic [[Domain Expert as Oracle]] model where one person handles both assessment and improvement.
- **Valuation**: Passed $1 billion valuation

## Related
- [[Mehedi Hassan]] — Product Engineer at Granola
- [[Product Feedback Loops]] — Granola's approach to AI product development
- [[Web Shell Pattern]] — pattern Granola uses for rapid testing
- [[Custom Tracing Tools]] — Granola's in-house LLM observability
- [[Electron]] — desktop framework used by Granola
- [[Domain Expert as Oracle]] — Granola's domain expert model
- [[ChrisLovejoy]] — cited Granola as Oracle model case study
- [[summary-20260510 - Feedback Loops are All You Need — Mehedi Hassan, Granola]] — source transcript
- [[summary-20260516 - How to Leverage Domain Expertise — Chris Lovejoy, Notius Labs]] — source talk referencing Granola
