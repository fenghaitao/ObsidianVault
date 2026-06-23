---
title: "Making Agentic Workflows Trustworthy with a Custom DSL"
type: source
tags: [DSL, trust, verification, agent-architecture, elicit]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London Day 2/07 - Making agentic workflows trustworthy and verifiable with a custom DSL.md]
last_updated: 2026-06-23
---

## Core Summary

James Brady from Elicit presents their approach to making agentic workflows trustworthy using Ash PL, a custom domain-specific language (DSL) for scientific research agents. The DSL is a Turing-incomplete, purely functional, typed subset of Python with domain-specific primitives for academic research. The core engine alternates between writing Ash PL programs and interpreting them, with content-addressable caching enabling full re-interpretation on every iteration without performance loss. The talk argues that mechanism matters as much as output — two systems producing identical results are trusted differently based on their internal process.

## Key Points

- **Mechanism matters:** Two systems producing identical output are trusted differently based on how they arrived at that output. Elicit's value proposition is the rigorous, transparent process, not just the final table.
- **Three desiderata for the DSL:** (1) Process must be legible to users and other agents, (2) Iteration must retain fidelity without drift, (3) Process must be followed faithfully — the plan is literally executable.
- **Ash PL design:** Turing-incomplete (no loops, no recursion, no mutation), purely functional, typed, opinionated subset of Python with added domain primitives (retrieve academic papers, clinical trials).
- **Write-interpret-redraft loop:** Curator writes Ash PL → Python service parses, type-checks, interprets → results feed back → curator redrafts/extended Ash PL. The whole program is reinterpreted from scratch each iteration.
- **Content-addressable caching:** Pure functional language enables hashing expressions; if an expression was evaluated before, the cached result is used. This makes full reinterpretation fast despite growing programs (100 lines → 1,000+ lines).
- **Architecture:** Event-sourced with append-only event log, Python service as message broker, sandbox for curator (model-agnostic wrapper allows swapping harnesses), gateway for credential isolation.
- **User-facing transparency:** Ash PL code is viewable for each artifact; a graphical DAG representation derived from the Ash PL is more ergonomic for users to verify the process.
- **When to use a DSL:** When your product's desiderata (legibility, fidelity, faithfulness) point toward it. Base it on an existing language with training data presence. Most work is conventional software engineering around the DSL, not the DSL itself.

## Related

- [[ClaudeCode]] — agent tool used in the curator harness
- [[ClaudeManagedAgents]] — alternative harness approach
- [[AgenticMemory]] — caching/memorization pattern parallels
- [[Elicit]] — the company behind Ash PL
