---
title: "GeminiInteractionsAPI"
type: entity
tags: [api, google, deepmind, gemini, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
The Gemini Interactions API is a unified API from Google DeepMind (launched in beta December 2025) that supports both models and agents through a single interface. It replaces the legacy Generate Content API with server-side state management, type-based content blocks, built-in agents (like Deep Research), background execution, and implicit caching.

## Key Information
- Launched in beta in December 2025 alongside Deep Research
- Unified API for both models and agents — switch between them by changing the model/agent definition
- Server-side state management via previous interaction IDs eliminates client-side history management
- Type-based content blocks: every input/output has a type field (function call, thought signature, text, audio, video, image)
- Less proto-specific and less GRPC-oriented than Generate Content, more aligned with industry standards (OpenAI, Anthropic)
- Supports built-in tools, remote MCP, and tool combination (Google Search + custom functions, launched ~2 weeks before April 2026)
- Background execution support with polling or webhooks for long-running agent tasks
- Streaming via SSE (Server-Sent Events)
- Implicit caching: server-side state leads to 2-3x better cache hit rates compared to client-managed history
- Input caching is 90% cheaper for input tokens
- Free tier stores interactions for 1 day; paid tier stores for 55 days
- Coming to Vertex AI with more storage flexibility
- Content blocks make chaining models easy (e.g., Nano Banana for images, Lyra for audio, Flash for text)
- Supports both server-side state mode and client-managed history mode

## Related
- [[summary-20260430 - Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind]] — source
- [[GoogleDeepMind]] — developer
- [[PhilippSchmid]] — presenter
- [[GeminiLiveAPI]] — sister API (Live API coming to Interactions API)
- [[Gemini3]] — model used with this API
- [[ServerSideStateManagement]] — key feature
- [[ImplicitCaching]] — key benefit
- [[ToolCombination]] — key feature
- [[BackgroundExecution]] — key feature
- [[MCP]] — remote MCP support
