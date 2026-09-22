---
title: "Model FLOPS Utilization"
type: concept
tags: [ML, hardware, metric]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg.md"]
last_updated: 2026-09-22
---
## Definition
Model FLOPS utilization (MFU) is the ratio of useful flops a neural net performs to the total flops the accelerator could have done in that time — a measure mistakenly read as "wastage" when naively low.
## Key Information
- To hit 100% MFU you would only run matmuls in a loop with no memory reads or other operations — not a useful computation.
- Real neural nets must apply activations, do attention, and write intermediate outputs to HBM; those use the memory bus, vector units, or run slower than peak matmul.
- Hence the low-10s MFU seen on Twitter is not naively low — it reflects the mix of memory and non-matmul operations.
- Inference co-design targets saturating all hardware units together to raise MFU while keeping quality.
- A computation never matches the natural rate of every hardware operation at once.
## Related
- [[summary-20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg]] — source summary
- [[Vlad Feinberg]] — source
- [[Inference Co-Design]] — the optimization it measures
- [[Model Quantization]] — reduces the flops needed
