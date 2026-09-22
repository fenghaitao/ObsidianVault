---
title: "Domain-Specific Architecture"
type: concept
tags: [computer-architecture, accelerators, GPU, TPU, machine-learning]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260713 - Turing Award Winner： TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC ｜ David Patterson.md"]
last_updated: 2026-09-23
---
## Definition
A domain-specific architecture is a processor designed for a narrow class of programs — such as graphics or machine learning — sacrificing generality for large gains in efficiency for that domain.
## Key Information
- GPUs, which appeared around 2000, were the first modern examples: a "graphics processing unit" with one job that didn't need virtual memory or even compiler support.
- After Dennard scaling (2005) and Moore's law (2010s) ran out, general-purpose CPUs stagnated, so ~2015 architects turned to domain-specific designs — "if I only have to run a narrow class of programs, I can shuffle resources to do something much more efficient."
- The pattern reappeared just as machine learning/AI "burst on the scene" (2012-2015), making ML/AI the obvious domain; Google's TPU (2016) was the watershed that showed dedicated ML hardware could deliver dramatic, continued improvements for one domain.
- Trade-off: a specialized chip does some things well, others poorly or not at all — CPUs remain the right solution for operating systems and compilers.
- Patterson's counterfactual: had Dennard scaling continued, ~100 terahertz general-purpose chips would have "raised all boats" and GPUs would have stayed a niche.
## Related
- [[summary-20260713 - Turing Award Winner： TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC ｜ David Patterson]] — source summary
- [[Tensor Processing Unit (TPU)]] — Google's ML-specific accelerator
- [[Nvidia]] — the GPU that became an ML accelerator
- [[Computer Architecture]] — the field
- [[Moore's Law]] — its slowdown triggered the shift
- [[Dennard Scaling]] — whose end also forced specialization
