---
title: "Agent Specification Components"
type: concept
tags: [concept, agent-testing, specification, evals, agent-design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence.md"]
last_updated: 2026-06-30
---

## Definition

Agent specification components are the distinct elements that together form a comprehensive specification for what an AI agent is supposed to do. They go beyond traditional eval datasets to capture the full context of the agent's task, role, and operating constraints.

## Key Information

A comprehensive agent specification includes seven component types:

1. **Ground-Truth Datasets**: Examples of what good looks like — the traditional eval/test set of inputs and expected outputs
2. **Business Rules**: Hard constraints the agent must never violate (e.g., "never give a discount more than 10%," "no refunds after 30 days")
3. **Ontologies/Dictionaries**: The relevant universe of valid entities (e.g., an airline chatbot only flies to certain destinations)
4. **Internal Terminology**: Company-specific terms and policies that no one outside the organization knows, but the agent must respect
5. **Domain Knowledge**: Field-specific distinctions that general LLMs may confuse (e.g., gross profit vs gross sales — interchangeable to an LLM but critically different in business)
6. **Rights and Roles**: How the agent's behavior differs based on authentication state, permissions, and user roles
7. **Robustness Requirements**: How the agent performs under stress — typos, rephrasing, input variations — and the acceptable degradation envelope

These components should be implementation-independent, surviving migration between agent frameworks and platforms. The long-term vision is expressing them in an open, version-controlled format (analogous to OpenAPI for APIs).

## Related

- [[summary-20260531 - Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence]] — source
- [[SpecDriven Testing]] — the testing approach built on these components
- [[Agent Robustness Testing]] — the testing of component 7 (robustness requirements)
- [[Smart vs Safe Tradeoff]] — the safety motivation for comprehensive specs
- [[Steven Willmott]] — introduced this framework
- [[SpecificationDrivenDevelopment]] — related concept for code generation specs
