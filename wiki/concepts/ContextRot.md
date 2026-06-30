---
title: "ContextRot"
type: concept
tags: [ai-systems, context-management, quality]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - No More Slop – swyx.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson.md"]
last_updated: 2026-06-25
---

## Definition
Context rot is the degradation of context quality in AI systems over extended interactions or when processing too much information, leading to lower quality outputs and increased slop.

## Key Information
- Identified as one of the biggest themes at the AI Engineer Summit
- Occurs when AI agents handle too much information over time, losing coherence and quality
- Can be fought using sub-agents that handle bounded subtasks with clean context
- Represents a structural source of slop in AI systems
- Related to the broader challenge of maintaining quality as AI systems scale in complexity and duration

## Related
- [[summary-20251222 - No More Slop – swyx]] — source
- [[summary-20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson]] — source (one of three key challenges for long-running agents)
- [[SubAgents]] — technique to fight context rot
- [[Slop]] — context rot contributes to this
- [[CodeSlop]] — context rot in coding contexts
