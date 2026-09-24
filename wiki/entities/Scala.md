---
title: "Scala"
type: entity
tags: [language, functional-programming, object-oriented, statically-typed]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260919 - Creator of Scala： Rust, Zig, Python vs Scala ｜ Martin Odersky.md"]
last_updated: 2026-09-23
---
## Definition
Scala is a statically typed language that combines functional programming with object orientation and subtyping.

## Key Information
- SPJ positions Haskell and Scala as the two leading-edge statically typed languages (OCaml close behind), placing them in an "equivalence class" that isn't strictly comparable.
- Scala has "almost everything Haskell has" plus subtyping and object orientation — which makes it more complex and, he suggests, costly (Martin Odersky would agree).
- Odersky's framing: Scala is the only functional language that is also a very capable object-oriented language, born from a genuine synthesis of the two rather than a side-by-side blend; OOP contributes modules, components, and encapsulation, which pure FP mostly lacks.
- Scala 3 "looks a lot like Python" but with a strong, always-on type system; Scala also runs beyond the JVM on JavaScript/Node.js, WebAssembly (transcribed "WAM"), and native via LLVM.
- Selected design regrets: inheriting Java's universal methods (`toString`/`equals`/`hashCode`) instead of type classes, and introducing the full functional feature set at once — which fueled over-abstraction and a culture clash between functional- and object-oriented communities.

### Odersky on Scala vs Rust, Go, Zig, and Python
- Against Rust: Scala is garbage-collected, which means small pauses and needing a big chunk of memory; Rust runs in far smaller memory and is better for embedded, but Odersky thinks Rust is overused higher up the stack where GC is the simpler choice.
- Scala's GC cannot be turned off in production; research toward custom allocators would statically track references (like Zig) so reclaimed memory is never reached, but it has not shipped.
- Scala's `inline` is close to Zig's comptime inlining, with the added requirement that inlining introduce no new type errors (the C++ template failure mode).
- Against Python: Scala has an always-on strong type system that guarantees "certain bad states can't happen"; syntactically Scala 3 is "quite close" to Python.

## Related
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[Haskell]] — the other type-system leader
- [[Type System]] — where it competes with Haskell
- [[Object-Oriented Programming]] — the paradigm it adds
- [[Martin Odersky]] — the creator
- [[JVM]] — the original platform
- [[Type Classes]] — what he wishes Scala had used
- [[Capability-Based Security]] — the AI-era direction
- [[summary-20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky]] — source summary
- [[summary-20260919 - Creator of Scala： Rust, Zig, Python vs Scala ｜ Martin Odersky]] — source summary
- [[Rust]] — the embedded / memory-footprint contrast
- [[Go (Programming Language)]] — the deliberately small contrast
- [[Zig]] — the comptime-inlining comparison
- [[Python]] — the dynamically typed contrast
- [[Garbage Collection]] — can't be turned off in production
