---
title: "Self Flow"
type: entity
tags: [research-paper, self-supervised-learning, multimodal, representation-learning, image-generation, video-generation, audio-generation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - FLUX, Open Research, and the Future of Visual AI — Stephen Batifol, Black Forest Labs.md"]
last_updated: 2026-06-29
---

## Definition
Self Flow is a research paper and approach from Black Forest Labs that enables scalable training of multimodal generative models using self-supervised learning, eliminating the need for external encoder models by combining representation learning and generation in the same flow.

## Key Information
- Published as open research by Black Forest Labs ~March 2025
- Eliminates external encoder models (e.g., DinoV2) from the training pipeline
- Combines representation learning and generation in a single flow
- **Mechanism**: Two types of random noise added to assets (high noise, low noise); student model denoises high-noise images; teacher model (EMA of student) processes low-noise images; student minimizes both generation loss and representation loss
- **Results across modalities**: Better than flow matching baselines for audio, images, and video
- Converges faster than baselines; baseline plateaus while Self Flow continues improving
- Significantly improves text rendering (correct spelling, proper letter placement)
- Better anatomy in generated images
- Eliminates flickering in video generation
- Can generate video and audio jointly from the same model
- Can also predict robot actions when trained on action data
- Scales naturally: both student and teacher scale with model size, unlike frozen external encoders

## Related
- [[summary-20260508 - FLUX, Open Research, and the Future of Visual AI — Stephen Batifol, Black Forest Labs]] — source
- [[Black Forest Labs]] — creator
- [[Flux]] — model family using this approach
- [[SelfSupervised Representation Learning]] — core concept
- [[Representation Alignment]] — the problem Self Flow solves
- [[Flow Matching]] — baseline approach it improves upon
- [[DinoV2]] — external encoder it replaces
- [[MultiModal Generation]] — enabled capability
- [[Physical AI]] — robotics application
- [[Student-Teacher Architecture]] — training architecture
