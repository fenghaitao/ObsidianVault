---
title: "GenCast"
type: entity
tags: [model, google, deepmind, weather, probabilistic, ai-for-science]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research.md"]
last_updated: 2026-06-26
---

## Definition
GenCast is Google DeepMind's probabilistic weather prediction model, the successor to GraphCast, that uses a mesh-based approach to produce ensemble forecasts capturing the chaotic nature of weather. It achieves higher accuracy and dramatically higher efficiency than traditional physics-based supercomputer models.

## Key Information
- **Probabilistic**: Models the fundamentally chaotic nature of weather, capturing tail events that deterministic models miss
- **Architecture**: Mesh-based (successor to GraphCast's spherical graph neural network)
- **Accuracy**: More accurate than gold-standard forecasts 97% of the time across 1,300 benchmarked weather forecasts
- **Efficiency**: Produces a 15-day forecast in 8 minutes on a single chip vs. hours on very large supercomputers
- **Operational readiness**: Designed to be operationalized and used for actual weather prediction
- **Successor**: FGN (Functional Generative Network) for cyclone-specific prediction

## Related
- [[summary-20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research]] — source
- [[GoogleDeepMind]] — creator
- [[GraphCast]] — predecessor
- [[FGN]] — cyclone-specific successor
- [[ProbabilisticWeatherPrediction]] — concept
- [[RaiaHadsell]] — research lead
