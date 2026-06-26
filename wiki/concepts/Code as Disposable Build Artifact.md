---
title: "Code as Disposable Build Artifact"
type: concept
tags: [ai, agentic-engineering, code-generation, paradigm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI.md"]
last_updated: 2026-06-26
---

## Definition
"Code as disposable build artifact" is the paradigm that source code is a compiled output of a well-defined specification, not the primary artifact of software engineering. The LLM acts as a fuzzy compiler, and the spec, guardrails, and acceptance criteria are the source of truth.

## Key Information
- Referenced by Ryan Lopopolo in connection with Symphony, OpenAI's agent orchestrator
- Code is treated as a compiled artifact of a super well-defined spec
- The LLM acts as a "fuzzy compiler" — context and guardrails in the codebase are like constraints and optimization passes
- Swapping models is analogous to changing code generation backends (e.g., LLVM to Cranelift in Rust)
- Different models may produce different code (different "machine code"), but the spec and guardrails ensure acceptable output regardless
- Inverts the traditional relationship: the spec is primary, the code is derivative and disposable

## Related
- [[summary-20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI]] — source
- [[LLM as Fuzzy Compiler]] — the underlying mental model
- [[Symphony]] — OpenAI's agent orchestrator embodying this paradigm
- [[Code is Free]] — enabling premise
- [[SpecificationDrivenDevelopment]] — related approach
