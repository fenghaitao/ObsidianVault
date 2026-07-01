---
title: "Preserve Meaning"
type: concept
tags: [agents, context, semantic-meaning, llm, state]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition

Preserve Meaning is the principle that in agent systems, everything is context — we no longer have well-defined data structures for all application state. The focus shifts from structured data modeling to preserving and conveying semantic meaning through text and context that LLMs can interpret.

## Key Information

- **Articulated by Philipp Schmid** as a core principle for agent building
- **The shift**: Traditional software modeled everything in data structures — user preferences as flags, workflow states as enums, decisions as Booleans. Agent systems carry state as natural language context
- **Semantic richness**: Natural language can express nuance that structured data cannot. A user preference like "I'm European so I use Celsius, but Fahrenheit for cooking" has semantic meaning that a simple `useFahrenheit: false` flag loses
- **Context is everything**: Every piece of information the agent might need — user preferences, conversation history, domain knowledge, tool outputs — becomes part of the context. The quality of the context determines the quality of the agent's decisions
- **Implication for system design**: Instead of designing database schemas for state, design context assembly and management strategies. What context does the agent need? How is it assembled? How is it preserved across interactions?
- **Beyond text**: Images, video, audio — any modality the LLM can interpret becomes part of the preserved meaning
- **Contrast with traditional state machines**: Traditional state machines have explicit, finite states with defined transitions. Agent state is fluid, contextual, and interpreted by the model

## Related

- [[summary-20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind]] — source
- [[PhilippSchmid]] — speaker
- [[Text as State]] — the specific mechanism this principle describes
- [[ContextEngineering]] — the discipline of managing meaning-rich context
- [[Context Management]] — practical techniques for preserving meaning
- [[Semantic Understanding]] — the LLM capability that makes this possible
- [[Agent Memory]] — how preserved meaning persists across interactions
