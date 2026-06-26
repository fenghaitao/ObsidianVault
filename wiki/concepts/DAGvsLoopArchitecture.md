---
title: "DAGvsLoopArchitecture"
type: concept
tags: [agent-architecture, design-tradeoffs, coding-agents, determinism]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer.md"]
last_updated: 2026-06-25
---

## Definition
DAG vs. loop architecture is the fundamental design trade-off in agent systems between deterministic directed acyclic graph (DAG) workflows and flexible model-driven while-loops. DAGs enforce sequential execution and prevent hallucinations but create complex webs of engineering; loops trust the model to explore and adapt but sacrifice determinism.

## Key Information
- For ~2.5 years before December 2025, most agent builders used DAGs with hundreds of nodes: classifiers, routing prompts, conditional branches
- DAG advantages: guarantee against hallucinations, solve prompt injection (classifier nodes with thrown-away context), enforce specific output formats
- Loop advantages: 10x easier to develop, 10x more maintainable, actually works better because models are now good enough
- The happy middle ground: use the agent paradigm of a master while-loop with tool calls, but make tool calls rigorous and testable
- Use-case dependent: general-purpose coding agents benefit from loops; structured deliverables (travel itineraries, specific email formats) may benefit from DAG-like tool calls
- Zoneraich recommends: for exploration, trust the model; for deterministic outputs, build rigorous tools
- The trend is toward loops — "we're getting rid of all this stuff" (ML-based intent detection, ReAct baked in, classifiers)
- Even the DAG example of customer support agents (refund routing, etc.) is being replaced by model-driven approaches

## Related
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — source
- [[MasterWhileLoop]] — the loop side of the trade-off
- [[SimpleDesignPhilosophy]] — the philosophy favoring loops
- [[ToolCalling]] — the mechanism that enables loops
- [[AgentSmell]] — evaluation approach for loop-based agents
