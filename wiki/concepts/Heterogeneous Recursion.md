---
title: "Heterogeneous Recursion"
type: concept
tags: [technique, long-context, multi-model, recursive-language-models, optimization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum.md"]
last_updated: 2026-06-30
---

## Definition
Heterogeneous Recursion is a technique developed by [[Callosum]] that extends recursive language models (MIT, Oct 2024) by mapping sub-contexts generated during recursive decomposition to different chips and different models, rather than using a single model on a single chip. This achieves dramatic cost and speed improvements while emulating frontier model intelligence.

## Key Information
- Extension of **recursive language models** where context is treated as an environment and interacted with programmatically via Python REPL (keyword search, regex, context extraction)
- Instead of spawning identical recursive agents, sub-contexts are mapped to the optimal model/chip combination based on task complexity
- Results on ULong benchmark vs GPT-5.2:
  - **Cerebras**: 7x cheaper, 5x faster (~$0.54/task vs $3.75, ~400s vs 2000s)
  - **SambaNova**: 12x cheaper, 3x faster (lower cost but higher latency tradeoff)
- Automation layer detects task complexity and automatically predicts the best model and hardware
- Demonstrates architectural decisions (hardware + model selection) creating massive price/performance differences

## Related
- [[Recursive Language Models]] — base technique extended by heterogeneous recursion
- [[Callosum]] — company that developed the technique
- [[Heterogeneous Intelligence]] — overarching paradigm
- [[Cerebras]] — hardware partner (low-latency option)
- [[SambaNova]] — hardware partner (low-cost option)
- [[Context Rot]] — the problem recursive/heterogeneous recursion solves
- [[summary-20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum]] — source
