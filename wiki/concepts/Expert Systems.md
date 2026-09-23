---
title: "Expert Systems"
type: concept
tags: [AI, knowledge-representation, uncertainty]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260727 - Turing Award Winner： Early AI, LLM Predictions, Causality ｜ Judea Pearl.md"]
last_updated: 2026-09-23
---

## Definition

Expert systems are early AI programs that encode an expert's rules (e.g., medical diagnosis) as logic. They reached a hurdle in combining uncertain rules, which motivated Judea Pearl's Bayesian networks.

## Key Information

- Example: MYCIN (transcribed "Mason"), developed by Ed Feigenbaum (transcribed "Ed Fenbomb") and colleagues for medical analysis.
- The approach began with logical rules, but real knowledge is corrupted by uncertainty, so practitioners tried to attach percentages (e.g., "if you came from Asia, 50% chance of malaria").
- Logic tells you how to combine certain assertions but not uncertain ones; probability does, but textbook probability is exponentially expensive.
- Pearl later showed the naive rules-based approach could not work: probabilities do not combine the way logical assertions combine.
- This failure was the immediate motivation for Bayesian networks, which encode conditional independence in a graph.

## Related

- [[Judea Pearl]] — identified the limitation
- [[Bayesian Networks]] — the solution that followed
- [[Machine Learning]] — the broader AI context
- [[summary-20260727 - Turing Award Winner： Early AI, LLM Predictions, Causality ｜ Judea Pearl]] — source summary
