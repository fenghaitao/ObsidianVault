---
title: "OpenRouter"
type: entity
tags: [tool, api, llm, gateway]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI.md"]
last_updated: 2026-06-29
---

## Definition
OpenRouter is an API gateway that provides unified access to multiple LLM providers through a single API key, used in DSPy demonstrations for model mixing.

## Key Information
- Used in Kevin Madura's DSPy workshop to access multiple models (Claude, Gemini, GPT-4.1 mini) through a single API.
- Enables model mixing strategies where different LLMs are used for different workloads within the same DSPy program.
- Simplifies the process of testing and comparing model performance across providers.

- Paperclip uses OpenRouter via OpenClaw as an agent integration, enabling access to many models including free ones like Qwen 3.6+
- **n8n Integration**: Used in Liam McGarrigle's n8n workshop as the LLM provider for the AI agent node. OpenRouter enables switching between any model (GPT-5.3, Claude Opus 4.6, etc.) through a single API key. A shared workshop key was provided to attendees
- **Voice AI context**: Neil Zeghidour cited OpenRouter as an example of tool call latency being the real bottleneck for voice AI — tool calls via OpenRouter have latency between 500ms and 4 seconds, dwarfing the 10-20ms TTS latency improvements that the industry focuses on

## Related
- [[DSPy]] — framework demonstrated using OpenRouter
- [[LiteLLM]] — library that can interface with OpenRouter
- [[Paperclip]] — agent orchestrator using OpenRouter for BYO-agent
- [[BringYourOwnAgent]] — concept enabled by OpenRouter integration
- [[summary-20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners]] — source
- [[summary-20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa]] — source
- [[n8n]] — platform using OpenRouter for LLM access
- [[summary-20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle]] — source
- [[summary-20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI]] — source (tool call latency)
- [[Tool Calling]] — latency bottleneck in voice AI
- [[Voice AI]] — domain where OpenRouter latency is relevant
