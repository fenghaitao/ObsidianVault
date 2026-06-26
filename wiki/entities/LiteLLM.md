---
title: "LiteLLM"
type: entity
tags: [tool, library, llm, integration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners.md"]
last_updated: 2026-06-26
---

## Definition
LiteLLM is a library used by DSPy under the hood for LLM integration, providing a unified interface to multiple model providers.

## Key Information
- DSPy uses LiteLLM as its underlying LLM integration layer.
- Provides usage tracking information (token usage, etc.) that DSPy surfaces to users.
- Enables DSPy's model-agnostic approach by abstracting provider-specific APIs.

## Related
- [[DSPy]] — framework that uses LiteLLM
- [[OpenRouter]] — API gateway compatible with LiteLLM
- [[summary-20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners]] — source
