---
title: "Agent Robustness Testing"
type: concept
tags: [concept, agent-testing, robustness, perturbation, input-variation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence.md"]
last_updated: 2026-06-30
---

## Definition

Agent robustness testing is the practice of evaluating AI agents under input perturbations — such as typos, rephrasing, and other variations — to determine the stability boundaries of their operation. It measures how much input variation an agent can tolerate before its outputs become unreliable.

## Key Information

- Originates from SafeIntelligence's work on vision model robustness: testing object detection under fog, camera shake, lighting changes, and other environmental perturbations
- For language-based agents, robustness perturbations include: typos (how many before the agent breaks?), rephrasing (how stable are results under rewording?), and other input variations
- The goal is to understand the "range" or "envelope" of valid operation and identify where the agent tips over into incorrect behavior
- Directly addresses user frustration: if a customer-facing agent fails on simple typos, it degrades the user experience
- Part of the broader [[Spec-Driven Testing]] framework, where robustness requirements are one component of a comprehensive agent specification
- Enables a closed-loop improvement cycle: identify robustness gaps → iterate on the agent → re-test → redeploy

## Related

- [[summary-20260531 - Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence]] — source
- [[Spec-Driven Testing]] — the broader framework this is part of
- [[Agent Specification Components]] — robustness requirements as one element of a spec
- [[SafeIntelligence]] — company with products for robustness testing
- [[Smart vs Safe Tradeoff]] — the safety motivation behind robustness testing
- [[Formal Verification for ML]] — SafeIntelligence's foundational approach to input-space analysis
- [[UserFrustration]] — the real-world impact of poor robustness
