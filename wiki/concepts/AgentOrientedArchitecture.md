---
title: "AgentOrientedArchitecture"
type: concept
tags: [agent-architecture, coding-agent, design-philosophy]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - Amp Code： Next Generation AI Coding – Beyang Liu, Amp Code.md"]
last_updated: 2026-06-25
---

## Definition
Agent-oriented architecture is Amp Code's design philosophy that rejects the conventional model-selector UX pattern in favor of purpose-built agents optimized for specific modalities. Instead of letting users choose from N different models, the architecture provides a small number of top-level agents (Smart and Rush) each deeply optimized for their use case.

## Key Information
- Contrasts with the model-selector approach used by most coding agents, where users pick from multiple models in a dropdown
- Model selectors create a paradox of choice — cognitive burden on the user, and prevent deep optimization for any single model
- Amp Code has exactly two top-level agents: Smart Agent (complex tasks, sub-agent access) and Rush Agent (fast, tight-loop edits)
- These two agents pick points along the "frontier of intelligence and speed" that are meaningful to user experience
- Maps to two user modalities: asynchronous task-spinning (Smart) and in-the-loop babysitting (Rush)
- Amp Code has only switched the Smart model once (to Gemini 3), reflecting deep investment in optimization per model

## Related
- [[summary-20251222 - Amp Code： Next Generation AI Coding – Beyang Liu, Amp Code]] — source
- [[AmpCode]] — product implementing this architecture
- [[SubAgents]] — key component of the Smart Agent
