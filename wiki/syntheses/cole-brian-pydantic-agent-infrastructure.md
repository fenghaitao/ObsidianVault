---
title: "cole-brian-pydantic-agent-infrastructure"
type: synthesis
tags: [synthesis, comparison, agent-infrastructure, harness, cole-medin, brian-casel, pydantic]
sources: []
last_updated: 2026-06-25
---

# How Pydantic, Cole Medin, and Brian Casel Approach Agent Infrastructure

## The Shared Diagnosis

All three converge on the same insight: the model alone isn't enough. The wrapper around it — the harness, the infrastructure, the scheduling layer — is where competitive advantage lives. But they approach it from different altitudes and for different audiences.

## Cole Medin: The Architecture

Cole Medin's [[HarnessEngineering]] is the most comprehensive framework. It has two layers: the single-session [[AILayer]] (rules, skills, MCP, hooks, sub-agents) and multi-session orchestration ([[RalphLoop]], [[AdversarialDev]]). His key insight: the model-facing harness will be eaten by model providers; invest in the world-facing infrastructure. The mindset is [[SystemEvolution]] — every failure improves the harness.

Cole's reference architecture (from Anthropic's open-source harness): an initializer agent scaffolds the project, then a task agent loops with fresh context each session, reading progress artifacts, implementing features, and self-validating. The file system is the memory. The tool belt extends the harness with Linear, GitHub, and Slack sub-agents via [[Arcade]].

## Pydantic: The Primitives

Hamza Tahir's PyAI Conf talk [[summary-20260514 - Hamza Tahir We Solved Building Agents. Now What - PyAI Conf 2026]] makes the identical distinction: model-facing harness vs. world-facing infrastructure. He argues the industry needs to standardize agent infrastructure the way ML Ops standardized model deployment. The Pydantic stack is his exhibit A for infrastructure primitives:

- **[[Monty]]** — sandboxing: secure Python execution for AI-generated code, ~1 microsecond startup, white-list approach
- **[[Logfire]]** — observability: OpenTelemetry-based tracing with AI-specific features, MCP distributed tracing
- **[[PydanticAIGateway]]** — governance: unified LLM inference with budgeting, model fallback, edge deployment
- **[[DBOS]]** — durable execution: Postgres-based checkpointing for crash recovery and workflow forking
- **[[PydanticAI]]** — agent framework: type-safe, MCP-native, with Pydantic Graph for multi-step workflows

Samuel Colvin's Monty talks [[summary-20260401 - Samuel Colvin Controlling the wild： Monty, from tool calling to computer use - PyAI Conf 2026]] frame the infrastructure problem as a spectrum: tool calling (most controlled) → Monty → sandboxing services → coding agents → full computer use (least controlled). Each point on the spectrum has economic value; Monty fills the gap between simple tool calling and expensive sandbox VMs.

## Brian Casel: The Accessible On-Ramp

Brian Casel's [[NightShiftModel]] operates at a different scale — solo builder, not enterprise. His infrastructure is lighter: a scheduling platform (Hermes, Claude Co-work), a shared interface (markdown files or custom apps like [[SparkDrop]] and [[BrainDown]]), and portable skills. He doesn't need Monty or DBOS because his agents run on dedicated machines with controlled scope.

His key insight is [[AgentPlatformPortability]]: the pattern matters more than the platform. The Night Shift works on OpenClaw, Hermes, Claude Co-work, or Claude Code because the skills (markdown files) are portable. This is the pragmatic counterpoint to Cole's deep tooling integration and Pydantic's infrastructure primitives.

## The Enterprise Extreme

Abhishyant Khare's Co-Founder CTO demo [[summary-20260408 - Abhishyant Khare Agent Native Engineering With Cofounder⧸CTO - PyAI Conf 2026]] shows harness engineering at production scale: a CTO agent managing engineering, support, finance, and marketing departments, with agents querying their own Logfire traces for self-debugging. Three principles: agents control the full lifecycle of sub-agents, delegation is async, and agents have full visibility into the system.

## The Synthesis

The progression is additive — you start with Brian's scheduled delegation, layer on Cole's harness patterns, and instrument with Pydantic's infrastructure. Cole provides the architecture, Pydantic provides the primitives, Brian provides the accessible on-ramp, and companies like GIC prove it works at scale.

## Related

- [[HarnessEngineering]] — Cole's discipline
- [[AgentHarness]] — the artifact
- [[AgentInfrastructure]] — the underdeveloped layer
- [[NightShiftModel]] — Brian's pattern
- [[Monty]] — Pydantic's sandboxing primitive
- [[Logfire]] — Pydantic's observability primitive
- [[PydanticAIGateway]] — Pydantic's governance primitive
- [[DBOS]] — durable execution
- [[RalphLoop]] — Cole's multi-session pattern
- [[AILayer]] — Cole's single-session wrapper
- [[AgentPlatformPortability]] — Brian's platform strategy
- [[cole-vs-brian-agent-autonomy]] — prior Cole vs Brian synthesis
