---
title: "AI Safety Layers"
type: concept
tags: [AI, safety, Anthropic, framework]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny.md"]
last_updated: 2026-07-10
---

## Definition

Anthropic's three-layer framework for studying AI safety, ranging from the lowest mechanistic level to the highest real-world observation level. Each layer provides different insights, and the model might look good on lower layers but not on higher ones.

## Key Information

**Layer 1: Alignment & Mechanistic Interpretability (Lowest)**
- The lowest level: studying what's happening in the model's neurons as it's trained
- Fairly sophisticated technology to trace neuron activations
- Can monitor specific neurons (e.g., deception-related) to understand when they activate
- This is done during training to ensure the model is safe

**Layer 2: Evals (Laboratory)**
- The model is in a "petri dish" — studied in a laboratory setting
- Synthetic situations are created to test the model's behavior
- Questions: "Is it doing the right thing? Is it aligned? Is it safe?"

**Layer 3: Real-World Behavior (Highest)**
- Seeing how the model behaves "in the wild" with actual users
- As models get more sophisticated, this becomes increasingly important
- The model may look good on layers 1 and 2 but not on layer 3
- This is why Anthropic releases products early (as research previews) — to study real-world safety
- Claude Code was used internally for 4-5 months before external release because it was the first major agent

## Related

- [[Anthropic]] — creator of this framework
- [[Mechanistic Interpretability]] — Layer 1
- [[Evals (Evaluation Metrics)]] — Layer 2
- [[Claude Code]] — first major agent studied through this framework
- [[summary-25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny]] — source summary
