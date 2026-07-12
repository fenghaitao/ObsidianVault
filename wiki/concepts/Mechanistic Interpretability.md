---
title: "Mechanistic Interpretability"
type: concept
tags: [AI, safety, research, Anthropic]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny.md"]
last_updated: 2026-07-10
---

## Definition

Mechanistic interpretability is the field of studying what individual neurons and layers in AI models represent — understanding the "brain" of the model at a mechanistic level. Pioneered by Chris Olah at Anthropic.

## Key Information

- Pioneered by Chris Olah at Anthropic
- Idea: model neurons are not the same as animal neurons but behave similarly in many ways
- Researchers can study which neurons map to which concepts, how particular concepts are encoded, how the model does planning, and how it thinks ahead
- Early question: was the model just predicting the next token, or doing something deeper? Now there's "quite strong evidence" it's doing something deeper
- **Superposition:** As models get bigger, a single neuron might correspond to dozens of concepts; when activated together with other neurons, they represent more sophisticated concepts
- This is the lowest of Anthropic's three safety layers: mechanistic interpretability (lowest) → evals (laboratory) → real-world behavior (highest)
- Anthropic publishes this research openly to inspire other labs to work on safety
- Can monitor specific neurons (e.g., deception-related) to understand when they're activating

## Related

- [[Chris Olah]] — pioneer of the field
- [[Anthropic]] — where this research is done
- [[AI Safety Layers]] — the three-layer framework
- [[Superposition (Neural Networks)]] — related concept
- [[summary-25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny]] — source summary
