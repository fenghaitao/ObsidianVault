---
title: "AI Safety Three Layers"
type: concept
tags: [ai-safety, anthropic, evaluation]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny.md"]
last_updated: 2026-07-11
---

## Definition

[[Boris Cherny]]'s three-layer framework for how [[Anthropic]] studies AI safety, in increasing order of realism: alignment/mechanistic interpretability, evals, and real-world deployment behavior.

## Key Information

- **Layer 1 — alignment / mechanistic interpretability**: studying a model's internal neurons directly (a field invented by [[Chris Olah]]) to understand what concepts are encoded and how the model reasons — e.g., detecting when a neuron associated with deception activates. Model neurons behave surprisingly similarly to biological neurons in some respects; as models scale, "superposition" occurs, where a single neuron can encode a dozen or more concepts simultaneously.
- **Layer 2 — evals**: a "laboratory"/petri-dish setting where the model is placed in synthetic scenarios to test whether it behaves safely and as intended.
- **Layer 3 — real-world behavior**: as models get more sophisticated, they can look good on the first two layers but behave differently once deployed in the wild — the reason [[Claude Code]] was used internally for 4-5 months, and [[Claude Cowork]] was tested internally and with select customers, before either was released externally as a clearly-labeled "research preview."
- Releasing early and clearly-labeled is explicitly framed as a safety practice, not just a product-iteration one — real-world feedback is the only way to close the gap between how a model performs in the first two layers and how it actually behaves once broadly deployed.

## Related

- [[summary-25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny]] — source summary
- [[Boris Cherny]] — describes this framework
- [[Chris Olah]] — originated the interpretability layer
- [[Anthropic]] — organizational context
- [[Claude Code]] / [[Claude Cowork]] — products developed and released under this framework
- [[Race To The Top]] — related practice of open-sourcing safety tooling
