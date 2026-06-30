---
title: "Fillers (Voice AI)"
type: concept
tags: [voice-ai, latency, tool-calling, conversation, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI.md"]
last_updated: 2026-06-29
---

## Definition
Fillers in voice AI are a technique where the LLM splits its output into two streams: one that sends a tool call and another that keeps the conversation going naturally while waiting for the tool call result. Once the result returns, it is inserted back into the conversation seamlessly. This mitigates the unpredictable latency of tool calls in voice agents.

## Key Information
- Addresses the tool call latency problem (500ms to 4 seconds via OpenRouter)
- LLM splits output: sends tool call + generates conversational filler simultaneously
- Filler content is contextually relevant (e.g., saying nice things about the destination while fetching travel options)
- Result is inserted back naturally when it arrives
- Live demo: travel agent filled with "Tokyo is such an incredible choice..." while fetching hotel options
- Makes latency feel more controlled and reliable despite tool call unpredictability
- Neil Zeghidour described it as "needs polishing" but the core concept works
- Tool call latency has become the main bottleneck, not TTS latency

## Related
- [[summary-20260509 - Voice AI： when is the ＂Her＂ moment — Neil Zeghidour, CEO, Gradium AI]] — source
- [[Tool Calling]] — the latency source being mitigated
- [[Cascaded Systems (Voice)]] — architecture where fillers are used
- [[Latency]] — problem being addressed
- [[Voice AI]] — parent domain
- [[OpenRouter]] — example of tool call latency source
