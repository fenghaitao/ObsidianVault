---
title: "OpenRouter"
type: entity
tags: [tool, api, llm, gateway]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa.md"]
last_updated: 2026-06-26
---

## Definition
OpenRouter is an API gateway that provides unified access to multiple LLM providers through a single API key, used in DSPy demonstrations for model mixing.

## Key Information
- Used in Kevin Madura's DSPy workshop to access multiple models (Claude, Gemini, GPT-4.1 mini) through a single API.
- Enables model mixing strategies where different LLMs are used for different workloads within the same DSPy program.
- Simplifies the process of testing and comparing model performance across providers.

- Paperclip uses OpenRouter via OpenClaw as an agent integration, enabling access to many models including free ones like Qwen 3.6+

## Related
- [[DSPy]] — framework demonstrated using OpenRouter
- [[LiteLLM]] — library that can interface with OpenRouter
- [[Paperclip]] — agent orchestrator using OpenRouter for BYO-agent
- [[BringYourOwnAgent]] — concept enabled by OpenRouter integration
- [[summary-20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners]] — source
- [[summary-20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa]] — source
