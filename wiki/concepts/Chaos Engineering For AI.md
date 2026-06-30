---
title: "Chaos Engineering For AI"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests — Vincent Koc, OpenClaw.md"]
last_updated: 2026-06-30
---

## Definition

Chaos engineering for AI applies the traditional software chaos engineering principle — deliberately breaking systems to discover their limits — to AI agent evaluation. While traditional software engineering has evolved through unit tests, regression suites, CI/CD, and chaos engineering, AI evaluation has largely stopped at static benchmarks and handcrafted tests, missing the deliberate stress-testing that reveals where systems actually fail.

## Key Information

- **Gap in AI evaluation**: Software engineering uses chaos engineering to discover system boundaries through random experimentation and deliberate breaking. AI evaluation has no equivalent — no systematic approach to finding where agents break under unexpected conditions
- **Analogy to traditional chaos engineering**: Just as Netflix's Chaos Monkey randomly terminates production instances to test resilience, AI systems need approaches that randomly perturb inputs, change user demographics, and introduce edge cases to reveal failure modes
- **The VR goggles metaphor**: Vincent Koc used his experience with early VR (used for 3 hours despite a 5-minute warning, vomited for 3 hours) as a metaphor — measurement at the edge of technology is inherently "janky and weird," and that's where learning happens
- **Application**: The 20% of agent behavior that constantly changes — weird user questions, novel usage patterns — is where chaos engineering principles should be applied to discover vulnerabilities before they manifest in production

## Related

- [[summary-20260512 - Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests — Vincent Koc, OpenClaw]] — primary source
- [[VincentKoc]] — proposed the application to AI
- [[Malleable Evals]] — broader framework incorporating chaos engineering principles
- [[Eval Calcification]] — problem chaos engineering helps prevent
- [[Static Benchmarks]] — the insufficient approach chaos engineering supplements
- [[Adaptive Testing For LLMs]] — related methodology for evolving tests
