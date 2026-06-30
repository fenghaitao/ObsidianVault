---
title: "Contract Negotiation"
type: concept
tags: [ai, agents, harness, evaluation, specification, generator-evaluator]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson.md"]
last_updated: 2026-06-30
---

## Definition
Contract Negotiation is a mechanism in the generator-evaluator harness pattern where the builder agent and evaluator agent negotiate what "done" means before any code is written. They exchange proposals and critiques via files on disk until both agree on feature scope, test criteria, and edge cases. The evaluator then grades the final output against this mutually agreed contract rather than the original high-level spec.

## Key Information
- **Pre-Build Negotiation**: Before the generator writes a single line of code, the two agents negotiate the definition of done via files on disk — one writes markdown, the other reads it, iterating until both agree
- **Example Flow**: Generator proposes "I'll build X feature, you verify by testing Y." Evaluator pushes back: "scope too big, tests too weak, missed XYZ edge case." Back-and-forth until consensus
- **Contracts vs Specs**: Evaluator grades against the contract the two agents decided between themselves, not the original spec the planner one-shotted at the beginning. This bridges user stories (spec) into tangible, testable assertions without the planner over-specifying
- **Granularity Matters**: For the Retro Forge demo, 27 contract criteria were established. Vague criteria produce vague critiques that the generator shrugs off; granular criteria tell the agent exactly which line to fix
- **Key Innovation Over RALPH Loop**: The RALPH loop had a fixed plan.md, but nobody on the other side argued with the main loop. Contract negotiation adds adversarial pressure that the RALPH loop lacked
- **Planner Separation**: The planner sets high-level outer boundaries; the generator and evaluator figure out exact feature sets and contracts to satisfy that spec. The planner doesn't intervene mid-build
- **File System as Medium**: Contracts are exchanged as markdown files on disk — simple, persistent, greppable, and accessible to any agent or human

## Related
- [[summary-20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson]] — source
- [[Generator-Evaluator Pattern]] — parent harness pattern
- [[Self-Evaluation Trap]] — problem this mechanism helps avoid
- [[Rubric-Based Evaluation]] — complementary evaluation framework
- [[File System as Shared State]] — communication medium for contracts
- [[Sprint Decomposition]] — planner's role in setting scope
- [[RALPH Loop]] — predecessor pattern lacking this mechanism
- [[Specification]] — broader concept of defining what to build
