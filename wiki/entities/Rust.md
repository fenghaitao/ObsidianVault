---
title: "Rust"
type: entity
tags: [language, systems-programming, Mozilla, memory-safety]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20251010 - Mozilla Firefox CTO： Chrome vs Firefox and Distinguished Eng Promos.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md"]
last_updated: 2026-09-14
---

## Definition

Rust is a systems programming language created at Mozilla to provide compile-time guarantees against memory-safety bugs and data races, developed with the Servo browser engine as its testbed.

## Key Information

- Motivated by two C++-rooted problems in Firefox: memory-safety vulnerabilities (a web page can take over the computer) and the difficulty of safely adding multithreading as core counts grew
- Co-evolved with Servo, Mozilla's attempt to build a memory-safe and parallel browser engine to leapfrog Chrome
- The parallel Rust CSS engine was uplifted into Firefox as Quantum CSS, improving Amazon.com rendering time by ~25% and becoming the industry's fastest CSS engine
- The full-engine rewrite (Servo) proved unsustainable against hundreds of Chromium engineers, but Rust escaped the browser and became a widely adopted industry language
- James Cowling: Dropbox rewrote its Magic Pocket storage nodes in Rust (before Rust hit GA) to eliminate Go's unpredictable garbage-collected memory usage, which caused OOM restarts that looked like disk failures and could trigger congestion collapse.

## Related

- [[Mozilla]] — its creator
- [[Servo]] — the engine testbed it enabled
- [[Firefox]] — where Quantum CSS landed
- [[summary-20251010 - Mozilla Firefox CTO： Chrome vs Firefox and Distinguished Eng Promos]] — source summary
- [[Magic Pocket]] — Dropbox system whose storage nodes were rewritten in Rust
- [[Discotech]] — the disk project that coincided with the Rust rewrite
- [[Go (Programming Language)]] — the language Rust replaced on storage nodes
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
