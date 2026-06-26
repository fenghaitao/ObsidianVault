---
title: "MatryoshkaRepresentationLearning"
type: concept
tags: [machine-learning, embeddings, dimensionality, efficiency]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research.md"]
last_updated: 2026-06-26
---

## Definition
Matryoshka Representation Learning (MRL) is a technique that allows a single embedding model to produce representations at multiple dimensions, enabling coarse-to-fine retrieval where you can start with low-dimensional embeddings (e.g., 256 dims) for fast search and expand to higher dimensions for more expressiveness — all from the same network.

## Key Information
- **Name origin**: Named after Matryoshka (Russian nesting) dolls — representations nest within each other at different dimensionalities
- **Efficiency**: Start retrieval at 256 dimensions for speed, expand to full dimensionality for precision
- **Single network**: No need for separate models at different dimensions — one network produces all
- **Used in**: Gemini Embeddings 2 for dimension-scalable retrieval
- **Benefit**: Enables trade-off between speed and accuracy without model switching
- **Unified semantic space**: Lower dimensions capture the same semantic structure as higher dimensions

## Related
- [[summary-20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research]] — source
- [[GeminiEmbeddings2]] — model using MRL
- [[OmnimodalEmbeddings]] — related concept
- [[ContrastiveLoss]] — complementary training technique
