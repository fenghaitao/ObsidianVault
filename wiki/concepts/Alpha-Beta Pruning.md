---
title: "Alpha-Beta Pruning"
type: concept
tags: [AI, search, game-playing, algorithm]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260727 - Turing Award Winner： Early AI, LLM Predictions, Causality ｜ Judea Pearl.md"]
last_updated: 2026-09-23
---

## Definition

Alpha-beta pruning is an optimization for game-tree search that skips branches without changing the final result. Judea Pearl proved it is optimal in the number of positions inspected.

## Key Information

- Central to early AI game-playing systems (chess, checkers).
- Pearl frames chess AI as a tradeoff between fast "static evaluation" (intuition) and deeper search — an instance of the interplay between Kahneman's fast and slow thinking.
- He proved mathematically that alpha-beta cannot be beaten in the number of terminal positions inspected at a given search depth; the result surprised Donald Knuth (transcribed "Klo"), who had questioned it in his book.
- Led Pearl from search into broader work on reasoning, and eventually to Bayesian networks and causality.

## Related

- [[Judea Pearl]] — proved optimality
- [[Machine Learning]] — the learned evaluation-function complement
- [[summary-20260727 - Turing Award Winner： Early AI, LLM Predictions, Causality ｜ Judea Pearl]] — source summary
