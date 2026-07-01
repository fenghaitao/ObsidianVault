---
title: "Non-functional Requirements Specification"
type: concept
tags: [ai, agentic-engineering, code-quality, methodology]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI.md"]
last_updated: 2026-06-26
---

## Definition
Non-functional Requirements Specification is the practice of explicitly writing down the ~500 little decisions around underspecified non-functional requirements (NFRs) that go into producing good code, so that coding agents can see and follow them. It transforms tacit engineering knowledge into durable, agent-readable instructions.

## Key Information
- Articulated by Ryan Lopopolo (OpenAI): doing a single patch well requires ~500 little decisions around underspecified NFRs
- Models have seen trillions of lines of code making every possible choice — the engineer's job is to specify which choices are acceptable
- NFRs include: error handling patterns, retry/timeout conventions, component decomposition rules, package privacy, dependency edges, async helper usage, schema deduplication
- Written down as documentation, ADRs, lint rules, test assertions, and reviewer agent prompts
- When one engineer documents an NFR, every agent trajectory benefits from it — leverage stacks
- Example: "parse don't validate at the edge" — an NFR that eliminates `unknown` types deep in the codebase
- Implementation: custom ESLint rules, source code structure tests, reviewer agent prompts, agents.md files

## Related
- [[summary-20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI]] — source
- [[Harness Engineering]] — the broader discipline
- [[PersonaOriented Documentation]] — how NFRs are organized by engineering perspective
- [[Reviewer Agents]] — enforce NFRs in CI
- [[Garbage Collection Day]] — when new NFRs are identified and encoded
- [[SpecificationDrivenDevelopment]] — related approach
