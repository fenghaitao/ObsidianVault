---
title: "Mixture of Experts"
type: concept
tags: [model-architecture, scaling, sparsity, heterogeneous]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum.md"]
last_updated: 2026-06-30
---

## Definition
Mixture of Experts (MoE) is a model architecture that replaces large dense models with multiple specialized "expert" sub-networks, where only a subset of experts is activated for any given input. It represents the architectural level of the shift from homogeneous to heterogeneous intelligence.

## Key Information
- Replaces large dense models as part of the transition to heterogeneous intelligence
- Operates at the architecture level of heterogeneity (alongside workflow-level multi-agent systems and hardware-level prefill-decode disaggregation)
- Each expert specializes in different aspects of the input space
- Only a subset of experts is activated per input, making computation more efficient than equivalently-sized dense models
- Part of the "mild heterogeneity" stage in the three-stage progression toward full heterogeneous intelligence
- Enables more efficient scaling than homogeneous dense models by distributing knowledge across specialized components

## Related
- [[Heterogeneous Intelligence]] — the broader paradigm shift MoE is part of
- [[Multi-Agent Systems]] — workflow-level heterogeneity
- [[Prefill-Decode Disaggregation]] — hardware-level heterogeneity
- [[summary-20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum]] — source
