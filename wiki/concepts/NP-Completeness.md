---
title: "NP-Completeness"
type: concept
tags: [complexity-theory, computer-science, reductions]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams.md"]
last_updated: 2026-09-23
---

## Definition

NP-completeness is the property of the hardest problems in NP: NP-complete problems are as hard as all problems in NP, so solving one efficiently solves all of them, and proving one hard proves all of them hard.

## Key Information

- Wigderson distinguishes NP-complete (as hard as all of NP) from NP-hard (at least as hard); examples include satisfiability, graph coloring, Sudoku, the traveling salesman problem, and protein folding formulated as energy minimization.
- Discovered in the early 1970s by Cook and Levin; their first NP-complete problem was satisfiability. Richard Karp subsequently showed many natural problems are NP-complete.
- The reason reductions are usually simple is that computation is local: a machine's time evolution consists of local bit operations, so any NP computation can be written as local Boolean constraints — which is why coloring, Sudoku, and factoring all reduce into satisfiability.
- Factoring integers reduces to satisfiability because given factors you can just multiply and check, and multiplication is a simple local algorithm.
- Real-world instances are often NOT worst case: protein folding, the simplex method for linear programs, and SAT solving all work in practice on the restricted, structured instances that actually arise, even though worst-case instances are exponentially hard.
- A stronger conjecture: satisfiability problems may require roughly 2^(c·n) time — practitioners still use SAT solvers because real formulas have structure and the worst case rarely shows up.
- Ryan Williams shows that subset sum (NP-complete, naive 2ⁿ) can be solved in ~2^(n/2) by reducing it to two-sum via meet-in-the-middle — an instance-blowing-up reduction that classical P vs NP theory cannot make, but fine-grained complexity can.
- This illustrates a general fine-grained phenomenon: problems that look like they "should have nothing to do with each other" (an NP-complete problem and a polynomial one) can still be related through their exact time complexity.

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[P vs NP]] — whether these classes collapse
- [[Boolean Satisfiability]] — the canonical complete problem
- [[Computational Complexity Theory]] — the field
- [[Stephen Cook]] — co-founder of the concept
- [[Leonid Levin]] — co-founder of the concept
- [[Richard Karp]] — advanced the reductions
- [[AlphaFold]] — practical example on structured instances
- [[Hardness of Approximation]] — how close you can get
- [[Interactive Proofs]] — generalize NP
- [[Oded Goldreich]] — used it for ZK universality
- [[Protein Folding]] — NP-hard example
- [[Zero-Knowledge Proofs]] — reduced to NP statements
- [[summary-20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams]] — source summary
- [[Subset Sum]] — NP-complete speedup via fine-grained reduction
- [[Meet-in-the-Middle]] — the speedup technique
- [[Fine-Grained Complexity]] — relates NP-complete and polynomial problems
