---
title: "Proof Assistants"
type: concept
tags: [formal-methods, theorem-proving, tools]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md"]
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

## Related

- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
- [[Lean]] — a leading proof assistant
- [[Coq]] — a leading proof assistant
- [[Formal Verification]] — the program-verification use case
- [[Semantics of Programming Languages]] — what must be taught to prove programs
- [[CompCert]] — verified using a proof assistant
