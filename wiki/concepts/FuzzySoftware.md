---
title: "FuzzySoftware"
type: concept
tags: [software-engineering, determinism, ai-agents, llm, nondeterministic, paradigm-shift]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240808 - Using agents to build an agent company： Joao Moura.md"]
last_updated: 2026-06-26
---

## Definition
Fuzzy Software describes the paradigm shift from traditional deterministic software (known inputs, predictable outputs, testable behavior) to AI-powered software where inputs can be arbitrary (CSV, JSON, jokes), models are black boxes, and outputs are non-deterministic. This fundamentally changes how software is built, tested, and deployed.

## Key Information
- **Strongly-typed software (traditional)**: Known inputs (form fields, integers, strings), deterministic processing, predictable and testable outputs. Behavior is always the same, enabling comprehensive test coverage.
- **Fuzzy software (AI-powered)**: Input is a string but could be CSV, JSON, or a random joke. LLMs are black boxes. Output is non-deterministic — the same input may produce different results.
- This shift means traditional testing strategies (assert expected output for given input) no longer suffice. Eval-based testing, human-in-the-loop verification, and guardrails become necessary.
- Joao Moura described this as "everything is fuzzy" — you don't know what's coming in and you don't necessarily know what's coming out.
- The fuzziness is a feature, not a bug: it enables agents to adapt to circumstances in real time, handling situations that would break deterministic automations.
- Traditional automations require connecting every dot (A→B→C→D), becoming brittle as complexity grows. Fuzzy agents can navigate unanticipated paths.

## Related
- [[summary-20240808 - Using agents to build an agent company： Joao Moura]] — source
- [[AgentCompanyPattern]] — business pattern built on fuzzy software
- [[DeterministicWorkflows]] — the older paradigm
- [[DeterministicGuardrails]] — approach to constraining fuzzy behavior
- [[HumanInTheLoopWorkflows]] — verification strategy for fuzzy outputs
- [[EvalFlywheel]] — evaluation approach for non-deterministic systems
