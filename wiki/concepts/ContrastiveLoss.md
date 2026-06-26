---
title: "ContrastiveLoss"
type: concept
tags: [machine-learning, embeddings, loss-function, deep-learning]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research.md"]
last_updated: 2026-06-26
---

## Definition
Contrastive Loss is a loss function used to train embedding models by learning to pull similar items closer together and push dissimilar items apart in the embedding space. It was pioneered in part through Siamese neural networks and is critical for building robust retrieval and comparison systems.

## Key Information
- **Purpose**: Train models to produce embeddings where similar concepts are close and dissimilar ones are far apart
- **Siamese networks**: Early architecture using contrastive loss, part of Raia Hadsell's PhD work with Yann LeCun at NYU
- **Application**: Used in Gemini Embeddings 2 to create unified omnimodal embedding spaces
- **Benefit**: Enables fast retrieval, recognition, and comparison across modalities
- **Inspiration**: Mirrors how the brain uses "Jennifer Aniston cells" — neurons that activate for the same concept regardless of modality (image, voice, text)

## Related
- [[summary-20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research]] — source
- [[GeminiEmbeddings2]] — model using contrastive loss
- [[OmnimodalEmbeddings]] — related concept
- [[JenniferAnistonCells]] — neuroscience inspiration
- [[RaiaHadsell]] — researcher who worked on Siamese networks
