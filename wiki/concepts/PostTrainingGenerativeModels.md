---
title: "PostTrainingGenerativeModels"
type: concept
tags: [generative-models, fine-tuning, conditioning, preference-tuning, diffusion]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Post-training for generative models refers to the phase after pre-training where additional conditioning signals (beyond text prompts) and preference tuning are added. This includes reference-based generation, camera motion control, event timing, and human preference optimization via RLHF or DPO.

## Key Information
- **Beyond text prompts**: Users want reference-based generation (e.g., put yourself in a video using a photo), camera motion control, and specific event timing
- **Why post-training**: Pre-training datasets typically lack these advanced conditioning signals, so they must be added afterward
- **Conditioning insertion methods**: Transformers offer multiple ways to add conditioning — extra tokens, broadcasting to all tokens, or other mechanisms
- **Representation matters**: Conditioning signals should be semantically abstract; finding the right representation is key
- **Preference tuning**: Human evaluation-based optimization (RLHF, DPO) applied to generative models, similar to LLM post-training
- **Effect on model "style"**: Post-training makes models more "opinionated" — it selects which sliver of the pre-training distribution to focus on
- **Sander Dieleman's view**: Post-training probably plays a bigger role in model "style" than guidance scale

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[DiffusionModels]] — model type
- [[FineTuning]] — related technique
- [[Veo]] — video model using post-training
- [[NanoBanana]] — image model using post-training
