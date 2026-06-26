---
title: "GraphNeuralNetwork"
type: concept
tags: [machine-learning, graph, neural-network, weather, ai-for-science]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research.md"]
last_updated: 2026-06-26
---

## Definition
Graph Neural Networks (GNNs) are neural network architectures that operate on graph-structured data, where nodes represent entities and edges represent relationships. In weather prediction, spherical GNNs encompass the Earth with nodes from the surface to the lower stratosphere to model atmospheric dynamics.

## Key Information
- **Spherical GNN**: GraphCast uses a spherical graph neural network encompassing the Earth with nodes from surface to lower stratosphere
- **Variables**: GraphCast predicts 100 atmospheric variables autoregressively (wind speed, temperature, humidity, etc.)
- **Training**: 40 years of global weather data
- **Forecast horizon**: Up to 15 days
- **Advantage over physics models**: 3 extra days of accurate hurricane landfall prediction (9 days vs. 6 days for Hurricane Lee)
- **Successor**: GenCast uses a mesh-based approach (also graph-structured) with probabilistic outputs

## Related
- [[summary-20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research]] — source
- [[GraphCast]] — spherical GNN implementation
- [[GenCast]] — mesh-based probabilistic successor
- [[ProbabilisticWeatherPrediction]] — related concept
- [[GoogleDeepMind]] — creator
