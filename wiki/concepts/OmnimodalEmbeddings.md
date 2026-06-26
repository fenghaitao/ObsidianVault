---
title: "OmnimodalEmbeddings"
type: concept
tags: [embeddings, multimodal, retrieval, google, deepmind]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research.md"]
last_updated: 2026-06-26
---

## Definition
Omnimodal Embeddings are unified vector representations that encode text, video, audio, and documents (PDFs) into a single embedding space without separate processing steps per modality, enabling truly end-to-end cross-modal retrieval without information loss from modality combination.

## Key Information
- **Truly unified**: Unlike multimodal embeddings that may process modalities separately and combine, omnimodal embeddings are end-to-end unified
- **No information loss**: Avoids losing information by trying to combine audio, visual, and text information together as separate steps
- **Single vector**: One vector represents text (up to 8K tokens), 128 seconds of video, 80 seconds of audio, and full PDFs
- **Implementation**: Gemini Embeddings 2 from Google DeepMind
- **Use cases**: Retrieval, querying, agentic logic, comparison functions
- **Contrast with multimodal embeddings**: Omnimodal is a stricter form — truly unified rather than multi-pipeline

## Related
- [[summary-20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research]] — source
- [[GeminiEmbeddings2]] — implementation
- [[Multimodal Embeddings]] — broader concept
- [[MatryoshkaRepresentationLearning]] — dimension-scalable technique used
- [[ContrastiveLoss]] — training approach
- [[JenniferAnistonCells]] — neuroscience inspiration
