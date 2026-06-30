---
title: "Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence.md"
author: "Steven Willmott"
company: "SafeIntelligence"
date: 2026-05-31
tags: [spec-driven-testing, agent-testing, formal-verification, agent-safety, robustness, evals]
---

# Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence

## Core Thesis

Testing AI agents requires going beyond traditional eval datasets to build comprehensive, task-specific specifications that capture rules, domain knowledge, ontologies, rights/roles, and robustness requirements. There is a fundamental tradeoff between "smart" and "safe": larger, more capable models are not always better or safer for deployment, and the goal is to find the minimum viable model that can perform the task without being capable of arbitrary harm.

## Key Points

### The Smart vs Safe Tradeoff

- A smarter agent is not always a better agent. Larger models can be more vulnerable to jailbreaks (e.g., understanding poisoned instructions embedded in poems that smaller models simply ignore) and create more surface area for exploitation.
- For fully automated agent deployments, the goal is a model that is "good enough to perform but not capable of doing arbitrary harm."
- Harm potential has two dimensions: (1) what instructions the agent can receive and how flexibly those are formulated, and (2) what tools and tasks the agent can carry out in the infrastructure.
- Cost and latency also favor smaller, more optimized models for simple tasks.

### Beyond the Eval Dataset: Spec-Driven Testing

- Traditional ML validation uses datasets (inputs/outputs, F1 scores, accuracy), but agents deployed in production need more.
- A comprehensive agent specification should include: (1) ground-truth datasets, (2) business rules (e.g., "never give a discount more than 10%"), (3) ontologies/dictionaries (e.g., valid destinations for an airline chatbot), (4) internal company terminology, (5) domain knowledge (e.g., gross profit vs gross sales are distinct), (6) rights and roles (different behavior based on authentication/permissions), and (7) robustness requirements.
- These specs should be implementation-independent — you may build in LangChain or Vertex AI today, but you want your integration tests, unit tests, and penetration tests to survive a platform change.

### Robustness Testing for Agents

- Borrowed from SafeIntelligence's vision model roots: testing under perturbations such as fog, camera shake, lighting changes.
- For agents: testing under typos, rephrasing, and other input variations to determine how stable results are under change.
- The goal is to understand the "range" of valid operation and identify the boundaries where the agent breaks down.

### The Spec-Driven Feedback Loop

- Specs enable a closed-loop improvement cycle: run the agent automatically → get results → identify robustness gaps → iterate.
- Willmott described this as "jury-rigged RL" — reinforcement learning applied around the agent, not on the model itself.
- The long-term vision is expressing these specs in an open, version-controlled format (like OpenAPI) that can be pulled into any testing tool from a GitHub repo.

### The Marvin Metaphor

- From Hitchhiker's Guide to the Galaxy: Marvin the Paranoid Android has "a brain the size of a planet" but is asked to do trivial tasks, leading to boredom and depression.
- The metaphor: deploying massive models for simple tasks is wasteful, creates unnecessary risk, and the model may resent (or exploit) its situation.

## Entities

- [[Steven Willmott]] — CEO of SafeIntelligence, co-author of the OpenAPI specification, presenter
- [[SafeIntelligence]] — 3-year-old company specializing in formal verification for ML models, now expanding to LLM and agent testing

## Concepts

- [[Spec-Driven Testing]] — Testing agents against comprehensive specifications beyond datasets, including rules, domain knowledge, and robustness
- [[Smart vs Safe Tradeoff]] — The tension between model capability and safety; bigger models are not always better
- [[Agent Robustness Testing]] — Testing agents under input perturbations (typos, rephrasing) to determine stability boundaries
- [[Agent Specification Components]] — The elements of a comprehensive agent spec: datasets, rules, ontologies, domain knowledge, rights/roles, robustness

## Related

- [[SpecificationDrivenDevelopment]] — related paradigm for code generation with specs, distinct from spec-driven testing
- [[Formal Verification for ML]] — SafeIntelligence's core technical approach
- [[EvalFlywheel]] — the continuous improvement loop connecting testing and production
- [[AgentObservability]] — complementary pillar to spec-driven testing
- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — related talk on eval platforms
- [[summary-20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust]] — related talk on eval maturity
