---
title: "summary-2026-06-08 - Building intelligent apps for Apple platforms with Claude in the Foundation Models framework"
type: source
tags: [source, claude-blog, apple, swift]
sources: ["raw/01-articles/claude/2026-06-08 - Building intelligent apps for Apple platforms with Claude in the Foundation Models framework.md"]
last_updated: 2026-07-07
---

## Core Summary

Anthropic released a Swift package that connects Apple's Foundation Models framework to Claude, enabling Apple platform developers to hand off complex reasoning tasks from on-device models to Claude while preserving typed Swift outputs. The integration works across iOS 27, iPadOS 27, macOS 27, visionOS 27, and watchOS 27, and supports streaming, tool calls, web search, and code execution. This allows apps to use Apple's on-device models for fast local tasks and seamlessly escalate to Claude for multi-step reasoning, code generation, and data analysis within the same user experience.

## Key Points

- A new Swift package enables Claude as a backend for Apple's Foundation Models framework, available on iOS 27, iPadOS 27, macOS 27, visionOS 27, and watchOS 27.
- Apple's Foundation Models framework provides typed Swift outputs via @Generable annotations, giving Claude clean structured inputs instead of raw user text.
- The integration handles streaming, tool calls, and structured responses back into SwiftUI views.
- Use cases include journaling apps finding thematic threads across months of entries, and study apps escalating from on-device definitions to multi-step conceptual reasoning with Claude.
- Developers sign in with an Anthropic API key to enable the Claude handoff.

## Related

- [[AppleFoundationModels]] — Apple's native Swift framework for on-device model access
- [[ModelHandoff]] — the pattern of escalating from on-device to cloud models
- [[Claude]] — the AI model family powering the cloud-side reasoning
- [[Anthropic]] — creator of Claude and the Swift package
