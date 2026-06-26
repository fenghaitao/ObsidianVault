---
title: "ModelParallelism"
type: concept
tags: [training, scaling, infrastructure, distributed-computing, deep-learning]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Model parallelism is a distributed training technique where a neural network model is split (sharded) across multiple accelerator chips, as opposed to data parallelism where the batch is split. It becomes necessary when models grow too large to fit on a single chip, and JAX provides automatic tooling to minimize inter-chip communication.

## Key Information
- **When needed**: Beyond a certain scale, data parallelism (splitting batches) is insufficient; the model itself must be distributed
- **JAX automation**: JAX provides tooling that automatically shards models and minimizes communication between chips
- **Declarative approach**: Researchers specify the desired sharding strategy; JAX handles the implementation
- **TPU optimization**: JAX was designed with TPU fast interconnects in mind, making model parallelism efficient
- **Communication minimization**: Critical for performance — JAX automatically optimizes data transfer between chips
- **Scaling necessity**: Essential for training large diffusion models like Veo and NanoBanana
- **Beyond single chip**: TPUs are rarely used individually; they're designed for scale-out

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[JAX]] — framework providing automatic model parallelism
- [[TPU]] — hardware optimized for model parallelism
- [[DiffusionModels]] — models trained with this technique
- [[Veo]] — model requiring model parallelism
- [[NanoBanana]] — model requiring model parallelism
