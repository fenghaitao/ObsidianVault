---
title: "Bayesian Networks"
type: concept
tags: [probability, graphs, AI, causality]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260727 - Turing Award Winner： Early AI, LLM Predictions, Causality ｜ Judea Pearl.md"]
last_updated: 2026-09-23
---

## Definition

Bayesian networks are probabilistic graphical models that encode conditional independence relationships in a directed graph, making probabilistic inference tractable without exponentially large joint-probability tables.

## Key Information

- Motivation: expert systems needed to combine uncertain rules, but textbook probability requires exponential tables and time; humans instead rely on relevance judgments ("the color of my uncle's eye is irrelevant to a diagnosis").
- A graph encodes which variables are conditionally independent of which (given others); in the transcript the term is transcribed "Beijian network" / "bijian network."
- Philosophical tie: the axioms of conditional independence in probability mirror the axioms of graph separation, the "graphoid" theory Pearl developed jointly with Azaria Paz (transcribed "Aaria Paz").
- The graph can be supplied by judgment — defensible intuitive assumptions (e.g., "the sun doesn't listen to the rooster") — as well as by data.
- This work underpins Pearl's Turing Award and led to his later realization that probability still omits causal direction.

## Related

- [[Judea Pearl]] — co-creator
- [[Causality]] — what Bayesian networks still lacked
- [[Causal Inference]] — built on these graphs
- [[Ladder of Causation]] — the hierarchy above association
- [[Expert Systems]] — the uncertainty hurdle that motivated them
- [[Machine Learning]] — probabilistic learning context
- [[Turing Award]] — the award for this work
- [[summary-20260727 - Turing Award Winner： Early AI, LLM Predictions, Causality ｜ Judea Pearl]] — source summary
