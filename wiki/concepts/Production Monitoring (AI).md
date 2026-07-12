---
title: "Production Monitoring (AI)"
type: concept
tags: [AI, monitoring, production, observability, evaluation]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md"]
last_updated: 2026-07-10
---

## Definition

Production monitoring for AI products is the practice of tracking key metrics and signals from live user interactions to understand how the AI system is performing in the real world. Unlike traditional software monitoring, AI monitoring requires more granularity — tracking both explicit feedback (thumbs up/down) and implicit signals (regeneration, abandonment, behavior changes).

## Key Information

- **Complement to evals**: Evals catch known errors; production monitoring catches emerging patterns you never anticipated.
- **Explicit signals**: Thumbs up/down, user ratings, direct feedback.
- **Implicit signals**: When a user regenerates an answer instead of giving a thumbs down — clear indication the initial answer didn't meet expectations. When a user switches off a feature entirely.
- **The feedback loop**: Production monitoring surfaces failure patterns → examine those traces → identify patterns that matter → build eval datasets for them → deploy → still need production monitoring for new unknowns.
- **For high-throughput applications**: You can't practically review all traces. Production monitoring gives you indicators of which traces to look at.
- **Codex example**: When deploying a new model for code review, they AB test to see if it finds the right mistakes and how users react. If users get annoyed by incorrect code reviews, they "go to the extent of just switching off the product" — that's a critical signal.
- **Social media monitoring**: Codex also monitors social media for user problems and quickly fixes them.
- This has existed for traditional products, but AI agents require monitoring with much more granularity.

## Related

- [[Evals (Evaluation Metrics)]] — complementary to production monitoring
- [[Implicit User Signals]] — the data source for production monitoring
- [[Continuous Calibration Continuous Development (CCCD)]] — framework where production monitoring plays a key role
- [[Behavior Calibration]] — the calibration informed by production monitoring
- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — source summary
