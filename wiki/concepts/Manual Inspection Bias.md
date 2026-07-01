---
title: "Manual Inspection Bias"
type: concept
tags: [evaluation, bias, human-evaluation, model-selection]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna.md"]
last_updated: 2026-06-30
---

## Definition
Manual inspection bias is the double bias introduced when evaluating AI models through informal manual inspection: (1) evaluator preference bias — different people have different aesthetic and quality preferences, and (2) sample selection bias — evaluators' judgments change based on which specific samples they see. This makes manual inspection alone an unreliable method for selecting the best model.

## Key Information
- **Demonstrated live**: Bertrand Charpentier showed three sets of images to the audience and asked for preferences. Different people preferred different images, and some people changed their minds between rounds
- **Evaluator preference bias**: What one person considers the "best" image depends on their personal aesthetic preferences — there is no universal agreement
- **Sample selection bias**: People are biased toward the few specific samples they look at; changing which samples are shown changes which model appears best
- **Two times biased**: Manual inspection combines both biases, making it doubly unreliable
- **Not useless, but insufficient**: Manual inspection is good for getting a feeling but not enough for decision-making. It should be supplemented with scaled human evaluation (many evaluators) and automated metrics
- **Solution**: Ask many people, use many samples, and combine with automated metrics that target your specific use case

## Related
- [[summary-20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna]] — source
- [[StateOfTheArt Ambiguity]] — manual inspection bias contributes to SOTA ambiguity
- [[Public Leaderboards]] — alternative to manual inspection (though with their own problems)
- [[CLIP Score]] — automated metric that can complement manual inspection
- [[Model Efficiency]] — another dimension to consider beyond manual quality assessment
