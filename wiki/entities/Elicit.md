---
title: "Elicit"
type: entity
tags: [ai-research, scientific-research, dsl, agent-architecture, company]
sources: []
last_updated: 2026-07-07
---

## Definition

Elicit is an AI research company that builds tools for scientific research, known for developing Ash PL, a custom domain-specific language (DSL) for making agentic workflows trustworthy and verifiable. The company presented its approach at Code with Claude 2026 London.

## Key Information

- Presented Ash PL at [[CodeWithClaude|Code with Claude 2026]] London Day 2, a custom DSL for scientific research agents.
- Ash PL is a Turing-incomplete, purely functional, typed subset of Python with domain-specific primitives for academic research (retrieving papers, clinical trials).
- The core engine alternates between writing Ash PL programs and interpreting them, with content-addressable caching enabling full re-interpretation on every iteration without performance loss.
- Core philosophy: mechanism matters as much as output — two systems producing identical results are trusted differently based on their internal process.
- Architecture is event-sourced with an append-only event log, a Python service as message broker, a sandbox for the curator (model-agnostic wrapper allowing harness swaps), and a gateway for credential isolation.
- Ash PL code is viewable for each artifact, with a graphical DAG representation derived from it for user-friendly process verification.
- The [[ClaudeCode]] agent tool is used in the curator harness, with [[ClaudeManagedAgents]] discussed as an alternative harness approach.

## Related

- [[summary-making-agentic-workflows-trustworthy-dsl]] — source talk about Elicit's Ash PL DSL
- [[ClaudeCode]] — agent tool used in Elicit's curator harness
- [[ClaudeManagedAgents]] — alternative harness approach discussed in the talk
- [[AgenticMemory]] — caching and memorization pattern parallels
- [[Anthropic]] — hosted the Code with Claude conference where Elicit presented
- [[summary-07 - Making agentic workflows trustworthy and verifiable with a custom DSL]] — source summary
