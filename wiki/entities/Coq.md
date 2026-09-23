---
title: "Coq"
type: entity
tags: [tool, proof-assistant, formal-verification]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura.md"]
last_updated: 2026-09-23
---

## Definition

Coq is a proof assistant — an interactive theorem prover — originally developed to do mathematics on the computer, and used by Xavier Leroy to verify the CompCert C compiler.

## Key Information

- Classified among proof assistants (with Lean and Isabelle) that record proofs in a machine-understandable, recheckable format.
- When a proof is completed and rechecked, the computer confirms every inference is justified, no case is forgotten, and no conclusion is used as an hypothesis.
- Leroy used Coq (in the episode he refers to it loosely as "the Rock" / proof assistant) to prove CompCert preserves C semantics down to assembly.
- Coq and OCaml's ecosystems have received many obviously AI-generated issue reports, prompting talk of refusing AI-generated contributions.

- Leonardo de Moura names Coq ("Rock"/Rocq) alongside Lean as a proof assistant that is also a programming language: "Rock and Lean are programming languages and proof assistants," part of the dependently typed family.

## Related

- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
- [[CompCert]] — the compiler Leroy verified with it
- [[Proof Assistants]] — the category Coq belongs to
- [[Lean]] — a peer proof assistant
- [[Formal Verification]] — the activity it supports
- [[Xavier Leroy]] — its most famous verification user here
- [[Leonardo de Moura]] — cites Coq/Rocq alongside Lean
- [[Dependent Type Theory]] — the shared foundation
- [[summary-20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura]] — source summary
