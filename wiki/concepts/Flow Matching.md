---
title: "Flow Matching"
type: concept
tags: [generative-models, training-technique, diffusion, image-generation, video-generation, audio-generation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - FLUX, Open Research, and the Future of Visual AI — Stephen Batifol, Black Forest Labs.md"]
last_updated: 2026-06-29
---

## Definition
Flow Matching is the standard training approach for generative models, used as the baseline in Black Forest Labs' Self Flow research. It involves adding random noise to data and training a model to denoise it. Self Flow improves upon this by combining representation learning and generation in the same flow.

## Key Information
- Standard approach for training generative models (images, video, audio)
- Process: add random noise to training data, train model to denoise
- Used as the baseline comparison in BFL's Self Flow paper
- Self Flow outperforms Flow Matching across all modalities tested (audio, images, video)
- Flow Matching baselines plateau in loss reduction while Self Flow continues improving
- Flow Matching models exhibit worse text rendering, anatomy, and video flickering compared to Self Flow

## Related
- [[summary-20260508 - FLUX, Open Research, and the Future of Visual AI — Stephen Batifol, Black Forest Labs]] — source
- [[Self Flow]] — approach that improves upon Flow Matching
- [[DiffusionModels]] — related generative paradigm
- [[RectifiedFlow]] — related concept for straighter sampling paths
- [[Black Forest Labs]] — research lab comparing against Flow Matching
