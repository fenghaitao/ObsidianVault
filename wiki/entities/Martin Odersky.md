---
title: "Martin Odersky"
type: entity
tags: [person, programming-languages, Scala, academic]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260919 - Creator of Scala： Rust, Zig, Python vs Scala ｜ Martin Odersky.md"]
last_updated: 2026-09-23
---

## Definition

Martin Odersky is a computer scientist and professor at EPFL best known as the creator of the Scala programming language, which he designed as a genuine fusion of functional and object-oriented programming.

## Key Information

- The transcript intro garbles his name as "Martin Oderski"; the canonical spelling is Martin Odersky.
- He holds a PhD supervised by Niklaus Wirth (transcribed "Nicholas W."), and describes himself as an imperative programmer by origin who learned Pascal and Modula first and later converted to functional programming.
- Before Scala he worked with Phil Wadler on Pizza, a predecessor language that aimed to put an accessible functional language on the then-widespread JVM; to prepare, he wrote a Java compiler by hand in about three months (half-time).
- Scala (the second iteration after Pizza) was a blend of Java, OCaml/Standard ML, and Haskell: Java for the platform and objects, OCaml for modules/components, and Haskell for much of the standard library.
- Scala's development ran roughly 1998 to 2004/2005, when Java was an open language standard and building on it carried no licensing concerns.
- He teaches at EPFL (transcribed "DPFL") and on Coursera (transcribed "Corera"), with courses partly based on Structure and Interpretation of Computer Programs.
- His forward-looking position: as AI generates more code, languages must pivot to stronger types and capability safety so types become a reviewable contract between humans and AI, and capabilities give AI agents fine-grained permissions.
- His advice to his younger self: take risks, be adventurous, and be a bit non-conformist rather than following the mainstream.

### On the Rust / Go / Zig / Python comparison (20260919)
- Believes Rust is "actually overused" above the embedded/OS level: if you have the memory for a garbage collector, "you should absolutely use one" because it makes many things simpler.
- Sees Go as an intentionally small language that lags behind but whose limits force a uniform, readable style; Zig has a nifty comptime inlining he rates above Rust's clunkier macros.
- Positions Scala's edge over Python as an always-on strong type system guaranteeing "certain bad states can't happen"; notes Scala's GC cannot be turned off in production, though custom-allocator research tracks references statically.

## Related

- [[Scala]]
- [[EPFL]]
- [[Phil Wadler]]
- [[JVM]]
- [[Java]]
- [[Type System]]
- [[Type Classes]]
- [[Capability-Based Security]]
- [[Functional Programming]]
- [[Object-Oriented Programming]]
- [[summary-20260919 - Creator of Scala： Rust, Zig, Python vs Scala ｜ Martin Odersky]] — source summary
- [[Rust]] — overused above embedded, per Odersky
- [[Go (Programming Language)]] — the deliberately small language
- [[Zig]] — praised for comptime inlining
- [[Python]] — the dynamically typed contrast
- [[Garbage Collection]] — the simpler choice when memory allows
