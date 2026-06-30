---
title: "Multi-Modal Generation"
type: concept
tags: [multimodal, image-generation, video-generation, audio-generation, joint-generation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - FLUX, Open Research, and the Future of Visual AI — Stephen Batifol, Black Forest Labs.md"]
last_updated: 2026-06-29
---

## Definition
Multi-Modal Generation is the capability of a single model to generate content across multiple modalities — images, video, and audio — trained jointly rather than separately. Black Forest Labs' Self Flow approach enables this by combining representation learning and generation in a unified flow across modalities.

## Key Information
- Self Flow enables training a single model on images, video, and audio jointly
- Eliminates the need for separate modality-specific encoders
- Joint training enables joint generation: e.g., video with synchronized audio from a single model
- Self Flow outperforms Flow Matching baselines across all modalities (audio, images, video)
- Model can also be extended to action prediction for robotics
- Contrasts with the "Frankenstein" approach of stitching together modality-specific encoders
- Natural scaling: as the model scales, all modalities benefit together

## Related
- [[summary-20260508 - FLUX, Open Research, and the Future of Visual AI — Stephen Batifol, Black Forest Labs]] — source
- [[Self Flow]] — training approach enabling multi-modal generation
- [[Self-Supervised Representation Learning]] — core learning paradigm
- [[Representation Alignment]] — previous approach with modality-specific encoders
- [[Visual Intelligence]] — BFL's vision enabled by this capability
- [[Physical AI]] — extension to action/robotics modality
- [[Black Forest Labs]] — research lab
