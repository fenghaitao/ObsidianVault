---
title: "State Space Models"
type: concept
tags: [AI, ML, architecture, sequence-modeling]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260126 - Ex-Citadel Quant and AI Researcher： Breaking In, Tech vs Finance Careers ｜ Nimit Sohoni.md"]
last_updated: 2026-09-14
---

## Definition

State space models (SSMs) are a sequence-modeling architecture that compresses context into a fixed-size state, in contrast to transformers, whose key-value (KV) cache grows linearly with sequence length.

## Key Information

- Transformers store a representation of each token in a KV cache that grows with sequence length (Nimit analogizes transformers to a database that can recall anything in context).
- SSMs take in information, process it, and keep it in a fixed-size state; per-step cost and memory do not grow with sequence length (analogized to a brain).
- Trade-off: pure SSMs can lag transformers on recall- or fact-heavy tasks because transformers' exact in-context recall is useful there; SSMs scale as well or better on other tasks for a fixed budget.
- Hybrid models interleave SSM and transformer layers; Nimit cites NVIDIA's work and recent "Quinn" open-source models as following this strategy, calling hybrids the cutting edge for open-source text.
- SSMs are especially suited to low-information modalities: Cartesia found using SSMs for audio is "almost a free lunch" (better quality and faster inference), since a 10–100 ms audio frame contains little information and compresses well vs densely informational text.
- Mamba (by Albert Gu) demonstrated that SSMs can beat "just scale transformers," inspiring Cartesia's architectural direction.

## Related

- [[summary-20260126 - Ex-Citadel Quant and AI Researcher： Breaking In, Tech vs Finance Careers ｜ Nimit Sohoni]] — source summary
- [[Nimit Sohoni]] — explained the SSM vs transformer distinction
- [[Albert Gu]] — advanced SSMs via Mamba
- [[Cartesia]] — applies SSMs to audio
- [[Machine Learning]] — broader field context
