---
title: "GeminiEmbeddings2"
type: entity
tags: [model, google, deepmind, embeddings, multimodal, gemini]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research.md"]
last_updated: 2026-06-26
---

## Definition
Gemini Embeddings 2 is Google DeepMind's fully omnimodal embedding model derived from Gemini, capable of producing unified vector representations across text, video, audio, and PDF modalities for retrieval, querying, and agentic logic.

## Key Information
- **Omnimodal**: Truly unified across modalities — text (up to 8K tokens), 128 seconds of video, 80 seconds of audio, full PDFs
- **Single vector**: End-to-end unified representation without separate processing steps per modality, avoiding information loss from combining modalities
- **Derived from Gemini**: Inherits Gemini's world knowledge and understanding
- **Matryoshka Representation Learning (MRL)**: Same network supports different embedding dimensions; start retrieval at 256 dimensions, expand for more expressiveness
- **Unified semantic space**: State-of-the-art quality with cross-modal retrieval capabilities
- **Use cases**: Retrieval, querying, agentic logic, comparison functions
- **Inspiration**: Neuroscience concept of "Jennifer Aniston cells" — neurons that encode specific concepts invariantly across modalities

## Related
- [[summary-20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research]] — source
- [[GoogleDeepMind]] — creator
- [[Gemini]] — parent model family
- [[MatryoshkaRepresentationLearning]] — dimension-scalable technique
- [[OmnimodalEmbeddings]] — concept
- [[JenniferAnistonCells]] — neuroscience inspiration
- [[ContrastiveLoss]] — training approach
