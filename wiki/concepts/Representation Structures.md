---
title: "Representation Structures"
type: concept
tags: [ai, data-structures, knowledge-management, context, agent-design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260525 - Bounded Autonomy： Between Free Will and Determinism — Angus J. McLean, Oliver.md"]
last_updated: 2026-06-30
---

## Definition
Representation structures are the multiple data organization formats used to store and retrieve information for AI agents. The core insight is that no single representation structure is optimal for all tasks — different structures serve different purposes, and effective agent design uses a combination of them.

## Key Information
- Introduced by Angus J. McLean as practical guidance for agent builders.
- The five key representation structures:
  - **Markdown**: for human-readable hierarchy and authoring — best for documents, specifications, and structured text.
  - **Graph relationships**: for references and connections — best for navigating related entities and concepts.
  - **Clustering**: for large or unstructured bodies of text — best for discovering patterns in data.
  - **Folders**: for fast retrieval — best when you need to find specific items quickly.
  - **Timelines**: for chronological relevance — best when temporal ordering matters.
- The choice of representation structure is not about the inherent nature of the data but about what the observer (the agent or human) needs from it.
- Since AI is fundamentally translation between representations, the same content can and should exist in multiple representation structures simultaneously.
- This connects to the idea that structure is a property of the observer's representation, not an inherent property of the data object itself.
- Practical implication: agent systems should support translating content between representation structures as needed for different tasks.

## Related
- [[Angus J. McLean]] — speaker who introduced the concept
- [[summary-20260525 - Bounded Autonomy： Between Free Will and Determinism — Angus J. McLean, Oliver]] — source
- [[AI as Translation]] — the parent concept enabling multiple representations
- [[Knowledge Graphs]] — graph-based representation structure
- [[Context Graphs]] — graph-based context representation
- [[MarkdownAsCode]] — markdown as a representation for agents
- [[Knowledge Base Kanban]] — folder-based representation for knowledge management
- [[File System Memory]] — folder-based agent memory
