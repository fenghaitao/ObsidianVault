---
title: "Vision Model Training Conflicts"
type: concept
tags: [vision, training, llm, prompt-engineering, spatial-reasoning]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260501 - Agents on the Canvas in tldraw — Steve Ruiz, tldraw.md"]
last_updated: 2026-06-29
---

## Definition
Vision Model Training Conflicts are contradictions in vision model training data that make spatial reasoning and structured output generation challenging. Unlike text models, vision models have less training data and that data contains inherent conflicts in coordinate systems, directional references, and spatial conventions.

## Key Information
- **Less training data**: Vision models have significantly less training data than text models
- **Conflicting conventions**: Training data contains contradictory spatial conventions that don't exist in text:
  - **Y-axis conflict**: On Cartesian graphs, Y increases upward (0, 1, 2, 3...). On the web, Y increases downward (top-left origin is 0,0). The model must reconcile these opposing conventions.
  - **Left/right ambiguity**: "Left" can mean stage left, viewer left, object left, or screen left — all different spatial positions
- **Prompt engineering challenge**: Getting models to behave predictably with structured spatial outputs required extensive prompt engineering
- **Impact on structured outputs**: When generating structured data (shapes, positions, diagrams), these conflicts cause unpredictable behavior
- **Example**: Drawing a diagram on a canvas requires the model to understand which coordinate system the canvas uses and consistently apply it
- This is one reason why image generation (diffusion models) is easier for vision tasks than structured output generation — images don't need to resolve coordinate ambiguities

## Related
- [[summary-20260501 - Agents on the Canvas in tldraw — Steve Ruiz, tldraw]] — source
- [[Structured Outputs]] — the output format affected by these conflicts
- [[Prompt Engineering]] — the mitigation approach
- [[Foundation Models]] — the model category
- [[MultimodalAI]] — broader category of vision-capable models
