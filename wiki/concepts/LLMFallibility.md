---
title: "LLMFallibility"
type: concept
tags: [llm, reliability, non-determinism, agentic-coding, safety]
sources:
  - "raw/03-transcripts/aiDotEngineer/Channel Only/20260527 - Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry.md"
last_updated: 2026-06-30
---

## Definition
LLM fallibility is the inherent tendency of large language models to make mistakes due to their non-deterministic, probabilistic nature. Unlike deterministic software, LLMs predict tokens from probability distributions, meaning errors are inevitable and will never be fully eliminated. This makes deterministic guardrails essential when using LLMs for code generation.

## Key Information
- LLMs are non-deterministic by design; they predict the next most likely token, not the correct token
- This non-determinism means LLMs will always be fallible, even as models improve
- Errors can manifest as subtle bugs in code that looks sensible on the surface (good variable names, comments, structure)
- Just as the smartest humans make mistakes and need guardrails, LLM-generated code needs deterministic safety nets
- Common mitigation strategies (tests, code review agents) share the same fallibility problem: they are also LLM-generated or human-generated and can contain errors
- Tests can only prove incorrectness when they fail, not correctness for all inputs
- The failure modes of LLMs may be unexpected to humans because LLMs "think" differently (see [[AlienIntelligence]])
- Szoke's argument: the best defense is a deterministic system (compiler) that provides absolute guarantees, not probabilistic checks

## Related
- [[summary-20260527 - Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry]] — source
- [[AlienIntelligence]] — explains why LLM failure modes are unpredictable
- [[CompilerGuardrails]] — the deterministic defense against LLM fallibility
- [[MurphysLawAICoding]] — the inevitability of failures without guardrails
- [[DeterministicGuardrails]] — broader concept of rule-based validation
- [[AIGenerated Tests]] — tests share the same fallibility problem
- [[VibeCoding]] — the practice where LLM fallibility is most relevant
