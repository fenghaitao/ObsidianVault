---
title: "Scripting Languages"
type: concept
tags: [concept, programming-languages, scripting]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy.md"]
last_updated: 2026-09-23
---

## Definition

A scripting language is a language designed to coordinate or be embedded in a host program, forming a dual-language architecture in which a host (often C) runs the main loop and the script handles dynamic parts.

## Key Information

- Roberto Ierusalimschy: the defining idea of scripting is a dual-language architecture — the original scripting languages were Unix shells, which are only useful because they coordinate many C programs.
- "Scripting" literally means giving a script to be executed by other programs, with the script as coordinator.
- There are two typical uses distinguished by "who has the main loop": the program written in C calling the script, or the program written in the script calling C libraries.
- Many so-called scripting languages are easiest to use when the script is the main program (extension); Lua is exceptional at both embedding and extending.
- In games, the host C loop keeps the frame rhythm and calls the script each frame to update game state before returning to C for rendering.
- Scripting is not the same as "dynamic": scripting is about coordination, while dynamism is about runtime code creation.

## Related

- [[Lua]] — the scripting language par excellence
- [[Dynamic Languages]] — the distinct, broader category
- [[Embedding and Extending]] — the two directions of the architecture
- [[Language as a Library]] — what makes Lua script-friendly
- [[Roberto Ierusalimschy]] — who articulates the distinction
- [[C (Programming Language)]] — the typical host
- [[Python]] — a common scripting-adjacent contrast
- [[summary-20260803 - Creator of Lua： What People Get Wrong About Scripting Languages ｜ Roberto Ierusalimschy]] — source summary
- [[Programming Language Design]] — the craft involved
