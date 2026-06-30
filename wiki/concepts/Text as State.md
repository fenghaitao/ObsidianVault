---
title: "Text as State"
type: concept
tags: [agents, llm, state, context, semantic-meaning, data-structures]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition

Text as State is the paradigm shift where unstructured text and context replace traditional structured data (Booleans, flags, data structures) as the primary mechanism for tracking application state in agent-based systems. LLMs can understand semantic meaning from text, enabling dynamic, context-rich interactions that structured data alone cannot capture.

## Key Information

- **Traditional software**: State was tracked via Boolean flags, enums, and well-defined data structures. Everything could be checked deterministically: `if user.isEuropean then use Celsius`
- **Agent systems**: State lives in text and context. The LLM understands semantic meaning from natural language, allowing dynamic interpretation of preferences, constraints, and intent
- **Deep research example**: A traditional system would require a multi-step decline/replan cycle to adjust a research plan. With text as state, the user can approve the plan while simultaneously providing additional constraints ("focus on US market, ignore California") — all in one natural language interaction
- **Memory and personalization**: User preferences that vary by context can't be mapped to static flags. Example: a European user who prefers Celsius generally but Fahrenheit for cooking. Previously this required explicit profile flags; now the LLM can dynamically interpret preferences from natural language context
- **Beyond text**: The broader principle includes images, video, and audio — any modality the LLM can interpret becomes potential state
- **Implication**: We no longer operate in purely clear, structured data concepts. State becomes fluid, contextual, and interpreted by the model rather than checked by code

## Related

- [[summary-20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind]] — source
- [[PhilippSchmid]] — speaker
- [[Context as Code]] — related concept: context as the programming medium
- [[Context Engineering]] — the discipline of managing context as state
- [[Preserve Meaning]] — complementary principle: everything is context now
- [[Semantic Understanding]] — the LLM capability that enables text as state
- [[Non-Deterministic Agents]] — agents where state is fluid and interpreted
