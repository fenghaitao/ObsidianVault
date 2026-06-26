---
title: "Structured Outputs"
type: concept
tags: [llm, outputs, api, data]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240805 - What's new from Anthropic and what's next： Alex Albert.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Structured outputs are language model responses formatted in structured data formats (JSON, typed objects) rather than free text, enabling programmatic processing and integration into applications.

## Key Information
- **Anthropic / Claude 3.5 Sonnet**: Consistent structured JSON output enabled through the Tool Use API, allowing developers to give Claude hundreds of tools with structured output schemas
- Every Manus web application ships with a language model capable of structured outputs
- Used in the French learning app for inline corrections with structured feedback
- Manus supports any language model provider for structured outputs
- Enables deterministic parsing of agent responses for downstream processing
- Combined with Whisper for audio transcription in the language learning demo
- Structured outputs allow agents to return typed data that applications can directly consume
- Available as a configurable tool in Google's AI Studio for Gemini models

## Related
- [[summary-20240805 - What's new from Anthropic and what's next： Alex Albert]] — source for Anthropic structured JSON output
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[summary-20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind]] — source
- [[ManusAI]] — platform supporting structured outputs
- [[Agent Sandbox]] — environment where structured outputs are generated
- [[File Upload for Agents]] — input method paired with structured output analysis
- [[AI Studio]] — platform with structured outputs tool
