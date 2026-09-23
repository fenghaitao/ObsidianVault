---
title: "Mario Carneiro"
type: entity
tags: [person, computer-scientist, lean]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura.md"]
last_updated: 2026-09-23
---

## Definition

Mario Carneiro (transcribed "Mario Kanedo") is a Lean contributor who implemented Lean4Lean ("Lean for Lean"), an independent Lean kernel written in Lean itself.

## Key Information

- Implemented an independent Lean kernel, written in Lean, as a cross-check of Lean's own (unverified) kernel.
- Is working toward proving that this kernel is verified with respect to the semantics of Lean.
- Part of de Moura's trust strategy: because proof checking is type checking in the kernel, having multiple independent kernels (Lean4Lean, plus user-written kernels in Rust and other languages) is the best guarantee that results are correct.

## Related

- [[Lean]] — the system his kernel verifies
- [[Interactive Theorem Proving]] — the activity his kernel checks
- [[Leonardo de Moura]] — Lean's creator
- [[Formal Verification]] — the trust model involved
- [[summary-20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura]] — source summary
