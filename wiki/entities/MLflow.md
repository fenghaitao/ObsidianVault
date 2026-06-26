---
title: "MLflow"
type: entity
tags: [tool, mlops, experiment-tracking, open-source]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240719 - Lessons From A Year Building With LLMs.md"]
last_updated: 2026-06-26
---
## Definition
MLflow is an open-source MLOps platform for managing the machine learning lifecycle, including experiment tracking, model registry, and deployment. In the keynote, it is cited as a successful example of traditional MLOps tooling that made it easy to trace back which code version, model version, and data correspond to each result — a capability equally important for LLM applications.

## Key Information
- Open-source platform for the ML lifecycle (tracking, projects, models, registry)
- Praised for making traceability easy: knowing which code, data, and model version produced each result
- The traceability capability it pioneered is recommended for LLM application development — always know which GitHub commit, model version, and prompt version correspond to each trace
- Represents the type of infrastructure that needs to be built around LLMs, not just wrapping the model API

## Related
- [[summary-20240719 - Lessons From A Year Building With LLMs]] — source
- [[TechnicalDebtInML]] — the broader concept of infrastructure needed around models
- [[ContinuousImprovement]] — the iterative cycle it supports
