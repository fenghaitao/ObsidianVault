---
title: "AgentTraining"
type: concept
tags: [agents, training, memory, consistency, crewai, cli]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240808 - Using agents to build an agent company： Joao Moura.md"]
last_updated: 2026-06-26
---

## Definition
Agent Training is the process of baking instructions and desired behaviors into an agent crew's memory so they produce consistent results over time. Analogous to training a new employee, it encodes best practices and preferences directly into the agent's persistent memory rather than requiring explicit instructions in every interaction.

## Key Information
- Announced as a CrewAI feature: "Train Your Crew" CLI
- User runs the CLI and gives instructions to the crew
- Instructions become baked into the agents' memory
- Results in consistent outputs over repeated runs
- Analogy: "when you hire a new employee you train them — why not do that with your crew?"
- Distinct from per-request prompting: training persists across sessions
- Complements prompt engineering by encoding organizational knowledge and preferences permanently
- Enables agents to align with company-specific conventions, tone, and quality standards without repeated instruction

## Related
- [[summary-20240808 - Using agents to build an agent company： Joao Moura]] — source
- [[CrewAI]] — framework offering this feature
- [[AgentMemory]] — memory layer that training bakes into
- [[PromptOptimizationLoop]] — related concept of iterative prompt refinement
- [[FewShotExamples]] — alternative approach to consistent agent behavior
