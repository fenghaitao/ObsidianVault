---
title: "R (Programming Language)"
type: entity
tags: [programming-language, statistics, data-science]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260504 - Meta Superintelligence Labs (MSL) Eng Director： Promo Hacking, Industry Shifts, Regrets ｜ John White.md"]
last_updated: 2026-09-14
---

## Definition

R is a statistical programming language whose slow performance and permissive dynamics frustrated John Myles White and helped motivate the Julia language.

## Key Information

- Distance-matrix code that is C for-loops underneath runs 1,000–10,000x slower when translated naively into R.
- R is slow because it pays overhead for possible dynamic behavior: e.g., the brace used to delimit a block can be overridden by the user, so the runtime must check whether it was redefined.
- R is lazily evaluated: function arguments are passed as "promise" objects and not evaluated until needed; a paper by Jan Vitek's group ("Evaluating the design of the R programming language") found ~70–90% of those promises did not need to be lazy.

## Related

- [[summary-20260504 - Meta Superintelligence Labs (MSL) Eng Director： Promo Hacking, Industry Shifts, Regrets ｜ John White]] — source summary
- [[John Myles White]] — heavy R user disappointed by it
- [[Julia (Programming Language)]] — the language built to fix this
- [[Python]] — another dynamically-typed language with similar issues
- [[Statistics]] — R's domain
- [[Programming Language Design]] — the broader topic
