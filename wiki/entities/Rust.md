---
title: "Rust"
type: entity
tags: [language, systems-programming, Mozilla, memory-safety]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20251010 - Mozilla Firefox CTO： Chrome vs Firefox and Distinguished Eng Promos.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260724 - Why C Is a Dangerous Language ｜ Simon Peyton Jones.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg.md"]
last_updated: 2026-09-23
---

## Definition

Rust is a systems programming language created at Mozilla to provide compile-time guarantees against memory-safety bugs and data races, developed with the Servo browser engine as its testbed.

## Key Information

- Motivated by two C++-rooted problems in Firefox: memory-safety vulnerabilities (a web page can take over the computer) and the difficulty of safely adding multithreading as core counts grew
- Co-evolved with Servo, Mozilla's attempt to build a memory-safe and parallel browser engine to leapfrog Chrome
- The parallel Rust CSS engine was uplifted into Firefox as Quantum CSS, improving Amazon.com rendering time by ~25% and becoming the industry's fastest CSS engine
- The full-engine rewrite (Servo) proved unsustainable against hundreds of Chromium engineers, but Rust escaped the browser and became a widely adopted industry language
- James Cowling: Dropbox rewrote its Magic Pocket storage nodes in Rust (before Rust hit GA) to eliminate Go's unpredictable garbage-collected memory usage, which caused OOM restarts that looked like disk failures and could trigger congestion collapse.
- The Rust rewrite coincided with removing the filesystem layer entirely and directly driving the disks via ZBC (zone-based block control), part of the Discotech project.

### Charlie Marsh on Rust
- Chose Rust for Ruff partly for hype, but now calls it "an extremely good bet": cargo makes clone→build→test trivial, the toolchain is opinionated (no C++ build-system pain), and it delivers memory safety plus performance that "scaled very well."
- Would not start a net-new project in C or C++, while finding Zig and Go interesting alternatives; notes OpenAI also bets heavily on Rust.
- Much of Ruff's speed came from Rust, but even more comes from thinking deeply about performance and design (e.g., uv's cache layout and Andrew Gallant's u64 version representation).

### Simon Peyton Jones on Rust
- SPJ calls Rust "much, much better" than C: rewriting software infrastructure in Rust would put us in a "way better situation."
- He is unsure whether Rust's array-bounds checks are on by default, but compiling with them enabled removes by construction the buffer overruns behind most exploits.

### Xavier Leroy on Rust
- The big Rust-vs-OCaml divide is manual memory management versus garbage collection: Rust is "the finest language... for manual memory management" via the borrowing/ownership discipline, "infinitely safer than C or C++."
- Rust fuses C/C++-style low-level programming with high-level functional facilities (algebraic data types, pattern matching) — "a very interesting design" Leroy wishes could have come out of academia.
- Manual memory management is not always faster: defensive object copying and Rust's constrained sharing (forcing "unsharing") can cost more time and memory than GC in some applications.
- Leroy notes C-to-Rust AI translations today can end up "entirely in unsafe blocks" — a line-by-line C port usable only as a starting point.

### Leonardo de Moura on Rust
- A Lean tool maps Rust into Lean (shallow embedding) so the Lean translation can be verified — an example of verifying programs written in a different language.

### Anders Hejlsberg on Rust vs Go

- For the TypeScript compiler port, Rust was rejected because it has no garbage collection and its borrow checker does not allow circular data structures (trees with parent pointers, recursive types, symbols referencing each other) — which the compiler is "chalk full" of.
- Ref counting and other Rust strategies come with restrictions and lack the safety guarantees of language-integrated GC; garbage collection "engineered into the language" is a separate concern you don't have to do anything special for.
- Hejlsberg says Rust is "no better" than Go on the quality of generated code or the concurrency gains, so Go delivered the same benefits for less work.
- Choosing Rust would have forced a rewrite and "a whole bunch of new problems" rather than just porting — "we tried, and it just wasn't feasible"; the goal was doing the least work to reach the payout.

### Martin Odersky on Rust
- Rust is "closer to the metal" with better performance guarantees and a much smaller memory footprint; Scala's garbage collection always imposes small pauses and needs a big chunk of memory, so Rust is better for embedded.
- Odersky believes "right now Rust is actually overused": people push Rust higher up the stack where a garbage collector is fine, turning it into an intellectual exercise — "if you have the memory for a garbage collector, you should absolutely use one."
- He credits Rust as the big achievement that proved a low-level systems language can be memory safe — "nobody thought that was possible before Rust came."

## Related

- [[Mozilla]] — its creator
- [[Servo]] — the engine testbed it enabled
- [[Firefox]] — where Quantum CSS landed
- [[summary-20251010 - Mozilla Firefox CTO： Chrome vs Firefox and Distinguished Eng Promos]] — source summary
- [[Magic Pocket]] — Dropbox system whose storage nodes were rewritten in Rust
- [[Discotech]] — the disk project that coincided with the Rust rewrite
- [[Go (Programming Language)]] — the language Rust replaced on storage nodes
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[Charlie Marsh]] — chose Rust for Ruff and uv
- [[Astral]] — the company building in Rust
- [[Ruff]] — Python linter in Rust
- [[uv]] — Python package manager in Rust
- [[Zig]] — language compared with Rust
- [[Salsa (Framework)]] — Rust incremental-computation framework
- [[Bun]] — runtime being rewritten to Rust
- [[Andrew Gallant]] — Astral engineer writing Rust
- [[ripgrep]] — Rust search tool
- [[Rust Analyzer]] — Rust language server
- [[summary-20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh]] — source summary
- [[summary-20260608 - Co-Creator of Haskell： Functional Programming, Thinking in Types, Useless Languages ｜ Simon Jones]] — source summary
- [[summary-20260724 - Why C Is a Dangerous Language ｜ Simon Peyton Jones]] — source summary
- [[Buffer Overflow]] — the bug class Rust's bounds checks prevent
- [[Xavier Leroy]] — calls Rust the finest manual-memory-management language
- [[Manual Memory Management]] — Rust's model vs garbage collection
- [[OCaml]] — the garbage-collected contrast
- [[summary-20260720 - Creator of OCaml： Functional Programming, Formal Verification, Programming Languages ｜ Xavier Leroy]] — source summary
- [[summary-20260729 - AWS to Dropbox： The Largest Ever Data Migration In History ｜ James Cowling]] — source summary
- [[Lean]] — a tool maps Rust into Lean for verification
- [[Formal Verification]] — the use case
- [[summary-20260810 - Creator of Lean： Handwritten Math Will Change Dramatically ｜ Leonardo de Moura]] — source summary
- [[TypeScript]] — the compiler whose port rejected Rust
- [[Anders Hejlsberg]] — the decision-maker
- [[Go (Programming Language)]] — the language chosen instead
- [[summary-20260817 - Creator of TypeScript： 10x Faster TypeScript, Why AI Won't Replace SWEs ｜ Anders Hejlsberg]] — source summary
- [[Martin Odersky]] — calls Rust bottom-of-stack, overused higher up
- [[Garbage Collection]] — the simpler alternative above embedded
- [[summary-20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky]] — source summary
- [[summary-20260911 - Creator of TypeScript： Why We Chose Go For Our Rewrite ｜ Anders Hejlsberg]] — source summary
