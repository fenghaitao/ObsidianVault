---
title: "Proof Assistants"
type: concept
tags: [formal-methods, theorem-proving, tools]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura.md"]
last_updated: 2026-09-23
---

## Definition

Proof assistants (also called proof assistants/provers, e.g., Lean, Coq, Isabelle) are tools with a formal language for writing mathematical definitions and statements and for guiding proofs, with the machine rechecking completed proofs.

## Key Information

- Originally developed to do mathematics on a computer; they can also be used for formal verification of programs.
- Contrast with automatic theorem proving (the machine finds proofs alone, which is very hard); assistants automate small proof steps and let the user guide the major ones.
- Completed proofs are recorded in a machine-understandable format and rechecked, ensuring every inference is justified, no case is forgotten, and no conclusion is used as a hypothesis.
- Reliable enough for big results where proofs are too large for humans — e.g., a weak Goldbach conjecture effort involving checking thousands of inequalities in several real variables.
- Combine well with generative AI: an AI can produce proofs in a formal language like Lean that a machine rechecks, which is far more effective than a human checking English prose (though the statement and any "self-formalization" still need review).
- To prove properties of programs, the assistant must be taught the semantics of the programming language (what assignment and arithmetic mean), since mathematics has no assignment.

- Some proof assistants (Lean, Rocq/Coq) are also programming languages in the dependently typed family — "Rock and Lean are programming languages and proof assistants."
- Lean's tactic mode is a domain-specific language for proofs with a live Info View; users describe the interactive loop as a game, and "no goals left" marks a finished proof.
- Contrast with fully automatic SMT (Z3): push-button but unable to prove non-trivial absence of bugs; interactive assistants let you break a proof into influenceable steps.
- Only the checker (kernel) must be trusted: independent kernels (Lean4Lean, plus user kernels in Rust and other languages) cross-check exported developments.

## Related

- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
- [[Lean]] — a leading proof assistant
- [[Coq]] — a leading proof assistant
- [[Formal Verification]] — the program-verification use case
- [[Semantics of Programming Languages]] — what must be taught to prove programs
- [[CompCert]] — verified using a proof assistant
- [[Leonardo de Moura]] — Lean's creator
- [[Z3]] — the automatic contrast
- [[Dependent Type Theory]] — the logic underpinning some assistants
- [[Interactive Theorem Proving]] — the workflow
- [[Formalization of Mathematics]] — the math use case
- [[summary-20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura]] — source summary
