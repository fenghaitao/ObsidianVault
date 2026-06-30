---
title: "Homogeneous Intelligence"
type: concept
tags: [ai-paradigm, scaling, training, neural-scaling-laws]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum.md"]
last_updated: 2026-06-30
---

## Definition
Homogeneous Intelligence is the prevailing AI paradigm of scaling single models on a fleet of identical chips, largely driven by neural scaling laws showing that more data and more parameters lead to better models. It is primarily rooted in the training domain and becomes less relevant as the field shifts toward inference.

## Key Information
- Driven by the discovery of neural scaling laws: more data + more parameters = better models
- Primarily effective in the training domain, less relevant for inference
- Represents the first two eras of compute: CPU (quicker) and GPU/parallel ([[Nvidia]]-dominated)
- Already being displaced by heterogeneous approaches: [[Mixture of Experts]] replacing dense models, [[Multi-Agent Systems]] replacing single LLM calls, prefill-decode disaggregation replacing single chips
- Inefficient for real-world problems that decompose into sub-problems requiring different types of intelligence
- Under the production function framework: homogeneous systems can only scale a single peak (specialist) or produce a broad-but-shallow cylinder (generalist), neither of which matches diverse demand functions well

## Related
- [[Heterogeneous Intelligence]] — the emerging paradigm replacing homogeneous scaling
- [[Neural Scaling Laws]] — the empirical discovery driving homogeneous scaling
- [[Three Eras of Compute]] — framing homogeneous as the first two eras
- [[Mixture of Experts]] — architectural shift away from homogeneous dense models
- [[summary-20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum]] — source
