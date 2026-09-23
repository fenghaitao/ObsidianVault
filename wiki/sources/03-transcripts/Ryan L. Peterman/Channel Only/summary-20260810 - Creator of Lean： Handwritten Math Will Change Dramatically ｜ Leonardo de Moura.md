---
title: "summary-20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura.md"]
last_updated: 2026-09-23
---

## Core Summary

Leonardo de Moura, creator of the Lean proof assistant and earlier the Z3 SMT solver, explains that Lean is both a programming language and an interactive theorem prover, and that with AI the cost of formal verification has collapsed. He frames formal proofs as what shows the *absence* of bugs, whereas (per Dijkstra's famous dictum) testing can only show their presence, and cites real examples from seL4 to Kim Morrison's team who translated a C compression library into Lean and proved compress-then-decompress returns the original data in about a week. De Moura, who now works at AWS, sees a future where humans write specifications and AI synthesizes and proves the code — changing both software and mathematics without ending handwritten math. Over 13 years Lean grew from a research project born of Z3's limitations into a nonprofit-backed platform whose math-first community and mathlib drew Fields Medalists and IMO-verifying AI systems.

## Key Points

- Lean is a dependently typed functional programming language *and* a proof assistant: you write code, state properties about it, and prove them, obtaining machine-checkable absolute assurance.
- Software verification has two approaches: **shallow embedding** (translate a program into Lean, e.g. a Rust-to-Lean tool) and **deep embedding** (transcribed "jeep badging" — write the target language's semantics in Lean so programs become Lean objects you can reason about).
- The expensive part of verification is not writing the spec but developing and *maintaining* proofs as code changes; AI is now good at writing, maintaining, and even re-proving formal proofs.
- Example: a colleague (Kim Morrison) prompted AI to translate a C compression library to Lean, pass its test suite, and prove compress-then-decompress recovers the original data — "after one week."
- A specification is a superset of a test suite: tests sample cases while a proof covers all possible cases; an inefficient naive program can serve as the specification that AI optimizes against ("inefficient program is a spec").
- You only have to trust Lean's small kernel (proof checking is type checking); the kernel is ~5,000 lines by design and multiple independent kernels (e.g. Mario Carneiro's Lean4Lean) cross-check results.
- Proof assistants broke IMO: DeepMind's AlphaProof got silver in 2024, golds now follow (incl. ByteDance); OpenAI's unit-distance-conjecture result was formally disproved with a ~1-million-line Lean proof in ~2 weeks.
- The Liquid Tensor Experiment (2020, transcribed "liquid stencil experiments") verified a Fields Medalist Peter Scholze's unpublished result he was unsure of — and the team even simplified the proof guided by Lean's interactive feedback.
- Dependent type theory was chosen over higher-order logic for Lean at the urging of Jeremy Avigad, to attract serious mathematicians; dependent types express "a proof that x > y" as a type.
- Z3 (SMT solver) is fully automatic "push-button" and good at finding bugs, but weak at proving absence of bugs ("proof instability"); Lean was created to fill that gap.
- Roadmap: the Lean nonprofit (est. 2023, co-founded with Sebastian Ullrich) is pushing Lean as a programming language for software verification, backed by AWS's largest donation; de Moura expects this to be "the decade of formal verification."
- Advice: formalize when something is safety-critical or poorly understood; learning Lean with an AI agent (plus the free Lean books) is the fastest path.

## Related

- [[Leonardo de Moura]]
- [[Lean]]
- [[Z3]]
- [[mathlib]]
- [[Dependent Type Theory]]
- [[Interactive Theorem Proving]]
- [[Formalization of Mathematics]]
- [[Satisfiability Modulo Theories]]
- [[Formal Verification]]
- [[Proof Assistants]]
- [[Programming Language Design]]
- [[Semantics of Programming Languages]]
- [[Coq]]
- [[Microsoft]]
- [[AWS]]
- [[Haskell]]
- [[Rust]]
- [[seL4]]
- [[Jane Street]]
- [[DeepMind]]
- [[OpenAI]]
- [[Edsger Dijkstra]]
- [[Terence Tao]]
- [[Kevin Buzzard]]
- [[Mario Carneiro]]
- [[Kim Morrison]]
- [[Peter Scholze]]
- [[Patrick Massot]]
- [[Jeremy Avigad]]
- [[Sebastian Ullrich]]
