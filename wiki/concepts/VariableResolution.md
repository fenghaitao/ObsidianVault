---
title: "VariableResolution"
type: concept
tags: [multimodal, vision, image-processing, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Variable Resolution is a Gemma 4 capability allowing developers to select the resolution and soft token budget allocated to images, enabling trade-offs between image quality and token consumption based on task requirements.

## Key Information
- Available across five different resolutions/soft token budgets in all Gemma 4 models
- Higher resolutions (560, 1120) recommended for OCR and spatial object recognition
- Lower resolutions suitable for text-heavy applications not using multimodal capabilities
- Images are split into 16x16 pixel patches, then 3x3 grids of patches become single embeddings
- A token budget of 280 equates to 2,520 different patches
- Works with variable aspect ratios to provide flexible image processing
- Major improvement over Gemma 3's fixed pan-and-scan approach

## Related
- [[Gemma4]] — implements this capability
- [[VariableAspectRatios]] — complementary capability
- [[MultimodalModels]] — broader context
- [[summary-20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind]] — source
