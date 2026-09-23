---
title: "seL4"
type: entity
tags: [microkernel, formal-verification, operating-systems]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura.md"]
last_updated: 2026-09-23
---

## Definition

seL4 is a formally verified microkernel developed in Australia, used as a hypervisor in some applications, with every line of its ~8,000 lines of C proved correct.

## Key Information

- Manipulates processes, capabilities, and security tokens in extremely technical C.
- "Every line has been proved correct" — a very big achievement in certified software cited by Xavier Leroy alongside his own CompCert.
- Demonstrates that mature, real-world systems software (not just toy examples) can be exhaustively verified.

- Leonardo de Moura cites seL4 as a "major milestone": a microkernel verified manually before AI, at super-expensive cost — the poster child for why formal verification stayed niche until AI changed the game.

## Related

- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
- [[Formal Verification]] — how it was proved correct
- [[Memory Safety]] — the property such verification establishes
- [[C (Programming Language)]] — the implementation language
- [[CompCert]] — another landmark verified-systems achievement
- [[Leonardo de Moura]] — cites seL4 as the manual-verification cost benchmark
- [[Formal Verification]] — the field seL4 exemplifies
- [[summary-20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura]] — source summary
