---
title: "API Consistency"
type: concept
tags: [api-design, developer-experience, google, deepmind, model-interchangeability]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind.md"]
last_updated: 2026-06-29

---

## Definition
API Consistency is the design principle that different models within a product suite should share a unified API surface, allowing developers to swap model names without changing code. At Google DeepMind, achieving API consistency across GenMedia models has been a key Developer Advocate campaign.

## Key Information
- **Problem**: When Imagen and Nano Banana were released, each model had its own set of APIs — developers couldn't simply swap the model name
- **Advocacy**: Guillaume Vernade fought internally for API consistency as a Developer Advocate
- **Outcome**: The Imagen brand was eventually deprecated/consolidated, effectively achieving consistency by reducing the number of divergent API surfaces
- **Gemini API vs Vertex AI**: Google maintains the same SDK across both platforms, allowing developers to migrate between them without rewriting code
- **Ideal state**: A developer should be able to swap a model name string and have everything work — this remains an ongoing goal
- **Tension**: Different teams within DeepMind ship models at different cadences (every 5 days), making API consistency challenging to maintain

## Related
- [[summary-20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind]] — source
- [[Developer Advocate]] — role advocating for this principle
- [[Guillaume Vernade]] — key advocate
- [[GenMedia]] — product suite affected
- [[Imagen]] — deprecated brand, example of inconsistency
