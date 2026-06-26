---
title: "ModelSteering"
type: concept
tags: [interpretability, anthropic, model-behavior, safety, research]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240805 - What's new from Anthropic and what's next： Alex Albert.md"]
last_updated: 2026-06-26
---

## Definition
Model Steering is Anthropic's interpretability-based technique for controlling language model outputs by identifying and manipulating internal features (activations corresponding to specific concepts or topics). By "clamping" a feature's value up or down, developers can steer the model's behavior beyond what prompting alone can achieve.

## Key Information
- **Research foundation**: Based on the "Scaling Monosemanticity" paper, which explains how to find features within models that activate for different topics
- **Mechanism**: Once a feature is identified, its activation value can be clamped (turned up or down) to steer model outputs
- **Golden Gate Claude**: Public demonstration — a version of Claude with the "Golden Gate Bridge" feature turned up significantly, becoming a fan favorite
- **Steering API**: In beta testing as of August 2024 — allows developers to find and clamp features for specific attributes to control Claude's outputs in addition to prompting
- **Goal**: Roll out the Steering API to more developers in the near future
- **Contrast with prompting**: Steering modifies internal model activations rather than providing external instructions, offering an orthogonal axis of control

## Related
- [[Anthropic]] — organization behind this research
- [[Alex Albert]] — presented this feature
- [[Scaling Monosemanticity]] — research paper foundation
- [[Golden Gate Claude]] — public demonstration experiment
- [[summary-20240805 - What's new from Anthropic and what's next： Alex Albert]] — source
