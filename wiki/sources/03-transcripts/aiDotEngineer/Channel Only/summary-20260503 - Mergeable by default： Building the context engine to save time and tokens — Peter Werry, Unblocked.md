---
title: "summary-20260503 - Mergeable by default： Building the context engine to save time and tokens — Peter Werry, Unblocked"
type: source
tags: [source, transcript, context-engineering, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - Mergeable by default： Building the context engine to save time and tokens — Peter Werry, Unblocked.md"]
last_updated: 2026-06-29
---

## Core Summary

Peter Werry from Unblocked presents on building context engines to make AI agents "mergeable by default." He traces the evolution from fancy autocomplete (2022) through curated context to background agents running in YOLO mode. The core thesis: without a context engine that understands code, organization, and historical motivations, agents end up in doom loops. He debunks three myths about context engines and shares lessons from building Unblocked's context engine, then runs a workshop on building a social engineering graph component.

## Key Points

- Context engines supply exactly the context agents need and none they don't, optimizing tokens and time.
- Evolution: 2022 fancy autocomplete (8K tokens) → curated context → parallel agents with MCP/skills → background agents (YOLO mode).
- Three myths: context engines are just RAG, more context is always better, and access equals understanding.
- Without context engines, agents hit doom loops where they iterate incorrectly without human intervention.
- The social engineering graph maps relationships between code, people, and organizational decisions.
- Unblocked builds context engines for enterprise codebases.

## Related

- [[Unblocked]] — company building context engines
- [[ContextEngineering]] — art of curating context windows
- [[ContextManagement]] — techniques for managing agent context
- [[DoomLoop]] — failure mode addressed by context engines
