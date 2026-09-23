---
title: "Lean"
type: entity
tags: [tool, proof-assistant, formal-verification]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura.md"]
last_updated: 2026-09-23
---

## Definition

Lean is a proof assistant (interactive theorem prover) whose formal language lets users write mathematical definitions and statements and have proofs checked by machine.

## Key Information

- A leading example of proof assistants, alongside Coq and Isabelle.
- Small proof steps are automated; the user still guides the prover through major steps, and the completed proof is rechecked by the machine.
- Works with generative AI: AIs can produce proofs in Lean's formal language, which a machine can then recheck — much more effective than human-checking English proofs.
- Lean is mathematics-oriented: it has no assignment, so verifying a program still requires teaching it the semantics of the programming language (what assignment, plus, etc., mean).

- Created by Leonardo de Moura (also creator of Z3) with Sebastian Ullrich; born to fill Z3's gap of being strong at finding bugs but weak at proving their absence.
- A dependently typed functional programming language close to Haskell, plus proof support: proofs are written interactively in "tactic mode" and checked by a small kernel.
- Proof checking is type checking in the kernel (~5,000 lines by design); multiple independent kernels (e.g. Mario Carneiro's Lean4Lean) cross-check exported developments.
- Software verification: **shallow embedding** (translate a program into Lean, e.g. a Rust-to-Lean tool) versus **deep embedding** (transcribed "jeep badging" — write the target language's semantics in Lean so programs become Lean objects).
- Tooling mirrors a modern language — Lake (the build system, like cargo/make), doc-gen, and VS Code with a two-pane Info View giving constant feedback on the proof state.
- Self-hosted: originally C++, ~100k lines rewritten in Lean itself — a painful bootstrap whose required foundational proofs felt "almost like programming in assembly."
- Central to IMO-solving AI: problems are translated into Lean (easy thanks to mathlib) and the AI proves them via reinforcement learning against the goal state.
- Extensibility is a major draw: because Lean is implemented in Lean, users add meta-programs/extensions (e.g. Patrick Massot's natural-language proofs) without touching core Lean.

## Related

- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
- [[Proof Assistants]] — the category Lean belongs to
- [[Coq]] — a peer proof assistant
- [[Formal Verification]] — the activity it supports
- [[Semantics of Programming Languages]] — the bridge required to prove programs
- [[Leonardo de Moura]] — creator
- [[Sebastian Ullrich]] — co-creator
- [[Z3]] — the predecessor that motivated Lean
- [[mathlib]] — its mathematical library
- [[Dependent Type Theory]] — its logical foundation
- [[Interactive Theorem Proving]] — its proof workflow
- [[Formalization of Mathematics]] — its core math use case
- [[Mario Carneiro]] — the Lean4Lean kernel
- [[summary-20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura]] — source summary
