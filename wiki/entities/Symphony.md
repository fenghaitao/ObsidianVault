---
title: "Symphony"
type: entity
tags: [tool, openai, agent-orchestration, code-generation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - State of the Claw — Peter Steinberger.md"]
last_updated: 2026-06-26
---

## Definition
Symphony is an agent orchestrator released by OpenAI that treats code as a disposable build artifact — a compiled output of a well-defined specification, with the LLM acting as a fuzzy compiler.

## Key Information
- Released by OpenAI as an agent orchestrator
- Embodies the idea that code is a compiled artifact of a well-defined spec
- Uses the mental model of LLM as fuzzy compiler — context and guardrails are like constraints and optimization passes
- Swapping models is analogous to changing code generation backends (e.g., LLVM to Cranelift in the Rust compiler)
- Referenced by Ryan Lopopolo in his Harness Engineering talk
- Peter Steinberger cited Symphony as evidence that OpenAI is "really leaning in and understanding open source now" — "they released Symphony which is a really cool orchestration layer"

## Related
- [[summary-20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI]] — source
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — source (cited as open source evidence)
- [[OpenAI]] — creator
- [[LLM as Fuzzy Compiler]] — underlying mental model
- [[Code as Disposable Build Artifact]] — paradigm it embodies
- [[RyanLopopolo]] — referenced it
- [[PeterSteinberger]] — cited it as evidence of OpenAI's open source direction
