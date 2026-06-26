---
title: "Multimodal Embeddings"
type: concept
tags: [embeddings, multimodal, google, deepmind, search]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Multimodal Embeddings are vector representations that support video, images, audio, text, and code all in the same embedding space, enabling cross-modal search where a text query can retrieve results across all modalities.

## Key Information
- Google DeepMind's embeddings model supports video, images, audio, text, and code in the same embedding space
- Gemini Embeddings 2 is fully omnimodal — a single vector represents text (up to 8K tokens), 128 seconds of video, 80 seconds of audio, and full PDFs
- Uses Matryoshka Representation Learning (MRL) for dimension-scalable retrieval
- Enables queries like "Show me all content related to cats" returning video, images, audio (cat purring/meowing), and text (books about cats)
- Eliminates the need for separate embedding models per modality
- Available via Gemini APIs
- Represents a convergence of modalities in the embedding layer
- Inspired by neuroscience "Jennifer Aniston cells" — neurons that encode concepts invariantly across modalities

## Related
- [[summary-20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research]] — source
- [[summary-20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind]] — source
- [[Multimodal AI]] — broader concept
- [[Google DeepMind]] — creator
- [[Gemini 3.1 Pro]] — model family with multimodal capabilities
- [[GeminiEmbeddings2]] — omnimodal implementation
- [[OmnimodalEmbeddings]] — stricter form of multimodal embeddings
- [[MatryoshkaRepresentationLearning]] — dimension-scalable technique
- [[JenniferAnistonCells]] — neuroscience inspiration
