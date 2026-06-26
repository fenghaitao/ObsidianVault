---
title: "GLIDE"
type: entity
tags: [model, openai, diffusion, image-generation, pixel-space]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
GLIDE is an early pixel-space diffusion model at scale from OpenAI (2021), cited by Sander Dieleman as one of the last papers to show the dramatic difference between sampling with and without classifier-free guidance. After GLIDE, guidance became universally adopted.

## Key Information
- OpenAI paper from 2021, one of the first pixel-space diffusion models trained at scale
- Demonstrated the dramatic quality improvement from classifier-free guidance
- Showed that guidance reduces diversity but massively improves individual sample quality
- After this paper, guidance became standard and is never turned off in modern diffusion models
- Sander Dieleman notes that most people would be surprised how bad today's models are without guidance

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[OpenAI]] — creator
- [[DiffusionModels]] — underlying technique
- [[ClassifierFreeGuidance]] — key technique demonstrated
- [[GuidanceScale]] — hyperparameter studied in the paper
