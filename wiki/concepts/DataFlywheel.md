---
title: "DataFlywheel"
type: concept
tags: [data, improvement, feedback-loop, evals, product]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240719 - Lessons From A Year Building With LLMs.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - What Lies Beneath the API — Benjamin Cowen, Modal.md"]
last_updated: 2026-06-30
---
## Definition
The Data Flywheel is the virtuous cycle where evals drive data collection, data drives product improvements, and improvements create better evals. It is the operational manifestation of continuous improvement for LLM applications, centered on getting products in front of users, collecting real interaction data, and using that data to systematically improve.

## Key Information
- Core concept of the 2024 AI Engineer Summit keynote's strategic and operational sections
- The flywheel starts by shipping — putting something in the wild, even in beta, to begin collecting user interactions
- "LLM responses deserve human eyes" — binary human feedback is valuable; rich feedback is a bonus but start simple
- User requests reveal product-market fit (PMF) opportunities below the product surface — what are users asking that hasn't been implemented?
- Real user interactions are the most valuable data source for improvement
- After initial deployment, transition from real-time monitoring (Slack channels of agent outputs) to daily batch reviews
- Slice data by source, keyword, or topic to find actionable patterns rather than labeling outputs as generically "bad"
- Always maintain traceability: know which GitHub commit, model version, and prompt version correspond to each trace

## Related
- [[summary-20240719 - Lessons From A Year Building With LLMs]] — source
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
- [[summary-20260602 - What Lies Beneath the API — Benjamin Cowen, Modal]] — source (data as fine-tuning prerequisite)
- [[ContinuousImprovement]] — the broader framework this operationalizes
- [[EvalEngineering]] — the practice that powers the flywheel
- [[Guardrails]] — automated quality checks that feed the flywheel
- [[Golden Dataset]] — grows through the flywheel
- [[Impact Hierarchy]] — where to invest improvement effort
- [[GenchiGenbutsu]] — the principle underlying direct data inspection
- [[BryanBischof]] — advocated for shipping beta products to start the flywheel
- [[FineTuning]] — the flywheel provides the data prerequisite
- [[DomainSpecific Models]] — what the flywheel enables through fine-tuning
