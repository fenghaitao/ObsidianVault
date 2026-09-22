---
title: "Strong Exponential Time Hypothesis (SETH)"
type: concept
tags: [complexity-theory, computer-science, hypothesis]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams.md"]
last_updated: 2026-09-23
---

## Definition

The Strong Exponential Time Hypothesis (SETH) is the conjecture that SAT cannot be solved substantially faster than 2ⁿ — specifically, that K-SAT, for arbitrary clause width K, requires time approaching 2ⁿ as K grows.

## Key Information

- SETH is "a severe strengthening of the P versus NP question": P vs NP only rules out a polynomial-time algorithm, while SETH claims you essentially need close to 2ⁿ time for the SAT problem.
- Precisely: for every string of nines, there is no 1.999…9ⁿ-time algorithm for SAT — the hypothesis is stated through K-SAT over clauses of length K for arbitrary K.
- Ryan Williams is "on the record as not believing this hypothesis" — a minority opinion — but says the truth value is almost irrelevant to him because assuming it false forces him to think in new directions and has repeatedly produced other results.
- It was deliberately named a "hypothesis" rather than a "conjecture" to provoke thought; co-proposer Russell Impagliazzo (transcribed in this episode as "Russell and Piazzo") emphasized it was meant as something more controversial than P = NP-type beliefs.
- Believing SETH conveniently implies many other lower bounds (edit distance, various pattern-matching problems), since improving any of those would improve SAT below 2ⁿ; it makes a "convenient worldview" in which textbook algorithms are optimal.

## Related

- [[summary-20260629 - MIT Professor： Leetcode, P vs NP, SAT Solvers ｜ Ryan Williams]] — source summary
- [[Ryan Williams]] — publicly doubts it
- [[P vs NP]] — the question it strengthens
- [[Boolean Satisfiability]] — the SAT problem it concerns
- [[Fine-Grained Complexity]] — the field it anchors
- [[Computational Complexity Theory]] — parent field
