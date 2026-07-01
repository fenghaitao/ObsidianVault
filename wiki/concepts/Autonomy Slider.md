---
title: "Autonomy Slider"
type: concept
tags: [ai-engineering, architecture, agents, workflows, decision-making]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi.md"]
last_updated: 2026-06-26
---

## Definition
The Autonomy Slider is a mental model for AI system design that places approaches on a spectrum from simple prompting (low autonomy, high control, low cost) to fully agentic systems (high autonomy, low control, high cost). It helps AI engineers choose the right level of complexity for a given task, always starting with the simplest solution.

## Key Information
- **Spectrum**: Simple prompting → few-shot examples → context injection → retrieval-augmented generation → advanced workflows (chaining, routing, parallelization, loops) → single-agent systems → multi-agent systems
- **Trade-off**: More autonomy means less control over the system and higher cost. More control means less flexibility
- **Decision framework**: Ask a series of questions to determine where on the slider a task belongs:
  1. Does the model already know enough? → Just prompt it
  2. Need external context under 200K tokens? → Paste it in, use context caching
  3. Context not known until query time? → Inject knowledge on the fly (RAG)
  4. Need different approaches based on conditions? → Advanced workflow with predetermined steps
  5. Need autonomous actions and dynamic branching? → Agent
- **Most "agent" requests are workflows**: Clients often ask for agents when simple workflows would suffice. Example: a support ticket system with 6 fixed sequential steps does not need an agent
- **Real systems combine all levels**: Production AI products mix prompting, workflows, tools, and agents. Deep Research is an example combining all techniques
- **Start simple**: Always begin with the simplest solution and only add complexity when necessary

## Related
- [[summary-20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi]] — source
- [[AgenticWorkflows]] — the workflow portion of the spectrum
- [[MultiAgentArchitecture]] — the most complex end of the spectrum
- [[LouisFrançois Bouchard]] — introduced this mental model
- [[Deep Research Agent]] — example system combining all levels
- [[Context Budget]] — constraint that influences where to place a system on the slider
