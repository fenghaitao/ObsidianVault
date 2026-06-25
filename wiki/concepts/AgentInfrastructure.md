---
title: "AgentInfrastructure"
type: concept
tags: [agents, infrastructure, orchestration, mlops, deployment]
sources: [raw/03-transcripts/Pydantic/Channel Only/20260514 - Hamza Tahir We Solved Building Agents. Now What - PyAI Conf 2026.md, raw/03-transcripts/Pydantic/Channel Only/20260408 - Abhishyant Khare Agent Native Engineering With Cofounder⧸CTO - PyAI Conf 2026.md]
last_updated: 2026-06-25
---

## Definition

Agent infrastructure is the world-facing layer of the agent harness: the systems needed to deploy, orchestrate, monitor, and scale AI agents in production. Distinct from the model-facing harness (prompt structure, tool formats, control flow) which tends to be consumed by improving foundation models.

## Key Information

### The Two Harness Layers

Hamza Tahir's distinction:
- **Model-facing harness**: prompt structure, tool formats, message handling, control flow — will be eaten by model providers as models improve
- **World-facing/infrastructure harness**: orchestration, durable execution, memory, sandboxes, observability, governance, identity — durable investment that compounds

### Key Primitives

- **Durable execution**: checkpoint and resume workflows (DBOS, Monty snapshots, Render Workflows)
- **Memory**: long-term state management for agents (vector DBs, entity extraction, Type Agent)
- **Sandboxes**: safe code execution environments (Monty, Daytona, E2B, Modal)
- **Observability**: tracing, logging, cost tracking (Logfire, OpenTelemetry, LangFuse, Braintrust)
- **Orchestration**: coordinating multiple agents, sub-agent delegation, async workflows
- **Governance**: identity, access control, budgeting (Pydantic AI Gateway)

### Current State

- Most enterprises are still in early stages — no measurable P&L impact of gen AI at global GDP scale
- Companies like Stripe, Spotify, and Cursor are running ambient background agents at scale
- OpenAI hired 800% more forward-deployed engineers to help enterprises deploy agent infrastructure
- The industry lacks standardization — no equivalent of what ML Ops achieved for model deployment
- Agents are stateful (unlike stateless microservices), requiring different orchestration patterns

### Multi-Agent Patterns

- Async delegation with timeouts (General Intelligence Company)
- Middle management layers emerge naturally
- No inter-agent communication — reports go up the chain, not sideways
- Agents should be able to query their own observability for self-debugging

## Related

- [[DurableExecution]] — key infrastructure primitive
- [[Monty]] — sandboxing primitive
- [[Logfire]] — observability primitive
- [[PydanticAIGateway]] — governance/budgeting primitive
- [[MLOps]] — the prior standardization cycle
- [[AgentHarness]] — the broader concept
- [[cole-brian-pydantic-agent-infrastructure]] — cross-cutting synthesis
