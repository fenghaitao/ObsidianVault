---
title: "Sonnet"
type: entity
tags: [model, llm, anthropic, claude]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md"]
last_updated: 2026-06-26
---

## Definition
Sonnet is Anthropic's Claude model family. It is referenced as one of the backend LLMs powering Amazon Kiro's agent interactions.

## Key Information
- Referenced as a backend LLM for Kiro: "you're talking to sort of an amalgam of systems... when you're chatting, you are talking to just an LLM" (Sonnet or Gemini)
- Kiro uses Sonnet-class models with ~200k token context limits
- Prompt caching with Sonnet-class models achieves 90-95% cache hit rate in Kiro
- Kiro's summarization feature and session management are designed around Sonnet-class token limits

## Related
- [[summary-20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro]] — source
- [[Anthropic]] — creator of the Sonnet model family
- [[AmazonKiro]] — IDE that uses Sonnet as a backend
- [[Gemini3]] — alternative backend model also used by Kiro
