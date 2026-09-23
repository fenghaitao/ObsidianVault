---
title: "Lua"
type: entity
tags: [programming-language, scripting, embeddable]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260902 - Creator of Lua： You Can Interpret C And Compile Python ｜ Roberto Ierusalimschy.md"]
last_updated: 2026-09-23
---

## Definition

Lua is a minimal, embeddable scripting language created by Roberto Ierusalimschy, designed to run as the dynamic layer inside a host program (usually C or C++) rather than as a standalone platform.

## Key Information

- Positioned as a scripting language in a dual-language architecture: the host (C/C++) owns the main loop and calls Lua for dynamic, frequently changing tasks; in games the host keeps the frame rhythm and calls Lua each frame to update characters and state.
- Designed "as a library" from the start; its standalone console program is just a client of the library using the same API any embedding program uses.
- Uses `load` instead of `eval`: `load` compiles a chunk into a function (checking for errors) without executing it, keeping compilation separable from execution — friendlier for embedding in C.
- Has no global state: C creates an independent Lua state, and closing a state releases all memory Lua used; multiple states can coexist without communication.
- Exceptions can be raised in Lua and caught in C, a consequence of its library design.
- Deliberately minimalist: it ships almost no libraries, expecting the host program to provide the useful functions (e.g., game-engine commands); this keeps resource use very low.
- Among dynamic languages it emphasizes performance: features are omitted when they can't be implemented efficiently, and the small virtual machine fits in cache.
- In 2023 it was the second-highest-growth language by GitHub contributors, and it is used in games such as World of Warcraft and Roblox.
- The official interpreter is written in C: Lua bytecode runs on a loop-with-switch virtual machine, so portability is inherited from C.
- Interop with C uses function pointers: C registers a function pointer under a name in a Lua state, and Lua's interpreter calls the pointer; a Lua function is just bytecode data C can ask the interpreter to run.
- A fresh Lua state has no functions at all; standard libraries must be registered explicitly, which is what makes Lua usable as a sandbox.
- Booleans were added late, mainly for `false`: in tables, `nil` is indistinguishable from an absent key, so a separate false value was needed.
- Uses one-based indexing, matching real-world and mathematical convention rather than C's pointer-arithmetic-derived zero-based convention.
- Whole-program type inference does not work for Lua, but real performance gains come from an informal type discipline — e.g., not reusing one variable for both integers and strings — even though the language never enforces it.

## Related

- [[Roberto Ierusalimschy]] — creator
- [[LuaJIT]] — the independent JIT compiler for Lua
- [[Mike Pall]] — LuaJIT's author
- [[summary-20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy]] — source summary
- [[C (Programming Language)]] — typical host language
- [[C++]] — typical host language
- [[Python]] — the language most compared against
- [[Scripting Languages]] — the category Lua exemplifies
- [[Dynamic Languages]] — the broader category
- [[Embedding and Extending]] — the architecture it serves
- [[Language as a Library]] — its defining design
- [[Sandboxing]] — a consequence of its state model
- [[Just-in-Time Compilation]] — what LuaJIT adds
- [[Trace Compilation]] — LuaJIT's technique
- [[Zero-Based Indexing]] — the indexing convention it rejects
- [[Foreign Function Interface]] — its C interop mechanism
- [[Programming Language Design]] — the craft behind it
- [[summary-20260902 - Creator of Lua： You Can Interpret C And Compile Python ｜ Roberto Ierusalimschy]] — source summary
