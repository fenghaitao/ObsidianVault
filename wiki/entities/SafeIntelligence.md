---
title: "SafeIntelligence"
type: entity
tags: [company, formal-verification, ml-validation, agent-testing, security]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence.md"]
last_updated: 2026-06-30
---

## Definition

SafeIntelligence is a 3-year-old company founded by Steven Willmott that specializes in formal verification techniques for machine learning models and AI agents.

## Key Information

- Founded approximately 3 years ago (circa 2023)
- CEO: Steven Willmott, co-author of the OpenAPI specification
- Started with formal verification on vision models and tabular data models
- Core approach: examining whole regions of the input space to identify where test points "tip over" and produce incorrect results under perturbations
- Recently (as of May 2026) released a new product extending formal verification approaches to language models and agents
- For LLMs: focuses on clever generation of edge cases and test cases (since the model itself is not directly available for formal verification)
- Product does two things: (1) security checks by pulling agent specifications into security testing, (2) robustness testing by varying inputs to measure the range of valid operation
- Uses spec information to identify where agents are most vulnerable — the domains they're supposed to act in are also where they're most likely to be attacked
- Known for rubber duck giveaways with "Think Harder" branding at conferences
- Released [[Spec 27]], a new product to test agents, announced at aiDotEngineer June 2026 by team member [[Michal Cichra]]

## Related

- [[summary-20260531 - Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence]] — source
- [[summary-20260603 - BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence]] — source
- [[Steven Willmott]] — CEO and founder
- [[Michal Cichra]] — team member, presented on decision capture
- [[Spec 27]] — agent testing product released by the team
- [[Spec-Driven Testing]] — core concept behind their agent testing product
- [[Formal Verification for ML]] — their foundational technical approach
- [[Agent Robustness Testing]] — product capability
- [[Decision Capture Loop]] — concept presented by Michal Cichra
