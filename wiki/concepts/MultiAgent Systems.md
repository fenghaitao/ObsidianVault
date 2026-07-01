---
title: "Multi-Agent Systems"
type: concept
tags: [agent-architecture, workflow, orchestration, heterogeneous]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum.md"]
last_updated: 2026-06-30
---

## Definition
Multi-Agent Systems are workflow architectures where multiple AI agents collaborate to solve complex tasks, replacing single LLM calls. They represent the workflow level of the shift from homogeneous to heterogeneous intelligence, where different agents may use different models, architectures, and hardware.

## Key Information
- Replacing single LLM calls as part of the transition to heterogeneous intelligence
- Operate at the workflow layer of heterogeneity (alongside architecture-level MoE and hardware-level prefill-decode disaggregation)
- In heterogeneous implementations: different sub-agents use different LLMs optimized for their specific tasks
- [[Callosum]] optimizes multi-agent systems at three levels: hardware selection per agent, agent interaction patterns, and workflow construction
- [[Heterogeneous Recursion]] is a specific multi-agent pattern for long-context tasks
- Multi-modal web navigation uses heterogeneous multi-agent composition of video action language models
- Enables agents to decompose complex, open-ended problems into sub-problems matched to specialized capabilities

## Related
- [[Heterogeneous Intelligence]] — the paradigm enabled by multi-agent systems
- [[Mixture of Experts]] — architecture-level heterogeneity
- [[Heterogeneous Recursion]] — specific multi-agent pattern for long context
- [[Agent Orchestration]] — coordination of multi-agent systems
- [[summary-20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum]] — source
