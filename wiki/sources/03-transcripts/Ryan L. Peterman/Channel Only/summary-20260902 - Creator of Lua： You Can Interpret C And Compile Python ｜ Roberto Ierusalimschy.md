---
title: "summary-20260902 - Creator of Lua： You Can Interpret C And Compile Python ｜ Roberto Ierusalimschy"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260902 - Creator of Lua： You Can Interpret C And Compile Python ｜ Roberto Ierusalimschy.md"]
last_updated: 2026-09-23
---

## Core Summary

Roberto Ierusalimschy argues that "compiled" versus "interpreted" is a property of the toolchain, not of the source code — you could compile Python into machine code, and you could write an interpreter for C, even if it would be extremely slow. The real hallmark of a dynamic language is `eval` (creating code while running), which is why keeping `eval` forces a compiler into the runtime library and why dynamic languages are usually interpreted. Type systems matter to compilation because knowing types lets a compiler size variables and emit direct typed arithmetic, whereas a dynamic `a + b` must be resolved at runtime. Type inference is not that shortcut: for dynamic languages it is generally not computable, and useful performance comes instead from informally following type discipline.

## Key Points

- "Compiled" vs "interpreted" lives in the toolchain, not the language: you can write a compiler that turns Python into machine code, and you can write an interpreter for C — though interpreting C would be extremely slow.
- `eval` — the ability to create code while running — is the hallmark of a dynamic language; to compile while keeping `eval`, the compiler must be available as a library of the runtime.
- Type systems greatly ease compilation: known types give exact variable sizes (int/float/double) and let `a + b` compile to one typed instruction, avoiding the heap allocation and runtime type checks dynamic languages pay.
- Types that do not guarantee anything (TypeScript-style annotations) cannot be used to lay out registers or compile.
- Type inference for dynamic languages is generally not computable; attempts either demand a rigid coding style or infer overly generic types with no performance benefit.
- Following an informal type discipline (not reusing one variable for integers and strings) yields much better performance in Lua and LuaJIT even though the language does not enforce it.

## Related

- [[Roberto Ierusalimschy]] — guest
- [[Lua]] — the language he created
- [[Python]] — the "compiled Python" example
- [[C (Programming Language)]] — the "interpret C" example
- [[Dynamic Languages]] — `eval` as the hallmark
- [[Static and Dynamic Typing]] — compiled vs interpreted and types
- [[Type System]] — how types aid compilation
- [[Type Inference]] — not a shortcut for dynamic languages
- [[Language as a Library]] — compiler as a runtime library for `eval`
- [[Ryan L. Peterman]] — host
