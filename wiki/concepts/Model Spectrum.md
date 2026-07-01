---
title: "Model Spectrum"
type: concept
tags: [llm, model-customization, ai-engineering, strategy]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - What Lies Beneath the API — Benjamin Cowen, Modal.md"]
last_updated: 2026-06-30
---

## Definition
The Model Spectrum is a continuum describing the trade-off between convenience and customization in AI model deployment, ranging from Frontier APIs (maximum convenience, no customization) through fine-tuning (algorithm control without infra burden) to full model training (maximum control, maximum responsibility).

## Key Information
- **Frontier API end**: Fast iteration, no customization, great for prototyping, poor economics at scale
- **Middle ground (fine-tuning)**: Algorithm-level control without managing clusters, retains fast iteration cycles, accessible in ~300 lines of Python
- **Full training end**: Complete control over model behavior and architecture, but requires managing clusters, infrastructure, and the entire stack
- Companies naturally move rightward on the spectrum as their products mature and specialize
- The middle ground has been enabled by serverless compute platforms and open-source training libraries
- Key question: when does your application step over the line into a custom domain?

## Related
- [[summary-20260602 - What Lies Beneath the API — Benjamin Cowen, Modal]] — source
- [[Frontier API]] — left end of the spectrum
- [[FineTuning]] — the middle ground
- [[DomainSpecific Models]] — the outcome of moving right on the spectrum
- [[Serverless Training]] — enabler of the middle ground
- [[Model Customization]] — broader framework
