---
title: "ShreyaShankar"
type: entity
tags: [person, ai, researcher, mlops, evals]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240719 - Lessons From A Year Building With LLMs.md"]
last_updated: 2026-06-26
---
## Definition
Shreya Shankar is an AI researcher and co-author of the O'Reilly white paper "What We Learned from a Year of Building with LLMs." She presented the tactical considerations section of the keynote at the AI Engineer Summit, focusing on evals, monitoring, guardrails, and the importance of looking at production data.

## Key Information
- Co-author of a seminal MLOps paper (circa 2015) that communicated the idea that the model is only a small part of a production ML system
- Co-authored the O'Reilly white paper on LLM application building lessons alongside five other practitioners
- Presented the tactical track of the keynote alongside Eugene Yan
- Emphasized that looking at real production data regularly is critical for LLM application quality
- Advocated for slicing data by source, keyword, or topic to find actionable patterns rather than just labeling outputs as bad
- Stressed the importance of traceability: knowing which GitHub commit, model version, and prompt version correspond to each trace
- Recommended pinning model versions because LLM API behavior changes in hard-to-quantify ways

## Related
- [[summary-20240719 - Lessons From A Year Building With LLMs]] — source
- [[EugeneYan]] — co-author and co-presenter
- [[TechnicalDebtInML]] — concept from her earlier MLOps paper
- [[EvalEngineering]] — core practice she advocated
- [[Guardrails]] — topic she presented on
- [[PinModelVersion]] — practice she recommended
