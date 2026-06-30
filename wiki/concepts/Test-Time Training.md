---
title: "Test-Time Training"
type: concept
tags: [training, inference, continual-learning, personalization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs.md"]
last_updated: 2026-06-30
---

## Definition
Test-time training (also called continual learning at inference) is the paradigm where model weights are updated during inference based on usage patterns and user data, rather than remaining static after initial training. This could fundamentally break cloud batching economics and make local inference 10x more competitive.

## Key Information
- Instead of a static forward pass, the model actively learns and updates weights during inference
- Each user would have their own version of model weights personalized to their usage patterns and data
- Solves the long-context/memory problem: no context limits because learning is embedded in weights, not just KV cache
- Completely breaks cloud batching: each model becomes unique, so requests can't be batched together
- On the extreme end, if the whole model changes per user, cloud unit economics collapse — local becomes 10x better relative to cloud
- More likely near-term: only a small portion of weights change, preserving some batching capability
- Alex Cheema predicts this could hit an inflection point within the year
- Related to test-time scaling (Best of N, search-based approaches) but more fundamental — actual weight updates, not just multiple passes
- Represents a shift from "learning" paradigm to "learning + search" paradigm

## Related
- [[summary-20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs]] — source
- [[BestOfN]] — related test-time scaling technique
- [[Batching]] — cloud technique that test-time training breaks
- [[Local LLM Inference]] — benefits disproportionately from this paradigm
- [[Continual Learning]] — broader field this belongs to
