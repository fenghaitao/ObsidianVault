---
title: "Context Anxiety"
type: concept
tags: [ai, context-management, models, agent-behavior, long-running-agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson.md"]
last_updated: 2026-06-30
---

## Definition
Context Anxiety is a model behavior where an AI agent becomes "nervous" as it approaches the end of its context window, causing it to rush through remaining work, make hasty decisions, and prematurely declare tasks complete. It is one of the three key challenges for long-running autonomous agents, alongside context rot and planning limitations.

## Key Information
- **Behavior**: As the model nears its context window limit, it "just quickly hurries up to finish what it's doing" — rushing decisions, skipping verification, declaring incomplete work as done
- **Root Cause**: The model becomes aware (through training or context tracking) that it's running out of space, triggering urgency behaviors
- **Model-Dependent**: Opus 4.5 exhibited "really bad context anxiety." Opus 4.6 does not — this was specifically addressed in post-training
- **Mitigation Approaches**: (1) Context resetting between sessions (fresh context windows). (2) Compaction to reclaim space. (3) Larger context windows (1M context GA). (4) Model improvements through post-training
- **Relationship to Compaction**: Compaction alone doesn't solve context anxiety — even with compaction, the model may still feel pressure if it tracks remaining context budget
- **Harness Evolution**: As models improve (e.g., from Opus 4.5 to 4.6), harness patterns that compensated for context anxiety (like session resetting) can be dropped entirely
- **Smart Zone / Dumb Zone**: Related concept — models perform worse beyond certain context depths (~100K tokens in the "smart zone"). Context anxiety compounds this degradation

## Related
- [[summary-20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson]] — source
- [[Context Rot]] — related context degradation phenomenon
- [[Context Management]] — broader category of context handling
- [[Compaction]] — mitigation technique
- [[Smart Zone and Dumb Zone]] — related concept about context depth and performance
- [[One Million Context Window]] — larger context windows reduce anxiety
- [[Harness Evolution]] — how harnesses adapt as context anxiety is resolved
- [[Server-Side Compaction]] — enables indefinite runs without anxiety
