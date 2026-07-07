---
title: "AppleFoundationModels"
type: entity
tags: [apple, swift, framework, on-device-ai, ios]
sources: ["raw/01-articles/claude/2026-06-08 - Building intelligent apps for Apple platforms with Claude in the Foundation Models framework.md"]
last_updated: 2026-07-07
---

## Definition

Apple Foundation Models is a native Swift framework that gives developers access to Apple's on-device AI models for fast, local tasks like summarization, extraction, and concept explanation. It supports guided generation with typed Swift outputs through @Generable annotations.

## Key Information

- Available on iOS 27, iPadOS 27, macOS 27, visionOS 27, and watchOS 27.
- Returns typed Swift values through guided generation in as few as three lines of code.
- Powers on-device features such as journaling prompts, document summarization, and adaptive learning explanations.
- Can integrate with [[Claude]] via a Swift package from [[Anthropic]], enabling handoff to cloud models for complex reasoning (see [[ModelHandoff]]).
- The @Generable annotation system produces clean structured inputs for downstream API calls, including the Claude handoff.

## Related

- [[summary-2026-06-08 - Building intelligent apps for Apple platforms with Claude in the Foundation Models framework]] — source summary
- [[ModelHandoff]] — the pattern of escalating from on-device to cloud models
- [[Claude]] — the AI model that extends Foundation Models with cloud reasoning
- [[Anthropic]] — creator of the Claude Swift package for Foundation Models
