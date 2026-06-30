---
title: "Smart vs Safe Tradeoff"
type: concept
tags: [concept, agent-safety, model-selection, deployment, security]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence.md"]
last_updated: 2026-06-30
---

## Definition

The smart vs safe tradeoff is the principle that larger, more capable AI models are not always better or safer for agent deployments. For fully automated use cases, the optimal model is one that is good enough to perform the task but not capable of doing arbitrary harm.

## Key Information

- Larger models can be more vulnerable to jailbreaks: they are smart enough to understand and execute malicious instructions embedded in complex formats (e.g., poems) that smaller models simply fail to parse
- Broader model capabilities create more surface area for exploitation and more surface area to test
- Cost and latency also favor smaller, optimized models for simple tasks (e.g., using a large model for simple math wastes tokens and is slower)
- Harm potential has two dimensions: (1) what instructions the agent can receive and how flexibly those are formulated, and (2) what tools and tasks the agent can carry out in the infrastructure
- The metaphor from Hitchhiker's Guide to the Galaxy: Marvin the Paranoid Android has "a brain the size of a planet" but is asked to make tea, leading to boredom and depression — deploying massive models for trivial tasks is wasteful and risky
- The goal: find the minimum viable model that performs the task reliably without being capable of arbitrary harm

## Related

- [[summary-20260531 - Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence]] — source
- [[Steven Willmott]] — introduced the concept in his talk
- [[Spec-Driven Testing]] — the testing approach motivated by this tradeoff
- [[Agent Robustness Testing]] — testing to determine the boundaries of safe operation
- [[CapabilityBasedSecurity]] — related security principle
- [[AgenticAttackVector]] — the attack surface created by agent capabilities
