---
title: "Self-Supervised Learning (Vision)"
type: concept
tags: [deep-learning, computer-vision, pretraining, self-supervised-learning, vit]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow.md"]
last_updated: 2026-06-29
---

## Definition
Self-supervised learning in vision uses unlabeled images to pretrain models by creating proxy tasks (e.g., reconstructing masked patches, learning invariant representations), producing feature maps that approach supervised performance. Key techniques include MAE and DINO.

## Key Information
- **MAE (Masked Autoencoder)**: Drops random image patches and trains the model to reconstruct them. ViT-specific — cannot be applied to CNNs because convolution is invariant across patches. At scale, the model learns inductive biases from data.
- **DINOv2/DINOv3**: Produces semantically rich feature maps out of the box. PCA decomposition shows meaningful structure — e.g., tracing cat paws in different colors, decomposing satellite imagery semantically.
- Performance approaches supervised learning via linear probe: frozen features with only a linear projection head trained on task data
- The ViT exclusivity of MAE gives ViTs a decisive advantage over CNNs — they can benefit from this pretraining while CNNs cannot
- Self-supervised pretraining is the mechanism by which transformers overcome their lack of inductive bias
- Enables foundation models that work well across diverse downstream tasks without task-specific training

## Related
- [[summary-20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow]] — source
- [[MAE (Masked Autoencoder)]] — key pretraining technique
- [[DINOv3]] — self-supervised pretrained ViT
- [[ViT (Vision Transformer)]] — architecture benefiting from this paradigm
- [[Inductive Bias]] — what self-supervised learning compensates for
- [[Foundation Models]] — broader model class enabled by self-supervised pretraining
