---
title: "Pipeline Parallelism"
type: concept
tags: [distributed-systems, ML, training, serving]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg.md"]
last_updated: 2026-09-22
---
## Definition
Pipeline parallelism (here "pipeline prefill") parallelizes model layers — rather than experts — across machines, so each layer processes a subset of a prefill request and hands tokens to the next machine.
## Key Information
- In the dense case, Sholto Douglas argued (correctly, Vlad confirmed) that models were flop-bound, so pipelining would not change the prefill profile; the idea was shelved.
- For mixture-of-experts models it was decisive: instead of routing tokens machine-to-machine on every layer (the MoE latency problem), one layer computes on one subset of the request and passes tokens forward.
- Experts can then stay resident on a single machine or a smaller set, breaking the HBM sharding constraint.
- Communication overhead drops because pipeline-prefill transfers between layers can be hidden behind other computation (layer 2 on the first thousand tokens while layer 1 handles the second thousand).
- Rahul Arya, a report (transcribed "Gangyan"), and Google's Israel team applied this to MoE for Flash 2.0; Dwarak Rajagopal and Reiner Pope wrote it up in the algebra of The Scaling Book.
## Related
- [[summary-20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg]] — source summary
- [[Vlad Feinberg]] — source
- [[Gemini Flash]] — application
- [[Mixture of Experts]] — what it enabled
- [[Sholto Douglas]] — discussed the dense case
- [[Rahul Arya]] — applied it to MoE
- [[Tensor Processing Unit (TPU)]] — the chips
