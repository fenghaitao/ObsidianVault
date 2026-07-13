---
title: "Don't Box The Model In"
type: concept
tags: [ai, agents, product-design]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny.md"]
last_updated: 2026-07-11
---

## Definition

[[Boris Cherny]]'s core [[Claude Code]] design philosophy: instead of constraining a model to a narrow component of a larger orchestrated system (fixed step-by-step workflows, curated context, an "orchestrator" directing it), give the model tools, a goal, and minimal scaffolding, and let it decide which tools to use and in what order.

## Key Information

- Cherny's framing: "ask not what the model can do for you" — give it the tools to get the context and take the actions it needs, rather than pre-curating everything for it.
- Cited as a direct application of the [[Bitter Lesson]]: rigid workflows/scaffolding might buy 10-20% better performance short-term, but those gains typically get erased by the next, more capable general model, so minimal scaffolding ages better.
- Concretely, Claude Code was built by exposing the model directly with a minimal tool set rather than boxing it into a single fixed application component — described as "the product is the model."
- Connects to the model-side framing of [[Latent Demand]] ("being on distribution"): watch what the model naturally wants to do and make that easier, rather than forcing it into a predetermined shape.

## Related

- [[summary-25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny]] — source summary
- [[Boris Cherny]] — originates this philosophy
- [[Bitter Lesson]] — underlying principle
- [[Claude Code]] — product built on this philosophy
- [[Latent Demand]] — related model-side framing ("on distribution")
