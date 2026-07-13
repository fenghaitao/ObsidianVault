---
title: "Build For The Model 6 Months Out"
type: concept
tags: [ai, product-strategy, timing]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/26 - OpenAI’s head of platform engineering on the next 12-24 months of AI ｜ Sherwin Wu.md"]
last_updated: 2026-07-11
---

## Definition

[[Boris Cherny]]'s product-timing philosophy: design and build for the AI model's capability roughly 6 months in the future, not its current capability — accepting weak product-market fit at first so the product is ready to "click" the moment the more capable model arrives.

## Key Information

- Direct account of [[Claude Code]]'s own bet: in its early months, the underlying model (Sonnet 3.5-era) genuinely wasn't good enough to justify heavy trust, and Cherny personally wrote very little of his own code through it. The product only "inflected" when Opus 4/Sonnet 4 (Anthropic's first ASL-3-class release) arrived, at which point growth went exponential and stayed there.
- Generalizable predictions Cherny cites for betting ahead of the curve: models will keep getting better at using tools/computers, and will keep being able to run autonomously for longer stretches unattended (Claude went from ~15-30 seconds of reliable autonomous work a year prior to 10-30+ minutes with Opus 4.6, with some tasks running for hours, days, or even weeks).
- Explicit advice to startups: it will be uncomfortable to have weak product-market fit for the first ~6 months, but building for where the model is headed (not where it is) means the product is ready to capture the next capability jump immediately rather than playing catch-up.
- Complements [[Bitter Lesson]] and [[Don't Box The Model In]]: minimal, general-purpose scaffolding ages better precisely because it doesn't need to be rebuilt once the anticipated future model arrives.
- Independently echoed almost verbatim by [[Sherwin Wu]] (OpenAI, episode 26) as his standing advice to founders: "make sure you're building for where the models are going and not where they are today." Wu cites a companion line from FinTool founder Nicholas — "the models will eat your scaffolding for breakfast" — pointing to how 2022-2023-era scaffolding (vector stores, rigid agent frameworks) was largely rendered unnecessary as models improved, much as skills-file/AGENTS.md-based context management may itself be superseded later. Wu frames this as a reason not to blindly follow customer feedback, since customers requesting improvements to today's scaffolding are often optimizing a local maximum the next model generation will simply erase.

## Related

- [[summary-25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny]] — source summary
- [[summary-26 - OpenAI’s head of platform engineering on the next 12-24 months of AI ｜ Sherwin Wu]] — source summary
- [[Boris Cherny]] — originates and applies this philosophy
- [[Claude Code]] — product built on this bet
- [[Bitter Lesson]] / [[Don't Box The Model In]] — related design philosophy
- [[Sherwin Wu]] — independently echoes this principle at OpenAI
