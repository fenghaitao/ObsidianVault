---
title: "Architecture Enforcement"
type: concept
tags: [architecture, linting, module-imports, enforcement, agent-workflow, prevention]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence.md"]
last_updated: 2026-06-30
---

## Definition

Architecture Enforcement is the practice of preventing architectural violations entirely through automated module import restrictions and linting rules, rather than finding and fixing them after the fact. It is a core mechanism in the Decision Capture Loop.

## Key Information

- Core principle: "What you cannot find, you cannot enforce" and "You cannot keep finding problems — you need to prevent them entirely."
- Implemented by restricting module imports: defining what each module can and cannot import from other modules
- Example 1: end-to-end BDD test suites cannot access database modules — forces tests to use only browser features, iterating without database access
- Example 2: rendering templates cannot talk to database — prevents N+1 queries entirely by making them architecturally impossible
- Example 3: database reads must return plain shapes instead of ORM objects — prevents query duplication
- Example 4: no inline styles anywhere — enforced by linting, ensures UI consistency through the design system
- These rules are defined in ADRs, which explain why the restriction exists and how to comply
- When an agent's commit violates an import restriction, the lint tool rejects it and links back to the ADR explaining the rule
- The agent reads the ADR, understands the violation, fixes it, and tries again — closing the loop

## Related

- [[summary-20260603 - BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence]] — source
- [[Architecture Decision Record (ADR)]] — where architecture enforcement rules are documented
- [[Decision Capture Loop]] — the reinforcement loop that includes architecture enforcement
- [[Design System]] — architecture enforcement applies to UI consistency rules too
- [[Enforce Dont Instruct]] — related principle
- [[SpecificationDrivenDevelopment]] — related paradigm
