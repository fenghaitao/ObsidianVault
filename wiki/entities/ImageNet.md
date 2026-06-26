---
title: "ImageNet"
type: entity
tags: [dataset, computer-vision, benchmark, image-classification]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
ImageNet is a large-scale image dataset used by Sander Dieleman to demonstrate Fourier analysis of natural images, showing the power-law relationship in image spectra that underlies why diffusion models work well for image generation.

## Key Information
- Large-scale image dataset commonly used in computer vision research
- Used in the talk to demonstrate Fourier spectral analysis of natural images
- Images from ImageNet show a characteristic power-law spectrum (straight line on log-log plot)
- This power-law relationship means images have more energy in low frequencies and less in high frequencies
- The spectral properties explain why diffusion's coarse-to-fine generation (low frequencies first) is natural for images

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[FourierAnalysisOfImages]] — analysis technique demonstrated
- [[SpectralAutoRegression]] — concept derived from this analysis
- [[DiffusionModels]] — modeling paradigm informed by spectral properties
