---
title: "Pruna"
type: entity
tags: [company, model-efficiency, compression, optimization, open-source, image-generation, video-generation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna.md"]
last_updated: 2026-06-30
---

## Definition
Pruna is a company that builds "performance models" — compressed, optimized AI models that achieve comparable quality to large foundation models at a fraction of the compute cost. They serve models behind API endpoints and contribute open-source compression tools.

## Key Information
- **Core product**: Performance models for image and video generation served behind API endpoints, running between 1-5 seconds
- **Compression techniques**: Module-specific quantization (different quantization per module), pruning (removing unimportant components), and denoising step reduction (from 50 steps down to 4-20 via distillation or caching)
- **Efficiency gains**: Their optimized models can do the same evaluation workload as ChatGPT Image in 7 hours vs. 20 days — approximately 70x faster
- **Cost savings**: $265 vs. $5,000 for the same evaluation workload; energy equivalent of ~4 marathons vs. ~400
- **Open-source contributions**: Package with open-source compression algorithms; also provides materials on best research papers for efficiency and efficiency costs
- **Collaborations**: Worked with [[Black Forest Labs]] on optimizing Flux 2 Flex for text rendering, achieving way faster generation while staying on the Pareto frontier
- **Philosophy**: State-of-the-art is not a single model but multiple models along a Pareto frontier of quality vs. efficiency

## Related
- [[summary-20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna]] — source
- [[Bertrand Charpentier]] — speaker
- [[Performance Models]] — core concept
- [[Model Efficiency]] — central theme
- [[Pareto Frontier]] — evaluation methodology
- [[Quantization]] — compression technique used
- [[Model Pruning]] — compression technique used
- [[ModelDistillation]] — compression technique used
- [[Black Forest Labs]] — collaboration partner
