---
title: "VariableAspectRatios"
type: concept
tags: [multimodal, vision, image-processing, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Variable Aspect Ratios is a vision processing capability in Gemma 4 that supports images of different aspect ratios by passing spatial positional encoding to the model, eliminating the need for the pan-and-scan approach used in Gemma 3.

## Key Information
- Images of different aspect ratios (e.g., 4x2 vs. 3x3) have patches in different spatial positions
- Spatial positional encoding is passed through to the model so it understands patch positions
- Replaces Gemma 3's pan-and-scan approach (splitting images into square sequences)
- Works in conjunction with variable resolution to give developers control over image processing
- Enables more efficient and accurate processing of non-square images

## Related
- [[Gemma4]] — implements this capability
- [[VariableResolution]] — complementary capability
- [[MultimodalModels]] — broader context
- [[summary-20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind]] — source
