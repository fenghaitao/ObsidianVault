---
title: "Zig"
type: entity
tags: [language, systems-programming, compiler]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260919 - Creator of Scala： Rust, Zig, Python vs Scala ｜ Martin Odersky.md"]
last_updated: 2026-09-23
---
## Definition
Zig is a systems programming language Charlie Marsh cites as an interesting alternative to Rust. The transcript garbles it as "Zigg".

## Key Information
- Charlie: "what's happening in Zig is very interesting"; he wishes he had time to go deeper and believes Rust has things to learn from Zig's ecosystem.
- Zig's creator, Andrew Kelley, gave a data-oriented design talk that Charlie found highly influential, changing how he sees software, memory, and allocation.
- Zig has a much stricter LLM policy than Astral — no LLM-written or LLM-assisted code at all in the project.
- Bun, originally written in Zig, is the subject of the episode's discussion of an agent-driven rewrite to Rust.
- Odersky: Zig has "a really nifty compile-time inlining construct" where the compiler does smart inlining — clean and powerful — whereas Rust's macros are more clunky.
- Scala has something close to Zig's inlining, but with a restriction Odersky believes Zig lacks: no additional type errors may appear after inlining (the failure mode of C++ templates).
- Odersky's contrast: Zig's comptime inlining is "much better" than C++ templates, which can expand into very complex, hard-to-debug type errors.
- Odersky suspects Zig (like most low-level systems languages) is not memory safe, unlike Rust.

## Related
- [[Andrew Kelley]] — Zig's creator
- [[Bun]] — the runtime originally written in Zig
- [[Rust]] — the language it is compared with
- [[Go (Programming Language)]] — another alternative Charlie mentions
- [[Data-Oriented Design]] — the theme of Kelley's talk
- [[Contributor Poker]] — Zig's term for betting on contributors
- [[summary-20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh]] — source summary
- [[Martin Odersky]] — on Zig's comptime inlining
- [[Inlining]] — the comptime construct
- [[Scala]] — has a similar, more-constrained inline
- [[Rust]] — the clunkier-macro comparison
- [[summary-20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky]] — source summary
- [[summary-20260919 - Creator of Scala： Rust, Zig, Python vs Scala ｜ Martin Odersky]] — source summary
