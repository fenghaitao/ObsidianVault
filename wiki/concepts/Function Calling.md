---
title: "Function Calling"
type: concept
tags: [gemini, tool, api, agent]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240724 - From Software Developer to AI Engineer： Antje Barth.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-26
---

## Definition
Function Calling is a Gemini capability that allows models to invoke external tools and APIs as part of their response generation, enabling integration with external systems and data sources.

## Key Information
- Available as a configurable tool in AI Studio and via Gemini APIs
- Allows Gemini models to call external functions and APIs
- Gemini Live supports custom function calls and automatic function responses
- Enables models to interact with external systems beyond their training data
- Can be combined with other tools like code execution and search grounding
- Demonstrated in the context of Gemini Live for real-time tool invocation
- Amazon Bedrock's Converse API provides built-in function calling support via a tool list passed to the API call
- Antje Barth describes function calling as giving models "access to additional systems" in application code

## Related
- [[summary-20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind]] — source
- [[summary-20240724 - From Software Developer to AI Engineer： Antje Barth]] — source (function calling via Bedrock Converse API)
- [[AI Studio]] — platform where it's available
- [[Gemini 3.1 Flash Live]] — model supporting function calling in real-time
- [[Code Execution (Sandboxed)]] — related tool capability
- [[ToolCalling]] — broader concept
- [[Converse API]] — Bedrock API with built-in function calling
- [[AmazonBedrock]] — platform supporting function calling
