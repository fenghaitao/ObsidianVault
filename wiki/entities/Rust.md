---
title: "Rust"
type: entity
tags: [language, systems-programming, Mozilla, memory-safety]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20251010 - Mozilla Firefox CTO： Chrome vs Firefox and Distinguished Eng Promos.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh.md"]
last_updated: 2026-09-22
---

## Definition

Rust is a systems programming language created at Mozilla to provide compile-time guarantees against memory-safety bugs and data races, developed with the Servo browser engine as its testbed.

## Key Information

- Motivated by two C++-rooted problems in Firefox: memory-safety vulnerabilities (a web page can take over the computer) and the difficulty of safely adding multithreading as core counts grew
- Co-evolved with Servo, Mozilla's attempt to build a memory-safe and parallel browser engine to leapfrog Chrome
- The parallel Rust CSS engine was uplifted into Firefox as Quantum CSS, improving Amazon.com rendering time by ~25% and becoming the industry's fastest CSS engine
- The full-engine rewrite (Servo) proved unsustainable against hundreds of Chromium engineers, but Rust escaped the browser and became a widely adopted industry language
- James Cowling: Dropbox rewrote its Magic Pocket storage nodes in Rust (before Rust hit GA) to eliminate Go's unpredictable garbage-collected memory usage, which caused OOM restarts that looked like disk failures and could trigger congestion collapse.

### Charlie Marsh on Rust
- Chose Rust for Ruff partly for hype, but now calls it "an extremely good bet": cargo makes clone→build→test trivial, the toolchain is opinionated (no C++ build-system pain), and it delivers memory safety plus performance that "scaled very well."
- Would not start a net-new project in C or C++, while finding Zig and Go interesting alternatives; notes OpenAI also bets heavily on Rust.
- Much of Ruff's speed came from Rust, but even more comes from thinking deeply about performance and design (e.g., uv's cache layout and Andrew Gallant's u64 version representation).

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
