---
title: "Claude4.5Sonnet"
type: entity
tags: [claude, model, anthropic, agents, context-aware]
sources: ["raw/01-articles/claude/2025-09-29 - Managing context on the Claude Developer Platform.md"]
last_updated: 2026-06-28
---

## Definition

Claude Sonnet 4.5 is an Anthropic model released in September 2025, positioned as the best model for building AI agents. It adds built-in context awareness — tracking available tokens throughout a conversation — on top of the Claude 4 Sonnet foundation, enabling more effective autonomous context management.

## Key Information

- Released alongside [[ContextEditing]] and the memory tool on the Claude Developer Platform (September 29, 2025).
- **Context awareness**: Tracks available tokens throughout conversations, enabling proactive context management rather than reactive truncation.
- Described by Anthropic as "the best model in the world for building agents" at time of release.
- Supports processing entire codebases, analyzing hundreds of documents, and maintaining extensive tool interaction histories.
- Powers both [[ContextEditing]] (automatic stale-content removal) and the memory tool (file-based persistent storage) as the underlying model.

## Capabilities

- All capabilities of [[Claude4Sonnet]] (reasoning, analysis, agentic tasks)
- Built-in token tracking and context awareness
- Enhanced long-running agentic task performance
- Works with context editing for automatic context pruning
- Works with the memory tool for cross-session persistence

## Availability

- [[Anthropic]] Claude Developer Platform (public beta as of September 2025)
- [[AmazonBedrock]] (Amazon Web Services)
- [[VertexAI|Google Cloud Vertex AI]]

## Related

- [[Claude4Sonnet]] — predecessor model in the Claude 4 Sonnet line
- [[Claude4]] — the parent model family
- [[ContextEditing]] — context management feature powered by this model
- [[AgenticMemory]] — memory tool capability available with this model
- [[ContextWindow]] — the constraint this model is designed to manage more effectively
- [[AIAgent]] — primary use-case target for this model
- [[AmazonBedrock]] — deployment platform
- [[VertexAI]] — deployment platform
- [[Anthropic]] — creator
- [[summary-2025-09-29 - Managing context on the Claude Developer Platform]] — source article
