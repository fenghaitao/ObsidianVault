---
title: "Performance Models"
type: concept
tags: [model-optimization, efficiency, compression, pruna]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna.md"]
last_updated: 2026-06-30
---

## Definition
Performance models is Pruna's term for compressed, optimized AI models that achieve comparable quality to large foundation models at a fraction of the compute cost. They are served behind API endpoints and represent an alternative approach to model selection that prioritizes the Pareto frontier of quality vs. efficiency.

## Key Information
- **Origin**: Term used by [[Pruna]] to describe their optimized model offerings
- **Speed**: Fastest image and video models that can run between 1-5 seconds
- **Compression techniques used**: Module-specific [[Quantization]], [[Model Pruning]], and denoising step reduction (distillation or caching from 50 steps down to 4-20)
- **Efficiency comparison**: Can complete the same evaluation workload as [[ChatGPT Image]] in 7 hours vs. 20 days (~70x faster) at $265 vs. $5,000 (~19x cheaper)
- **Served behind API endpoints**: Available as hosted services
- **Open-source component**: Pruna also provides an open-source package with compression algorithms, plus materials on research papers and efficiency costs
- **Philosophy**: Performance models demonstrate that there are multiple state-of-the-art models, not one — the key is finding the right point on the [[Pareto Frontier]] for your use case

## Related
- [[summary-20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna]] — source
- [[Pruna]] — company behind the concept
- [[Model Efficiency]] — the broader principle
- [[Pareto Frontier]] — the evaluation methodology
- [[Quantization]] — compression technique
- [[Model Pruning]] — compression technique
- [[ModelDistillation]] — compression technique
- [[StepCaching]] — technique for denoising step reduction
