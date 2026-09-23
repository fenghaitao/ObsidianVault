---
title: "Causality"
type: concept
tags: [causality, AI, probability, theory]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260727 - Turing Award Winner： Early AI, LLM Predictions, Causality ｜ Judea Pearl.md"]
last_updated: 2026-09-23
---

## Definition

Causality is the study of cause-and-effect relationships. Judea Pearl argues it requires its own mathematics, because probability captures association but not the directional, invariant character of causation.

## Key Information

- Pearl initially believed probability was sufficient to capture human reasoning, and confesses in the introduction to his book *Causality* that he was wrong.
- Empirical clue: when experts encode Bayesian networks, they always draw arrows from cause to effect and resist reversing them (symptom ↔ disease), revealing something extra that probability does not encode.
- Invariance: the causal relationship (disease → fever) is stable under local changes (e.g., relocating a car's charger in a diagnostic system), whereas the reversed relationship is not, so causal models amortize knowledge across modifications.
- Algebra's symmetric equality sign — celebrated since Galileo — lets one invert questions both ways, but it cannot express the directionality of cause and effect; computer science's non-reversible assignment operation supplies the missing direction.
- Pearl's framework answers causal queries on three levels: association, intervention, and counterfactuals (the Ladder of Causation).

## Related

- [[Judea Pearl]] — developed the formal theory
- [[Bayesian Networks]] — the probabilistic precursor
- [[Causal Inference]] — the practice of answering causal queries
- [[Ladder of Causation]] — the three-level hierarchy
- [[Counterfactuals]] — the explanation level
- [[do-Calculus]] — the calculus of intervention
- [[summary-20260727 - Turing Award Winner： Early AI, LLM Predictions, Causality ｜ Judea Pearl]] — source summary
