---
title: "Model Preview vs GA"
type: concept
tags: [product-lifecycle, google, deepmind, api, europe, availability, preview, ga]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind.md"]
last_updated: 2026-06-29

---

## Definition
Model Preview vs GA (General Availability) describes the product lifecycle distinction at Google Cloud where preview models are only available on global endpoints, restricting access for customers requiring EU-hosted data processing. The rapid release cadence can reset the preview counter, delaying GA.

## Key Information
- **Preview limitation**: Preview models are only available on global endpoints, not on EU regional endpoints
- **European impact**: Companies requiring EU data hosting cannot use preview models, blocking access to the latest GenMedia capabilities
- **GA requirement**: Models must reach GA status to be available on EU endpoints
- **Release cadence problem**: Rapid back-to-back releases (e.g., Gemini 3 → Gemini 3.1) reset the preview counter, delaying GA for each iteration
- **Example**: Nano Banana 2 and Gemini 3.1 remained in preview because new versions shipped before predecessors reached GA
- **Developer Advocate priority**: Guillaume Vernade identified this as a "P0 thing" he is actively fighting to change
- **Proposed solution**: Release models to GA faster rather than changing the preview endpoint policy

## Related
- [[summary-20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind]] — source
- [[Data Sovereignty]] — underlying concern
- [[GenMedia]] — affected product suite
- [[Guillaume Vernade]] — advocate for change
- [[GoogleDeepMind]] — organization
