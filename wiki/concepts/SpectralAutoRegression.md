---
title: "SpectralAutoRegression"
type: concept
tags: [diffusion, fourier-analysis, image-generation, frequency-domain]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Spectral auto-regression is a term coined by Sander Dieleman to describe how diffusion models generate images: by progressively adding higher-frequency detail on top of lower-frequency structure, analogous to auto-regression but operating in the frequency domain rather than sequentially in pixel space.

## Key Information
- **Coined by**: Sander Dieleman, Google DeepMind
- **Core observation**: Natural images have power-law spectra (straight line on log-log plot) — more energy in low frequencies, less in high frequencies
- **Noise effect**: Gaussian noise has a flat spectrum (equal energy at all frequencies). Adding noise to an image obscures high frequencies first, then progressively lower frequencies
- **Generation process**: Diffusion denoising naturally recovers low frequencies (coarse structure, semantics) first, then progressively adds higher frequencies (fine details, textures)
- **Coarse-to-fine**: This matches the intuitive approach of sketching out semantics before adding details
- **Training implications**: Models can be trained to weight different frequency scales differently based on perceptual importance
- **Why it works for images**: Images have natural hierarchical structure that aligns with frequency decomposition
- **Contrast with pixel auto-regression**: Pixel-space auto-regression requires choosing an arbitrary sequence order; spectral auto-regression uses a more natural decomposition

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[DiffusionModels]] — the technique it describes
- [[FourierAnalysisOfImages]] — analytical foundation
- [[SanderDieleman]] — coined the term
- [[ImageNet]] — dataset used for demonstration
