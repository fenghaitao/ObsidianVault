---
title: "GraphCast"
type: entity
tags: [model, google, deepmind, weather, graph-neural-network, ai-for-science]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research.md"]
last_updated: 2026-06-26
---

## Definition
GraphCast is Google DeepMind's spherical graph neural network for weather prediction that autoregressively predicts 100 atmospheric variables up to 15 days out, trained on 40 years of global weather data. It demonstrated superior accuracy to physics-based models for major events like Hurricane Lee.

## Key Information
- **Architecture**: Spherical graph neural network encompassing the Earth with nodes from surface to lower stratosphere
- **Variables**: Predicts 100 atmospheric variables autoregressively (wind speed, temperature, humidity, etc.)
- **Training data**: 40 years of global weather data
- **Forecast horizon**: Up to 15 days
- **Hurricane Lee (2024)**: Predicted landfall location accurately 9 days out vs. 6 days for gold-standard physics-based models — a 3-day advantage critical for major hurricane landfall preparation
- **Origin**: Prompted by UK Met Office asking if AI could predict rainfall better than physics-based models
- **Successor**: GenCast (probabilistic, higher accuracy, higher efficiency)

## Related
- [[summary-20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research]] — source
- [[GoogleDeepMind]] — creator
- [[GenCast]] — probabilistic successor
- [[FGN]] — cyclone-specific successor
- [[GraphNeuralNetwork]] — architecture concept
- [[RaiaHadsell]] — research lead
