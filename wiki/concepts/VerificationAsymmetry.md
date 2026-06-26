---
title: "VerificationAsymmetry"
type: concept
tags: [concept, verification, computation-theory, p-vs-np, software-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - Making Codebases Agent Ready – Eno Reyes, Factory AI.md"]
last_updated: 2026-06-25
---

## Definition
Verification asymmetry is the principle that many tasks are significantly easier to verify (check if a solution is correct) than to solve (generate the correct solution), making automated verification a powerful force multiplier in software development.

## Key Information
- Referenced by Eno Reyes via a blog post by Jason about the asymmetry of verification
- Intuitively related to P vs NP in computer science
- Most interesting verification problems have: objective truth, quick validation, scalability (parallelizable), low noise, continuous signals
- Software development is highly verifiable, which is why coding agents are the most advanced AI agents
- Decades of work on automated validation (unit tests, E2E tests, QA tests) have created infrastructure that agents can leverage
- The concept underpins why investing in validation criteria yields outsized returns when using AI agents
- Connects to Andrej Karpathy's Software 2.0: automation via verification rather than specification

## Related
- [[summary-20251222 - Making Codebases Agent Ready – Eno Reyes, Factory AI]] — source transcript
- [[Software2.0]] — related concept by Andrej Karpathy
- [[AutomatedValidation]] — practical application
- [[AgentReadyCodebases]] — the goal enabled by this principle
