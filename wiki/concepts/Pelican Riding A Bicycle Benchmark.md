---
title: "Pelican Riding A Bicycle Benchmark"
type: concept
tags: [ai, benchmarking, humor]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming.md"]
last_updated: 2026-07-11
---

## Definition

Informal AI model benchmark created by [[Simon Willison]] (originally as a joke rebuttal to opaque numeric benchmarks): ask a model to generate an SVG image of a pelican riding a bicycle, then visually compare results across models.

## Key Information

- It's actually a test of text/code-generation quality, not image models — since it asks for SVG (vector drawing) code, which any text model can output and which can then be rendered and visually judged, unlike opaque numeric scores ("74% on Terminal Bench") that don't intuitively convey what a model is actually good at.
- Willison discovered an unexplained but consistent correlation: models that draw better pelicans-on-bicycles also tend to perform better on everything else, including on totally unrelated capability. Neither he nor anyone else has explained why.
- Has become a widely recognized meme within the AI industry — labs are aware of it and reportedly take some pride in their models' pelican output (e.g., Gemini's release materials have featured animated pelican-on-bicycle content).
- Willison deliberately keeps secret backup/alternate prompts (e.g., "an ocelot on a moped") specifically so he can detect if a lab ever trains a model specifically to game the pelican benchmark — if pelicans improve suspiciously while the secret alternates don't, that would reveal benchmark-gaming.

## Related

- [[summary-17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming]] — source summary
- [[Simon Willison]] — creates and maintains this benchmark
