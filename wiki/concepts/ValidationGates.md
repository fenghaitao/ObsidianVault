---
title: "ValidationGates"
type: concept
tags: [concept, validation, testing, prp, ai-coding, claude-code]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20250717 - Context Engineering 101 - The Simple Strategy to 100x AI Coding.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250724 - Build ANY AI Agent with this Context Engineering Blueprint.md"
last_updated: 2026-06-19
---

## Definition

Validation gates are explicit, automated checks the AI is required to run and pass before declaring its work complete. In the context of [[Rasmus]]'s [[PRPFramework]], they're a section of every PRP listing the linting commands, unit tests, and integration checks the AI must execute and iterate against before reporting back. They turn AI-generated code review from a *post hoc* activity into an *inner loop* the AI is responsible for closing.

## Key Information

### What goes in a validation gate

| Layer | Examples | When |
|---|---|---|
| **Lint / format** | `ruff check`, `black`, `eslint` | Run after each file write |
| **Type check** | `mypy`, `pyright`, `tsc` | Per file or per build |
| **Unit tests** | `pytest`, `npm test` | After feature complete |
| **Integration tests** | end-to-end against a sandbox or real service | After unit tests pass |
| **Build** | `npm run build`, `cargo build` | Before declaring done |
| **Custom domain checks** | Schema validation, smoke tests | Per project |

### The pattern in PRP execution

```
1. AI implements task N
2. AI runs validation gate (e.g., `pytest tests/test_feature.py -v`)
3. If failures → AI reads the failure, fixes, re-runs
4. Loop until gate passes
5. Move to task N+1
```

This is what Cole means by "context-engineered code is not vibe coding." The AI isn't just writing what looks plausible — it's writing what *passes specified checks.*

### Why they matter

- **The AI catches its own mistakes** before the human has to. Human-side review is shallower (skim the code) when the AI has already shown the tests pass.
- **Faster iteration.** A failing test prompts the AI to fix immediately, rather than the human running tests later and re-prompting.
- **Reduces hallucinated success.** Without gates, an AI can confidently say "done!" while leaving subtle bugs. Gates prevent that.
- **Deterministic correctness floor.** Anything covered by a passing test is at minimum doing what the test specifies. Gates give the AI a self-checkable target.

### Common pitfalls

- **Over-spec'd gates.** [[ColeMedin]] notes generated PRPs sometimes produce gates that are unrealistic ("run security audit", "validate against production traffic") — a manual edit before execution removes them. Gates should be runnable in the AI's environment.
- **Gates that mask poor coverage.** A handful of trivial unit tests will pass. Gates only validate what they cover. Pair them with human-side review to catch architectural / design issues.
- **Gates as a performative ritual.** If the AI writes both the implementation and the test, the test can be tautological. Cole's mitigation: write tests *first* (in the PRP plan), have the AI implement to satisfy them, and review the tests yourself for meaningful coverage.

### Relationship to [[AgentEvaluation]]

ValidationGates are *code-correctness* checks (does the function do what its tests say it does?). [[AgentEvaluation]] is *behavior-correctness* measurement (does the agent respond well across many scenarios). Both matter, both fit different layers:
- ValidationGates: per-build, runnable, deterministic.
- AgentEvaluation: continuous, often sampled, judgmental.

## Related

- [[PRPFramework]] — where validation gates live
- [[ContextEngineering]] — broader paradigm
- [[ClaudeCode]] — primary execution surface
- [[AgentEvaluation]] — adjacent but distinct
- [[Guardrails]] — runtime validation of agent inputs/outputs (similar spirit, different layer)
- [[Rasmus]] — articulated the pattern
- [[ColeMedin]] — popularized the pattern through his content
- [[summary-context-engineering-101]] — primary source
- [[summary-context-engineering-blueprint-for-ai-agents]] — PydanticAI use case
