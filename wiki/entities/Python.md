---
title: "Python"
type: entity
tags: [programming-language, scripting, data-science]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260504 - Meta Superintelligence Labs (MSL) Eng Director： Promo Hacking, Industry Shifts, Regrets ｜ John White.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md"]
last_updated: 2026-09-22
---

## Definition

Python is a high-level, dynamically-typed programming language. John Myles White notes its dynamism imposes runtime overhead and that its high-performance libraries are actually written in lower-level languages.

## Key Information

- Like R, Python pays overhead for possible dynamic behavior (e.g., you can manipulate the symbol table via the `inspect` module, so you can never be sure what something is bound to).
- High-performance Python libraries (e.g., PyTorch) are ultimately C++ code, handwritten assembly, or GPU kernels underneath.

- Bjarne Stroustrup: Guido van Rossum built Python with the explicit aim of letting "many people or even everybody" program — and succeeded; Bjarne designed C++ for serious programmers, "not the same problem."
- Raw Python runs ~70x slower than raw C++; its viability comes from key libraries written in C/C++, recreating the high-level + low-level split he designed C++ to avoid.
- James Cowling: Magic Pocket's initial prototype was written in Python, which he defends as "actually pretty efficient for IO" and unfairly maligned for IO-bound workloads, though less suited to concurrency, memory management, and refactoring.

## Related

- [[summary-20260504 - Meta Superintelligence Labs (MSL) Eng Director： Promo Hacking, Industry Shifts, Regrets ｜ John White]] — source summary
- [[John Myles White]] — discussed its performance
- [[R (Programming Language)]] — another dynamic language
- [[Julia (Programming Language)]] — aimed to match its ease with C speed
- [[PyTorch]] — a Python library backed by C++
- [[summary-20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup]] — source summary
- [[C++]] — the language its fast libraries use
- [[Guido van Rossum]] — Python's creator
- [[Static and Dynamic Typing]] — the trade-off it embodies
- [[Programming Language Design]] — a design-overhead example
- [[Go (Programming Language)]] — the language the Magic Pocket prototype was migrated to
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
