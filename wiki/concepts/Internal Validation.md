---
title: "Internal Validation"
type: concept
tags: [CI-CD, agents, testing, build, validation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner.md"]
last_updated: 2026-06-30
---

## Definition
Internal Validation is the build and test phase that runs on every iteration within the agent development harness, replacing the separate CI build/test phase. It validates that code compiles from a well-known source, passes tests, and introduces no regressions — continuously rather than as a delayed batch process.

## Key Information
- Part of the [[Continuous Compute]] paradigm proposed by [[HugoSantos]]
- Moves build and test from a separate CI phase into the agent harness inner loop
- Every iteration of the agent loop includes internal validation
- Speed is critical: cannot spend 15-45 minutes running tests without delaying the entire loop
- Enforces invariants: code must compile from a well-known checkout, no regressions, changes are allowed
- Requires stateful environments with warm caches to be fast enough
- Contrasts with traditional CI where tests run only on PR submission, creating delayed feedback

## Related
- [[summary-20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner]] — source
- [[Continuous Compute]] — paradigm it belongs to
- [[External Validation]] — complementary validation by specialized review agents
- [[AgentHarness]] — the loop where internal validation runs
- [[Stateful Development Environment]] — prerequisite for fast internal validation
- [[Verification in Agentic Loops]] — related concept of continuous verification
