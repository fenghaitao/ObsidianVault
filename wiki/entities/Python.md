---
title: "Python"
type: entity
tags: [programming-language, scripting, data-science]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260504 - Meta Superintelligence Labs (MSL) Eng Director： Promo Hacking, Industry Shifts, Regrets ｜ John White.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260518 - Creator of C++： Bell Labs, Negative Overhead Abstraction, Mistakes ｜ Bjarne Stroustrup.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260722 - Harvard Professor On Why You Should Learn C in 2026 ｜ David Malan.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260902 - Creator of Lua： You Can Interpret C And Compile Python ｜ Roberto Ierusalimschy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260919 - Creator of Scala： Rust, Zig, Python vs Scala ｜ Martin Odersky.md"]
last_updated: 2026-09-23
---

## Definition

Python is a high-level, dynamically-typed programming language. John Myles White notes its dynamism imposes runtime overhead and that its high-performance libraries are actually written in lower-level languages.

## Key Information

- Like R, Python pays overhead for possible dynamic behavior (e.g., you can manipulate the symbol table via the `inspect` module, so you can never be sure what something is bound to).
- High-performance Python libraries (e.g., PyTorch) are ultimately C++ code, handwritten assembly, or GPU kernels underneath.

- Bjarne Stroustrup: Guido van Rossum built Python with the explicit aim of letting "many people or even everybody" program — and succeeded; Bjarne designed C++ for serious programmers, "not the same problem."
- Raw Python runs ~70x slower than raw C++; its viability comes from key libraries written in C/C++, recreating the high-level + low-level split he designed C++ to avoid.
- James Cowling: Magic Pocket's initial prototype was written in Python, which he defends as "actually pretty efficient for IO" and unfairly maligned for IO-bound workloads, though less suited to concurrency, memory management, and refactoring.
- David J. Malan (2026): in CS50, the week-5 hand-built C hash table "gets whittled down in week six to one line where you just instantiate a Python dictionary" — the payoff of first understanding the underlying structure before the high-level abstraction.

### Charlie Marsh on Python tooling
- Charlie saw the Python ecosystem lacking the native, performance-focused tooling that had become accepted in the JavaScript ecosystem (esbuild, SWC, Bun, Deno), with most Python tools written in Python itself.
- That gap inspired Astral's Ruff and uv, framed by his "Python tooling could be much, much faster" hypothesis.
- Astral's Red-knot type checker and uv package manager bring the native/Rust approach to Python tooling.

### Roberto Ierusalimschy on Lua vs Python
- Lua and Python have very different goals: Python is a huge, library-rich language for quick general-purpose programming, while Lua is almost the opposite — intentionally minimal, expecting the host program to supply the useful libraries.
- Lua is often much faster than Python because Lua consciously focuses on performance (features are only added if implementable efficiently), is less dynamic, and its small virtual machine fits in cache.
- Roberto: in Python "everything can mean something else," producing many runtime interactions; Lua is more conservative, which contributes to the performance gap.
- Python's truthy/falsy coercion (zero, empty list, empty string are false) is an easy-writing/easy-mistake trade-off; Lua only added Booleans to get `false` and keeps `true` nearly useless.
- Sandboxing story: a large Python financial program embedded Lua for its user-facing command line because Python cannot be sandboxed — arbitrary Python can do anything to the program, whereas a fresh Lua state can only call functions the host registers.
- Odersky: Python is ubiquitous with nice, readable syntax; among dynamically typed languages he also names Scheme — "very grounded in computer science theory and lambda calculus" — though Python is "100 times more popular."
- The gap between Scala and Python is closing: Python added optional type syntax plus type checkers, and pattern matching — features Scala had from the start; languages broadly drift toward a shared feature set originating in functional programming.
- Scala's edge over Python: a strong, always-on type system that guarantees "certain bad states can't happen," versus Python where types are "just syntax," have fewer guarantees, and a culture that values types less.
- Python's great strength is as a glue language with efficient linkages to high-performance C++ libraries (pandas, NumPy).
- Odersky's standout among dynamically typed languages: Python is "ubiquitous" with nice, easy-to-read syntax; he tracks Scheme as the other meaningful dynamic standout but stresses Python is "100 times more popular."
- Scala 3 is "quite close" to Python syntactically, so the real difference is Scala's always-on strong type system versus Python's optional, lower-guarantee types.
- Roberto's "compiled Python" point: nothing in Python's source prevents compilation — you can write a compiler that turns Python code into machine code; it's the dynamic-language need to support `eval` at runtime, not the syntax, that keeps it mostly interpreted.

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
- [[Charlie Marsh]] — founder of Astral
- [[Astral]] — Python dev-tools company
- [[Ruff]] — Python linter in Rust
- [[uv]] — Python package manager in Rust
- [[Red-knot]] — Python type checker
- [[mypy]] — earlier Python type checker
- [[summary-20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh]] — source summary
- [[summary-20260722 - Harvard Professor On Why You Should Learn C in 2026 ｜ David Malan]] — source summary
- [[summary-20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling]] — source summary
- [[Martin Odersky]] — Scala-vs-Python comparison
- [[Scala]] — the strongly typed contrast
- [[Scheme]] — the other dynamic standout he names
- [[Type System]] — where Scala has the edge
- [[summary-20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky]] — source summary
- [[summary-20260902 - Creator of Lua： You Can Interpret C And Compile Python ｜ Roberto Ierusalimschy]] — source summary
- [[summary-20260919 - Creator of Scala： Rust, Zig, Python vs Scala ｜ Martin Odersky]] — source summary
- [[Pandas]] — high-performance C++-backed library
- [[NumPy]] — high-performance C++-backed library
