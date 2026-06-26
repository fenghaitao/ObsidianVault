---
title: "MiniMax"
type: entity
tags: [company, ai, llm, china]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is.md"]
last_updated: 2026-06-25
---

## Definition
MiniMax is a Chinese AI lab behind MiniMax M2, a state-of-the-art open model that deliberately chose to use standard quadratic attention rather than more efficient hybrid architectures, concluding that the efficiency-performance trade-off was not worth it.

## Key Information
- Released MiniMax M2, one of the state-of-the-art open models as of late 2025
- Deliberately chose not to use hybrid attention architectures (linear, sparse, sliding window)
- Published a detailed explanation of why they stuck with quadratic attention: more efficient architectures have an inherent trade-off in computation vs. quality
- Their findings support the argument that even if you can technically build models that don't break at millions of tokens, they aren't actually better at reasoning tasks

## Related
- [[summary-20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is]] — source
- [[ContextBroad]] — related limitation they implicitly acknowledge
