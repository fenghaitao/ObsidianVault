---
title: "Rust"
type: entity
tags: [language, systems-programming, safety, compiler, memory-safety]
sources:
  - "raw/03-transcripts/aiDotEngineer/Channel Only/20251227 - AGI： The Path Forward – Jason Warner & Eiso Kant, Poolside.md"
  - "raw/03-transcripts/aiDotEngineer/Channel Only/20260527 - Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry.md"
last_updated: 2026-06-30
---

## Definition
Rust is a compiled systems programming language designed with safety and performance in mind. It aims to be as fast as C and C++ while providing compile-time guarantees for memory safety, type safety, and concurrency safety. Daniel Szoke argues that Rust's strict compiler makes it the ideal language for vibe coding because it serves as a deterministic guardrail that catches LLM-generated errors before they reach production.

## Key Information
- **Compiled language** focused on safety and performance
- **Strict compiler** enforces type safety, memory safety, concurrency safety, null safety, and more
- **If it compiles, it's likely correct**: the compiler catches entire classes of bugs at compile time
- **Detailed compiler errors** provide context on what went wrong and how to fix it, making it well-suited for AI agent compile-fix loops
- **Fearless concurrency**: the compiler checks that multi-threaded data sharing is thread-safe; data races become compile errors
- **No null**: uses `Option` type instead of universal null, forcing explicit handling of absent values
- **No `any` escape hatch**: type safety cannot be bypassed with unchecked casts
- **Poolside Demo**: Malibu Agent converted an ADA codebase to Rust with self-testing and iterative feature addition (1,152 lines of Rust code)
- **Szoke's argument**: Rust is harder for LLMs to get right on the first try, but AI agents in compile-fix loops can autonomously fix errors, and each fix prevents a potential production bug
- **Trade-off**: harder first-try generation vs. deterministic safety net — the compiler is faster and more thorough than AI code review

## Related
- [[summary-20251227 - AGI： The Path Forward – Jason Warner & Eiso Kant, Poolside]] — source (Poolside demo)
- [[summary-20260527 - Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry]] — source (vibe coding argument)
- [[DanielSzoke]] — Rust SDK maintainer at Sentry, advocate for Rust in vibe coding
- [[Poolside]] — company that demoed ADA-to-Rust conversion
- [[MalibuAgent]] — Poolside's coding agent
- [[ADA]] — language converted to Rust in Poolside demo
- [[CompilerGuardrails]] — key concept: compiler as deterministic safety net
- [[FearlessConcurrency]] — Rust's compile-time concurrency guarantee
- [[VibeCoding]] — the practice Rust is argued to be ideal for
- [[TypeSafety]] — related concept
- [[MemorySafety]] — related concept
