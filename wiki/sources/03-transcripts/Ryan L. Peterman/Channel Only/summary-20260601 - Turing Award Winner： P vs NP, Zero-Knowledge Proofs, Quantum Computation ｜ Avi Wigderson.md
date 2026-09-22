---
title: "summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md"]
last_updated: 2026-09-22
---

## Core Summary

Avi Wigderson — winner of both the Turing Award and the Abel Prize — explains the central question of computational complexity theory, P versus NP, and frames it as a question about the limits of human knowledge: P is "what we can solve," NP is "all the problems we really want to solve." He walks through NP-completeness and reductions, why brute force still reigns for worst-case instances (while real-world instances like protein folding and linear programming are often structured enough to solve in practice), and how approximation can be exactly as hard as optimization. He then recasts randomness as a resource whose "quality is in the eye of the beholder," covering pseudorandomness, randomness extraction, and derandomization (hardness vs randomness). Finally he explains interactive and zero-knowledge proofs — how anything provable can be proved without revealing the proof — and closes with how quantum computation upended both complexity theory and cryptography, before reflecting on modeling as the real work of theoretical computer science.

## Key Points

- Wigderson defines P as the problems we can solve efficiently in our lifetime, and NP as the problems whose solutions are easy to verify — "all the problems we can honestly say we really want to solve." If P = NP, verification being easy would imply finding is easy, so "we can know everything we ever want to know" (limits of human knowledge).
- His intuition — shared by nearly all theoretical computer scientists — is that P ≠ NP: finding is usually harder than checking, and NP-complete problems have resisted 50–70 years of search while seeming to require an exponentially large search space.
- NP-complete problems are really families of instances; in practice software/engineering instances (verification, protein folding, linear programming) are a restricted, structured subset, not worst case. The simplex method solves linear programs in exponential worst-case time but appears to run in linear time on real inputs; AlphaFold succeeds because real proteins are a small, evolution-designed set.
- The PCP theorem (early 1990s) proved hardness of approximation; Håstad strengthened it to show that for three-variable constraints, random guessing satisfies 7/8, but achieving 7/8 + ε is already NP-hard — as hard as finding the optimum.
- Complexity classes classify problems by the resources they consume (time, space, communication, randomness, parallel time); Turing's work established that some problems are simply unsolvable, and the Complexity Zoo catalogs hundreds of classes.
- Cook and Levin made SAT the first NP-complete problem; the essential reason is that computation is local, so any machine's time evolution can be written as local Boolean constraints — which is why coloring, Sudoku, factoring, and satisfiability all reduce into one another.
- Time vs space: after ~50 years of a t/log t bound, Ryan Williams (2025) showed any time-t computation can be simulated in √t space (building on James Cook and Ian Mertz's result); earlier, Barrington showed majority can be computed in constant space via non-commutative algebra (permutations of a 5-element set) — a result used in cryptography.
- SAT solvers are popular because satisfiability is the one problem theorists optimized hardest with branching heuristics (set pivotal variables, force "domino" consequences) and because specifications translate naturally into constraints, even though the translation enlarges the instance.
- Randomized algorithms (e.g., Miller–Rabin and Solovay–Strassen primality tests) assume perfect, independent coin flips; since high-quality randomness is costly, complexity theory asks how to minimize or eliminate it, and understanding how an algorithm uses randomness often yields a deterministic version (the AKS primality test).
- Pseudorandomness: "the quality of randomness is in the eye of the beholder — or in the computational power of the beholder"; the Blum–Micali coin toss looks full-entropy to a person but fully predictable to a sensor-equipped Cray supercomputer, because only the observer's compute changed.
- Hardness vs randomness: if a hard function exists (exponential-size circuits for some problem), then P = BPP — every efficient probabilistic algorithm can be derandomized; the connection runs both ways, which is why theorists believe randomness in algorithms is weak.
- Randomness extraction/purification: weak physical sources (biased, correlated — weather, sunspots, stock prices) can't yield one perfectly random string, but can yield polynomially many blocks of length ≈ the source's entropy, 99% of which are perfect — run the algorithm on each and majority-vote. The sum-product theorem underpins multi-source extraction.
- Interactive proofs (Goldwasser–Micali–Rackoff, Babai in parallel) generalize NP to randomized conversations; zero-knowledge means the verifier learns nothing beyond that the claim is true. The GMW result shows every provable statement has a zero-knowledge proof, assuming one-way functions.
- One-way functions (multiply vs factor) underpin commitments and all e-commerce; trapdoor functions are rare, and Shor's 1994 quantum algorithm for factoring and discrete log broke the two underpinnings of all security systems, launching the race for quantum computers and quantum-resistant (lattice-based) assumptions.
- Quantum computation extends classical/probabilistic machines by superpositions ("probability theory with negative numbers"); it also transformed proof systems — MIP* = RE shows entangled quantum provers can convince an efficient verifier of uncomputable (halting-type) statements, with deep consequences for mathematics and physics.
- Wigderson sees theoretical computer science as living in both mathematics and computer science; he is motivated more by modeling than by applications (though ZK proofs — which he once thought would never be implemented — now matter in blockchains), and advises young researchers to work on what they enjoy most.

## Related

- [[Avi Wigderson]] — guest
- [[Turing Award]] — prize Wigderson holds
- [[Abel Prize]] — prize Wigderson holds
- [[P vs NP]] — central question
- [[NP-Completeness]] — the hardness backbone
- [[Computational Complexity Theory]] — the field
- [[Time Complexity]] — resource
- [[Space Complexity]] — resource
- [[Randomized Algorithms]] — randomness as a resource
- [[Pseudorandomness]] — observer-dependent randomness
- [[Randomness Extraction]] — purifying weak randomness
- [[Hardness vs Randomness]] — derandomization
- [[Interactive Proofs]] — proving interactively
- [[Zero-Knowledge Proofs]] — proving without revealing
- [[One-Way Functions]] — cryptographic foundation
- [[Cryptographic Commitment]] — hiding yet binding
- [[Hardness of Approximation]] — PCP theorem
- [[Boolean Satisfiability]] — SAT and solvers
- [[Primality Testing]] — probabilistic and deterministic tests
- [[Sum-Product Theorem]] — extraction ingredient
- [[Protein Folding]] — NP-hard in practice
- [[Quantum Computation]] — the new model
- [[Halting Problem]] — undecidability
- [[Millennium Prize Problems]] — the million-dollar framing
- [[Complexity Zoo]] — catalog of classes
- [[AlphaFold]] — real-world heuristic example
- [[Stephen Cook]] — co-founder of NP-completeness
- [[Leonid Levin]] — co-founder of NP-completeness
- [[Richard Karp]] — NP-completeness reductions
- [[Shafi Goldwasser]] — interactive/zero-knowledge proofs
- [[Silvio Micali]] — interactive/zero-knowledge proofs
- [[Oded Goldreich]] — GMW zero-knowledge result
- [[Charles Rackoff]] — interactive/zero-knowledge proofs
- [[László Babai]] — interactive proofs
- [[Manuel Blum]] — Blum–Micali randomness paper
- [[Noam Nisan]] — Nisan–Wigderson generator
- [[Scott Aaronson]] — Complexity Zoo founder
- [[Ryan Williams]] — time-space breakthrough
- [[David Barrington]] — constant-space majority
- [[Peter Shor]] — quantum factoring algorithm
- [[Richard Feynman]] — proposed quantum computation
- [[Claude Shannon]] — entropy and secrecy
- [[Johan Håstad]] — hardness of approximation
- [[Alan Turing]] — decidability and Turing machines
