---
title: "Foreign Function Interface"
type: concept
tags: [programming-languages, interoperability, OCaml]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md"]
last_updated: 2026-09-23
---

## Definition

A foreign function interface (FFI) is the mechanism by which a higher-level language (like OCaml or Python) calls functions written in a lower-level language (like C), bridging both control flow and data representation.

## Key Information

- The control-flow side is easy: the OCaml compiler emits a call to the C function using C calling conventions (or an interpreter uses dynamic loading such as `dlopen` to find a named function's address).
- The data side is hard because OCaml's and C's representations differ: an OCaml float is generally boxed (heap pointer, like a `double *`) not a raw `double`, and an OCaml two-dimensional array is an array of arrays (array of pointers), unlike C's contiguous rows.
- C code returning complex OCaml results (lists, arrays) must allocate in the OCaml heap and cooperate with the garbage collector via registration mechanisms.
- FFIs arrange this differently: the base C FFI is fast but requires C code to do all the work, while typed FFIs automate data conversion — sometimes expensively, e.g., copying a whole array when only two elements are needed.
- Xavier Leroy calls FFI work "a dirty part of programming language implementation" that's nonetheless necessary; Java's is also complicated.
- In compiled OCaml, C is joined by the C linker (like linking two object files), and Leroy is "a firm believer in static linking" to avoid runtime surprises such as missing DLLs.

## Related

- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
- [[OCaml]] — the high-level language
- [[C (Programming Language)]] — the lower-level target
- [[Python]] — another language that calls into C
- [[Garbage Collection]] — what C code must cooperate with when allocating OCaml data
