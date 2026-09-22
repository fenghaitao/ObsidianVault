---
title: "Turing Completeness"
type: concept
tags: [concept, computer-science, computability]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md"]
last_updated: 2026-09-22
---
## Definition
Turing completeness is the property of a computational system that can simulate a Turing machine — able to compute anything computable given unlimited resources.

## Key Information
- Someone demonstrated the C++ template instantiation mechanism is Turing complete (calculating prime numbers at compile time, using error messages to report results).
- The requirements to reach Turing completeness: some form of iterate/recurse plus a comparison.
- Bjarne's response to the suggestion he should "ban it": "this looks useful. Great." Real machines are finite, so a compiler runs out of resources long before infinite loops become a real problem; bugs get caught.
- Misusing templates for factorial/prime calculations is "awful," expensive, and memory-hungry — which is why he and Gabriel Dos Reis built `constexpr` to do compile-time computation in ordinary code.

## Related
- [[summary-20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup]] — source summary
- [[Template Metaprogramming]] — where it appeared in C++
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
