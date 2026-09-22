---
title: "P vs NP"
type: concept
tags: [complexity-theory, computer-science, open-problem]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260706 - Turing Award Winner： The Invention of Public Key Cryptography ｜ Martin Hellman.md"]
last_updated: 2026-09-23
---

## Definition

P vs NP is the central open question of whether every problem whose solutions are easy to verify (NP) can also be solved efficiently (P).

## Key Information

- Wigderson's intuitive framing: P = the problems we can solve efficiently (with algorithms, in our lifetime); NP = "all the problems we can honestly say we really want to solve," defined as problems whose solutions are easy to check when handed to us.
- Every serious human endeavor has the "recognize the solution" property — mathematicians verifying proofs, scientists checking theories against data, engineers meeting constraints, detectives closing cases — which is why "all the problems we want to solve are really NP problems."
- If P = NP, then everything we want to know (cure for cancer, etc.) could be efficiently found just because a solution is easily recognized: "we can know everything we ever want to know." It is philosophically about the limits of human knowledge.
- It is one of the Millennium Prize Problems, with a million-dollar prize for a proof in either direction.
- Wigderson's intuition (shared by "almost all members of the theoretical computer science community") is P ≠ NP: finding is generally harder than checking; NP-complete problems resisted 50–70 years of search; and they seem to require searching an exponentially large space with no known general way to cut it down.
- Ryan Williams is notably less confident: he assigns only 80% to P ≠ NP (Scott Aaronson nudged him up from ~75%). His rationale is that algorithms constantly yield surprises whereas lower bounds rarely do, so "we really don't understand polynomial time computation as deeply as we think we do."
- Williams assigns even lower confidence to the exponential-time analogue: 45% for EXP ≠ NEXP (he believes NEXP = EXP more likely than not) and 80% for NEXP = coNEXP. His intuition for the latter: a "little birdie" can give an NEXP machine a compact count of "yes" inputs, letting it exhaustively guess and rule out all the "no" inputs.
- Martin Hellman ties the question to cryptography: if any secure cryptographic system exists, then there are problems that are easy to check but hard to solve — the essence of P vs NP.
- He frames a "trapdoor" cryptographic system as a P vs NP-style asymmetry the designer can exploit.

## Related

- [[summary-20260601 - Turing Award Winner： P vs NP, Zero-Knowledge Proofs, Quantum Computation ｜ Avi Wigderson]] — source summary
- [[NP-Completeness]] — the hardest problems in NP
- [[Computational Complexity Theory]] — the field
- [[Halting Problem]] — the undecidable corner beyond NP
- [[Millennium Prize Problems]] — the prize framing
- [[Avi Wigderson]] — articulates the question
- [[Hardness vs Randomness]] — the hardness cousin
- [[Quantum Computation]] — the related model
- [[summary-20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams]] — source summary
- [[Strong Exponential Time Hypothesis (SETH)]] — a strengthening of P vs NP
- [[Lance Fortnow]] — The Golden Ticket imagines P = NP
- [[summary-20260706 - Turing Award Winner： The Invention of Public Key Cryptography ｜ Martin Hellman]] — source summary (Hellman interview)
- [[Public Key Cryptography]] — depends on easy-to-check/hard-to-solve problems
- [[One-Way Functions]] — the cryptographic instantiation
- [[Martin Hellman]] — connects P vs NP to cryptography
