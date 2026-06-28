---
title: "ContextEngineering"
type: concept
tags: [agent, context, memory, file-system, agentic]
sources: ["raw/01-articles/claude/2025-09-29 - Building agents with the Claude Agent SDK.md"]
last_updated: 2026-06-28
---

## Definition

Context engineering is the practice of deliberately designing an agent's environment — particularly its file and folder structure — so that the right information flows into the model's context window at the right time. Rather than loading everything upfront, the agent selects what to read based on the task at hand.

## Key Information

- The file system represents information that *could* be pulled into the model's context. How that information is organized determines how efficiently the agent can retrieve it.
- In [[ClaudeAgentSDK]], Claude uses bash tools (`grep`, `tail`) to perform agentic search: selectively loading only relevant portions of large files (logs, conversation histories, user uploads) rather than ingesting everything.
- Folder structure becomes a first-class design decision: an email agent storing conversations in a `Conversations/` folder can search that folder for relevant context on demand.
- Context engineering is an alternative framing to (and complement of) [[RetrievalAugmentedGeneration]]: where RAG chunks and embeds data into vectors, context engineering relies on the agent to navigate the raw file system directly.

### Agentic Search vs. Semantic Search

| Dimension | Agentic Search (context engineering) | Semantic Search ([[RetrievalAugmentedGeneration|RAG]]) |
|---|---|---|
| Speed | Slower | Faster |
| Accuracy | Higher | Lower |
| Transparency | High (bash commands visible) | Lower (embedding/vector black box) |
| Maintenance | Simpler | More complex (chunking, embeddings) |
| Recommendation | Start here | Add only when speed is critical |

### Relationship to Compact Feature

When context accumulates during long agent runs, the [[ClaudeAgentSDK]]'s compact feature summarizes prior messages automatically — ensuring the context window remains usable without manual intervention.

### Relationship to Subagents

[[ClaudeCodeSubagents]] complement context engineering: subagents run in isolated [[ContextWindow|context windows]], performing targeted searches and returning only the relevant excerpts. This keeps the orchestrator's context clean even when the search space is large.

## Related

- [[summary-2025-09-29 - Building agents with the Claude Agent SDK]] — source article introducing this framing
- [[ClaudeAgentSDK]] — the SDK where context engineering is a first-class pattern
- [[ClaudeCode]] — the tool that pioneered agentic file-system navigation
- [[RetrievalAugmentedGeneration]] — the vector-search alternative to agentic file-system navigation
- [[ContextWindow]] — the resource context engineering is designed to manage efficiently
- [[ClaudeCodeSubagents]] — isolated context windows for parallel context gathering
- [[AIAgent]] — the broader agent paradigm context engineering serves
