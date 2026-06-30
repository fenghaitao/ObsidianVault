---
title: "External Validation"
type: concept
tags: [CI-CD, agents, code-review, validation, security]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner.md"]
last_updated: 2026-06-30
---

## Definition
External Validation is the evaluation of agent-generated code changes by specialized review agents (security-focused LLMs, API conformance LLMs, etc.) within the development loop, replacing human code reviewers. These agents provide continuous feedback that the main agent harness incorporates back into the code.

## Key Information
- Part of the [[Continuous Compute]] paradigm proposed by [[HugoSantos]]
- Replaces human code reviewers with specialized AI review agents
- Examples: security-focused LLMs, API conformance LLMs, compliance-focused agents
- Operates within the agent harness loop, providing fast feedback
- Moves from delayed human review (hours/days) to near-instant agent review
- Enables the removal of PRs as the unit of work
- Human role shifts from reviewing code to approving intent and results at the [[Pre-merge Queue]]
- Must be fast to avoid delaying the agent loop
- Complements [[Internal Validation]] (build/test) within the same loop

## Related
- [[summary-20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner]] — source
- [[Continuous Compute]] — paradigm it belongs to
- [[Internal Validation]] — complementary build/test validation
- [[Reviewer Agents]] — the specialized agents performing external validation
- [[AgentHarness]] — the loop where external validation runs
- [[AgentIdentity]] — identity for agents performing validation
- [[Pre-merge Queue]] — where human approval happens after validation
