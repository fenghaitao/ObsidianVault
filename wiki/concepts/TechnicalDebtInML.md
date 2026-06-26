---
title: "TechnicalDebtInML"
type: concept
tags: [mlops, infrastructure, maintenance, llm, systems]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240719 - Lessons From A Year Building With LLMs.md"]
last_updated: 2026-06-26
---
## Definition
Technical Debt in ML refers to the principle that the machine learning model itself is only a small component of a production ML system, with the surrounding infrastructure (data verification, feature engineering, monitoring, configuration, serving) accumulating significant maintenance burden over time. The 2024 AI Engineer Summit keynote argued these same principles apply to LLM applications, just with different manifestations.

## Key Information
- Originated from a seminal 2015 MLOps paper (co-authored by Shreya Shankar, among others) that visualized the model as a tiny box surrounded by vast infrastructure
- The paper communicated that when productionizing ML systems, there is far more around the model that must be maintained over time
- For LLMs, the same principles apply with updated mappings: feature engineering becomes RAG context engineering; data validation becomes evals and guardrails; model monitoring becomes output quality monitoring
- "It's not just simply wrap your model or GPT in some software and ship it — there's a lot of investment that needs to happen around the model"
- The infrastructure around the model changes as models change under the hood, requiring ongoing maintenance
- The closing message: going from demo to production takes time (illustrated by the 1988-2020s timeline of neural-network-driven cars)

## Related
- [[summary-20240719 - Lessons From A Year Building With LLMs]] — source
- [[ShreyaShankar]] — co-author of the 2015 paper referenced
- [[ContinuousImprovement]] — the framework for managing this debt
- [[MLflow]] — a traditional MLOps tool that addressed some of this infrastructure
- [[AndrejKarpathy]] — quoted on the demo-to-production gap
- [[RAG]] — the modern LLM equivalent of feature engineering
- [[Guardrails]] — the modern equivalent of data validation
