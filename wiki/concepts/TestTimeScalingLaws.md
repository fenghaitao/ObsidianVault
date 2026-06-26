---
title: "TestTimeScalingLaws"
type: concept
tags: [scaling, pre-training, tokens, compute]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI.md"]
last_updated: 2026-06-26
---

## Definition
Test-time scaling laws, proposed by Roberts et al (2026), are new scaling laws showing that small models continue to improve with more pre-training tokens far beyond what Chinchilla scaling laws predict as compute-optimal, suggesting small models benefit from training on significantly more data than previously believed.

## Key Information
- Published by Roberts et al the week before Maxime Labonne's April 2026 presentation
- Show that Chinchilla scaling laws underestimate optimal token counts for small models
- LFM 2.5 350M was pre-trained on 28 trillion tokens — far beyond Chinchilla-optimal (~1B tokens)
- According to the new laws, even 28T tokens may not be enough for optimal performance
- Performance continues to grow when scaling pre-training tokens for small models
- Small models are cheaper to pre-train on massive token counts than large models

## Related
- [[summary-20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI]] — source
- [[ChinchillaScalingLaws]] — previous scaling paradigm being superseded
- [[LFM]] — model trained using these insights
- [[ModelScaling]] — broader scaling context
- [[EdgeModels]] — model category benefiting from these laws
