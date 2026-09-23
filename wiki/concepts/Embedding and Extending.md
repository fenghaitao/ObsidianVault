---
title: "Embedding and Extending"
type: concept
tags: [concept, programming-languages, scripting]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy.md"]
last_updated: 2026-09-23
---

## Definition

Embedding and extending are the two directions of a dual-language scripting architecture: embedding puts the host program in control and calls the script, while extending lets the script call functions provided by host-language libraries.

## Key Information

- The distinction hinges on "who has the main loop": a C program calling Lua is embedding; a Lua program calling C libraries is extending.
- Roberto Ierusalimschy: several called scripting languages are really only convenient for extending, where the script is the main program and C supplies libraries; Lua is strong at both.
- Lua is good at embedding because it was thought of and written as a library from the beginning.
- Embedding is crucial for games: the host loop keeps the frame rhythm, and at each frame calls Lua to update characters and images before returning to C for rendering.
- The same mechanics (C function pointers registered in a Lua state, and Lua functions as bytecode the interpreter runs) support calls in both directions, nesting recursively across the boundary.

## Related

- [[Lua]] — strong at both directions
- [[Scripting Languages]] — the architecture these terms describe
- [[Language as a Library]] — why Lua embeds so well
- [[C (Programming Language)]] — the usual host
- [[Foreign Function Interface]] — the interop mechanism
- [[Roberto Ierusalimschy]] — who explains the distinction
- [[summary-20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy]] — source summary
