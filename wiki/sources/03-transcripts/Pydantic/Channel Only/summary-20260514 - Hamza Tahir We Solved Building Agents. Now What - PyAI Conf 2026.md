---
title: "summary-20260514 - Hamza Tahir We Solved Building Agents. Now What - PyAI Conf 2026"
type: source
tags: [source, pydantic, pyai-conf, agent-infrastructure, mlops, harness]
sources: ["raw/03-transcripts/Pydantic/Channel Only/20260514 - Hamza Tahir We Solved Building Agents. Now What - PyAI Conf 2026.md"]
last_updated: 2026-06-25
---

## Core Summary

Hamza Tahir (ZenML) argues that while we've "solved" building individual agents, the infrastructure layer for running them at scale is underdeveloped. The model-facing harness (prompt structure, tool formats, control flow) will be consumed by improving foundation models. The world-facing harness (orchestration, durable execution, memory, sandboxes, observability) is where enterprises should invest. Draws parallels to the ML Ops evolution and predicts a similar standardization cycle for agent infrastructure.

## Key Points

- Long-running agents are predominantly coding agents — code is a general-purpose expression medium
- The harness has two layers: model-facing (will be eaten by model providers) and world-facing/infrastructure (durable investment)
- Manus rewrote their entire harness 5 times in 6 months as models improved — over-engineering control flow is risky
- Infrastructure primitives needed: durable execution, memory, sandboxes, observability, governance, identity
- Sandboxing is a central primitive — Monty, Daytona, E2B are key players
- Agents are stateful (unlike stateless microservices) — different orchestration patterns needed
- Stripe merges thousands of AI-generated PRs daily via ambient background agents
- OpenAI hired 800% more forward-deployed engineers to help enterprises deploy agent infrastructure
- Appeal: the industry needs to collectively standardize agent infrastructure, as was done for ML Ops
- Announced Kitaru: ZenML's new composable agent infrastructure layer (early testers wanted)

## Related

- [[AgentInfrastructure]] — the underdeveloped layer
- [[ZenML]] — Hamza's ML Ops company
- [[Monty]] — sandboxing primitive
- [[DurableExecution]] — key infrastructure pattern
- [[MLOps]] — the prior standardization cycle
