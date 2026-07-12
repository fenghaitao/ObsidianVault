---
title: "Feature Flags (Dangerous Shims)"
type: concept
tags: [engineering, product, process, quality]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/36 - \u201CI deliberately understaff every project\u201D \uFF5C Leadership lessons from Rippling\u2019s \ journey.md"]
last_updated: 2026-07-10
---

## Definition

Feature flags are temporary code toggles that engineers use to enable/disable features. Matt McGinness describes them as "the bane of my existence" and compares them to construction shims — temporary fixes that get forgotten and cause failures later.

## Key Information

- McGinness: "I'm not allowed to say feature flag without 'fucking' in front of it"
- Compared to shims in construction: a general contractor puts shims in places, forgets about them, builds walls over them, and eventually the shims fail and the door doesn't fit
- Engineers put feature flags in temporarily and forget to remove them
- Example: a feature flag caused a blank screen when Parker Conrad installed a new Rippling application
- Rippling's standard post-incident: "You are allowed to have one feature flag that governs your entire product at ship" — an extreme standard added to the pickle
- Feature flags need to be managed carefully as part of the product quality process

## Related

- [[summary-36 - “I deliberately understaff every project” ｜ Leadership lessons from Rippling’s $16B journey]] — source summary
- [[Product Quality List (Pickle)]] — process that manages feature flags