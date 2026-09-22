---
title: "Computer Architecture"
type: concept
tags: [computer-architecture, hardware, ISA, RISC]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260713 - Turing Award Winner： TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC ｜ David Patterson.md"]
last_updated: 2026-09-23
---
## Definition
Computer architecture is the design of the interface between software and hardware — instruction sets, microarchitecture, control, and the memory hierarchy — and, in Patterson's framing, its quantitative evaluation rather than design by intuition.
## Key Information
- In the 1970s-80s much of computer architecture was done "by intuition or gut," and even textbooks were "catalogues" that listed each machine's features without settling debates quantitatively — arguments were like "how many angels on the head of a pin."
- Patterson and Hennessy championed a scientific, measurement-based approach, which let the RISC vs CISC question finally be settled with ratios (how many more instructions vs how much faster each runs).
- The hard part of processor design, he argues, was control (see microprogramming); the instruction set question was really whether to keep a microcode interpreter or compile directly.
- The field was long guided by two scaling laws — Moore's law (transistor doubling) and Dennard scaling (constant power) — and their end reshaped it: multicore around 2005, then domain-specific architectures around 2015.
- The evolution: one sophisticated general-purpose CPU → many simpler cores → narrowly specialized accelerators (GPUs, TPUs), while CPUs remain the right tool for operating systems and compilers.
## Related
- [[summary-20260713 - Turing Award Winner： TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC ｜ David Patterson]] — source summary
- [[David Patterson]] — leading architect
- [[Hennessy & Patterson]] — the textbook and duo
- [[RISC vs CISC]] — the defining debate
- [[Moore's Law]] — a guiding scaling law
- [[Dennard Scaling]] — its power companion
- [[Domain-Specific Architecture]] — the post-Moore direction
- [[Microprogramming]] — the control technique RISC replaced
