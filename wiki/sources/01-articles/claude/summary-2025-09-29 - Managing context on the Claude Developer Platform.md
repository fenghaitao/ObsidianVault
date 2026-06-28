---
title: "summary-2025-09-29 - Managing context on the Claude Developer Platform.md"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2025-09-29 - Managing context on the Claude Developer Platform.md"]
last_updated: 2026-06-28
---

## Core Summary

Anthropic introduced two new context management capabilities on the Claude Developer Platform — context editing and the memory tool — enabling AI agents to handle long-running tasks without hitting context limits or losing critical information. Together, these features improve agentic task performance by 39% over baseline.

## Key Points

- **Context Editing**: Automatically clears stale tool calls and results from within the context window when approaching token limits. Preserves conversation flow while removing stale content, effectively extending how long agents can run without manual intervention. Delivered a 29% performance improvement alone; reduced token consumption by 84% in a 100-turn web search evaluation.
- **Memory Tool**: Enables Claude to store and consult information outside the context window via a file-based CRUD system (create, read, update, delete). Files are stored in a dedicated memory directory in the developer's own infrastructure, persisting across conversations. Operates entirely client-side through tool calls — developers control the storage backend.
- **Claude Sonnet 4.5**: Described as "the best model in the world for building agents." Includes built-in context awareness, tracking available tokens throughout conversations to manage context more effectively.
- **Combined performance**: Combining the memory tool with context editing improved performance by 39% over baseline on an internal agentic search evaluation set.
- **Availability**: Public beta on the Claude Developer Platform, natively and via [[AmazonBedrock]] and [[VertexAI|Google Cloud Vertex AI]].
- **Key use cases unlocked**: Processing entire codebases, analyzing hundreds of documents, maintaining extensive tool interaction histories across multi-step workflows.

## Related

- [[ContextEditing]] — the context management concept introduced in this article
- [[AgenticMemory]] — the broader concept of agent memory; memory tool is a specific platform implementation
- [[ContextWindow]] — the fundamental constraint that these features address
- [[Claude4.5Sonnet]] — the model featured in this announcement with built-in context awareness
- [[AIAgent]] — the primary beneficiary of these context management capabilities
- [[AmazonBedrock]] — platform where these features are available
- [[VertexAI]] — platform where these features are available
- [[Anthropic]] — author and platform provider
