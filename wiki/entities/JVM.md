---
title: "JVM"
type: entity
tags: [technology, virtual-machine, Java, runtime]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md"]
last_updated: 2026-09-23
---

## Definition

The JVM (Java Virtual Machine) is a runtime defined by its bytecode — an intermediate format into which programs are translated, then executed by an interpreter and an optimizing just-in-time (JIT) compiler.

## Key Information

- Its contract is bytecode: if a language can emit bytecode (which "is not very hard"), it can run on the JVM.
- The harder interop work is mapping Java library concepts into the target language's concepts so the compiler understands and documents them.
- Advantages Odersky cites: access to the entire Java library ecosystem, the JVM's high-performance garbage collectors, and runtime class loading (which makes a REPL easy — compile a snippet to bytecode, load it into the running process, and execute).
- Scala was born on the JVM but is now multi-platform, also targeting JavaScript/Node.js, WebAssembly (transcribed "WAM"), and native code via LLVM.

## Related

- [[Scala]]
- [[Java]]
- [[Martin Odersky]]
- [[Just-in-Time Compilation]]
- [[Garbage Collection]]
- [[LLVM]]
- [[Twitter]]
