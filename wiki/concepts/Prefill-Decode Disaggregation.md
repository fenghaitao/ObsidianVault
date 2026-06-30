---
title: "Prefill-Decode Disaggregation"
type: concept
tags: [hardware, inference, optimization, heterogeneous, architecture]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum.md"]
last_updated: 2026-06-30
---

## Definition
Prefill-Decode Disaggregation is a hardware-level technique in the heterogeneous intelligence paradigm where the prefill (prompt processing) and decode (token generation) phases of LLM inference are separated onto different hardware, replacing the single-chip approach of homogeneous systems. It represents the hardware layer of the shift toward heterogeneity.

## Key Information
- Separates the two phases of LLM inference: prefill (processing the input prompt) and decode (generating output tokens)
- Different phases have different computational characteristics: prefill is compute-bound, decode is memory-bandwidth-bound
- By disaggregating, each phase can run on hardware optimized for its specific demands
- Part of the "mild heterogeneity" stage alongside [[Mixture of Experts]] (architecture) and [[Multi-Agent Systems]] (workflow)
- Represents the hardware dimension of the three-level heterogeneous optimization framework
- Enables more efficient resource utilization than homogeneous single-chip deployments

## Related
- [[Heterogeneous Intelligence]] — the paradigm this technique supports
- [[Mixture of Experts]] — architecture-level heterogeneity
- [[Multi-Agent Systems]] — workflow-level heterogeneity
- [[summary-20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum]] — source
