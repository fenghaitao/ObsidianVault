---
title: "Spec-Driven Testing"
type: concept
tags: [concept, agent-testing, specification, validation, evals]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence.md"]
last_updated: 2026-06-30
---

## Definition

Spec-driven testing is an approach to AI agent validation that goes beyond traditional eval datasets to include comprehensive, task-specific specifications capturing business rules, domain knowledge, ontologies, rights/roles, and robustness requirements. It treats agent testing as an integration-testing discipline, independent of the agent's implementation.

## Key Information

- Goes beyond traditional ML evaluation (datasets, F1 scores, accuracy) to create task-and-role-specific benchmarks
- A comprehensive spec includes: ground-truth datasets, business rules (e.g., "never give a discount over 10%"), ontologies/dictionaries (e.g., valid airline destinations), internal company terminology, domain knowledge (e.g., distinctions like gross profit vs gross sales), rights and roles (authentication/permission-dependent behavior), and robustness requirements
- Should be implementation-independent: tests should survive a migration from one agent framework to another (e.g., LangChain to Vertex AI)
- Enables a closed-loop improvement cycle: run agent → get results → identify robustness gaps → iterate (described as "jury-rigged RL" around the agent)
- Security testing can leverage the spec: an agent's domain of operation is also where it's most vulnerable to attack
- Long-term vision: expressing specs in an open, version-controlled format (analogous to OpenAPI for REST APIs) that can be pulled from a GitHub repo into any testing tool
- Contrasts with [[SpecificationDrivenDevelopment]], which is about using specs to guide code generation rather than testing

## Related

- [[summary-20260531 - Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence]] — source
- [[Steven Willmott]] — advocate
- [[SafeIntelligence]] — company building tooling around this concept
- [[SpecificationDrivenDevelopment]] — related but distinct paradigm for code generation
- [[Smart vs Safe Tradeoff]] — the underlying motivation for spec-driven testing
- [[Agent Robustness Testing]] — a key component of spec-driven testing
- [[Agent Specification Components]] — the elements that make up a spec
- [[Formal Verification for ML]] — SafeIntelligence's foundational approach
- [[EvalFlywheel]] — the continuous improvement loop spec-driven testing enables
