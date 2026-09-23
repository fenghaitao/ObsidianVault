---
title: "Formalization of Mathematics"
type: concept
tags: [mathematics, formal-methods, theorem-proving]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura.md"]
last_updated: 2026-09-23
---

## Definition

Formalization of mathematics is the translation of theorems and definitions into a machine-checkable formal language (such as Lean) so that proofs can be verified and collaboratively built atop a trusted, shared library.

## Key Information

- Requires a mathematical library (mathlib) with definitions (e.g. the real numbers) just to *state* a problem; with mathlib, stating IMO problems in Lean is "the easy part."
- Enables large-scale collaboration without trusting others' proofs: Lean can fill gaps and machine-check every step, so teams can work "in large numbers."
- The Liquid Tensor Experiment (2020; transcribed "liquid stencil experiments") formalized a Peter Scholze result he was unsure about — and the team even simplified the proof guided by Lean's step-by-step feedback, without fully understanding it.
- The unit-distance conjecture was formally *disproved* with a ~1-million-line Lean proof, completed about two weeks after being posted as a Lean challenge.
- Current frontier: AI can discover novel *proofs* (and counterexamples), but there is "no evidence yet" it can invent new mathematical concepts/objects on its own.
- Formalizing a subject is itself educational: anyone who formalizes something "understands the subject way better after that," a level beyond merely implementing it.

## Related

- [[Lean]] — the language and prover used
- [[mathlib]] — the shared mathematical library
- [[Interactive Theorem Proving]] — how the proofs are constructed
- [[Formal Verification]] — the software-reasoning sibling
- [[Peter Scholze]] — whose result was formally verified
- [[Terence Tao]] — an early adopter of formal mathematics in Lean
- [[Kevin Buzzard]] — a leader in formalizing mathematics
- [[summary-20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura]] — source summary
