---
title: "CompCert"
type: entity
tags: [tool, compiler, formal-verification, C]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md"]
last_updated: 2026-09-23
---

## Definition

CompCert is a formally verified C compiler led by Xavier Leroy, proved to translate C source into assembly that faithfully preserves the program's semantics — i.e., the compiler introduces no miscompilation bugs.

## Key Information

- Takes C code, produces assembly code, and is proved (in a proof assistant) that the assembly is faithful to the C.
- Requires defining exactly what "preserve the semantics of a program" means — hence formal semantics of the source and target languages.
- The proof is several thousand pages if written on paper; mechanical verification makes it machine-checkable and trusted despite its size.
- Written in a purely functional style so it would be easier to reason about later; the gap between program and mathematics is much shorter for functional code.
- Mechanized verification also helps evolve the program: add features, adapt proofs, and be sure no regression was introduced.

## Related

- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
- [[Xavier Leroy]] — its creator and leader
- [[C (Programming Language)]] — the source language it verifies
- [[Coq]] — the proof assistant used in the verification
- [[Formal Verification]] — the methodology
- [[Semantics of Programming Languages]] — what the proof must define
