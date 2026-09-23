---
title: "Ladder of Causation"
type: concept
tags: [causality, hierarchy, inference]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260727 - Turing Award Winner： Early AI, LLM Predictions, Causality ｜ Judea Pearl.md"]
last_updated: 2026-09-23
---

## Definition

The Ladder of Causation is Judea Pearl's three-level hierarchy of causal queries: association (seeing), intervention (doing), and counterfactuals (imagining/explaining), where answering a query at one level requires assumptions from that level or above.

## Key Information

- Level 1, association: passive statistics and correlation — "if I see X, what can I tell about Y?" — the entire content of statistics 101.
- Level 2, intervention: doing/forcing (experiments) — "what if I make you smoke five packs a day?"
- Level 3, counterfactuals: explanation/retrospection given an observed outcome — "what if I had not smoked, given I'm 80 and healthy?"
- Formal hierarchy: you cannot climb from level i to level i+1 without higher-level assumptions.
- LLMs do not violate the ladder because they ingest human-interpreted knowledge (articles written by physicians and reviewers), not raw data; but that also means they summarize others' introspection rather than performing their own.

## Related

- [[Causality]] — the theory behind the ladder
- [[Causal Inference]] — answering queries by level
- [[Counterfactuals]] — level three
- [[do-Calculus]] — level two
- [[Bayesian Networks]] — association-level machinery
- [[Artificial General Intelligence]] — needs the higher levels
- [[Judea Pearl]] — proposed the ladder
- [[summary-20260727 - Turing Award Winner： Early AI, LLM Predictions, Causality ｜ Judea Pearl]] — source summary
