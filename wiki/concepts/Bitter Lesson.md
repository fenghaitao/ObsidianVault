---
title: "Bitter Lesson"
type: concept
tags: [ai, machine-learning, engineering-philosophy]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny.md"]
last_updated: 2026-07-11
---

## Definition

Principle from [[Rich Sutton]]'s essay "The Bitter Lesson" (~2019): more general AI models/methods reliably outperform more specific, hand-engineered ones over the long run — cited by [[Boris Cherny]] as required reading for the [[Claude Code]] team and a core design philosophy.

## Key Information

- Sutton's original context was domains like self-driving cars, but Cherny says the corollary generalizes broadly: always bet on the more general model rather than investing in narrow fine-tuning or small specialized models, when you have the flexibility to do so.
- Practical implication for agent harnesses: workflows/scaffolding that hand-hold a model through fixed steps might improve performance ~10-20% in the short term, but those gains are typically "wiped out" by the next, more capable general model — so it's often better to wait for capability gains than invest heavily in scaffolding.
- Directly underlies [[Don't Box The Model In]] and [[Build For The Model 6 Months Out]] as applied product philosophy at Anthropic.

## Related

- [[summary-25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny]] — source summary
- [[Rich Sutton]] — originated this principle
- [[Boris Cherny]] — applies it as Claude Code team doctrine
- [[Don't Box The Model In]] — applied design consequence
- [[Build For The Model 6 Months Out]] — related product-timing philosophy
