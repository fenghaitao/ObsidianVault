---
title: "Agent as Octopus"
type: concept
tags: [agents, design-philosophy, flexibility, constraints]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - LLM codegen fails and how to stop 'em — Danilo Campos, PostHog.md"]
last_updated: 2026-06-29
---

## Definition
"Agent as octopus" is a design philosophy for autonomous coding agents: agents are flexible and can wiggle into tight corners and maneuver around problems, so the goal is not to over-constrain them with rigid scaffolding but to provide enough well-sequenced information for them to do the right thing.

## Key Information
- Articulated by Danilo Campos (PostHog) as a guiding principle for the PostHog Wizard
- The metaphor: an octopus can squeeze into tight corners and maneuver around obstacles — agents have similar flexibility in problem-solving
- Core tension: you need to prevent shenanigans (security, destructive actions) but should not over-constrain the agent's problem-solving ability
- The right approach: step back, give enough information, and sequence it properly so the agent does what you want
- Contrasts with the instinct to "scaffold the hell out of the behavior of this agent"
- Implication: invest in information quality and sequencing (prose, documentation, breadcrumbing) rather than rigid control structures
- Complements the "Code as Depreciating Asset" insight: the value is in the prose that guides the agent, not in elaborate agent harness code

## Related
- [[summary-20260430 - LLM codegen fails and how to stop 'em — Danilo Campos, PostHog]] — source
- [[DaniloCampos]] — articulated the concept
- [[PostHogWizard]] — product embodying this philosophy
- [[Breadcrumbing]] — information sequencing technique
- [[Code as Depreciating Asset]] — complementary insight
- [[AgentHarnessSeparation]] — related architectural principle
- [[MinimalAgentDesign]] — related design philosophy
- [[Fine-Grained Tool Permissions]] — the necessary constraints (security)
