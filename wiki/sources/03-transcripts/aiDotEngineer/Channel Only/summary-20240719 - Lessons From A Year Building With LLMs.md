---
title: "summary-20240719 - Lessons From A Year Building With LLMs"
type: source
tags: [source, transcript, llm, strategy, operations, tactics, evals, ai-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240719 - Lessons From A Year Building With LLMs.md"]
last_updated: 2026-06-26
---
## Core Summary
Six practitioners (Bryan Bischof, Hamel Hussein, Jason Lou, Eugene Yan, Shreya Shankar, and others) deliver a keynote distilling their widely-read O'Reilly white paper on lessons from a year of building LLM applications. The talk is structured across three levels: strategic considerations (model-as-moat fallacy, Moore's Law for LLMs, continuous improvement), operational considerations (talent, team composition, the AI engineer role), and tactical considerations (evals, monitoring, guardrails, LLM-as-judge). The central argument is that success comes not from chasing the latest model or tool but from building evals, looking at real user data, and establishing a virtuous cycle of continuous improvement rooted in decades-old principles from Toyota's Kaizen to DevOps.

## Key Points
- The model is not your moat — build in your zone of genius, treat models as interchangeable SaaS products, and focus on product quality and user experience
- LLM inference costs drop roughly an order of magnitude every 12-18 months, faster than Moore's Law, enabling applications that are uneconomical today to become viable within 30 months
- The virtuous cycle of improvement (evals → data → improvements) traces back through MLOps, DevOps, Lean Startup, and ultimately Toyota's Kaizen and genchi genbutsu principle
- Do not hire a machine learning engineer until you have data; start with application/software engineering, add platform/data engineering, then ML engineering
- AI engineer is an aspirational but often overscoped and underspecified role — deliberate practice on evals and data literacy (4-6 weeks) can close the gap
- Assertion-based evals (checking extracted price, title, columns) are simple and effective; break amorphous outputs into dimensions before evaluating
- LLM-as-judge is easy to prototype but hard to align; fine-tuned classifiers are more precise and 100x faster, but require more upfront investment
- Look at production data regularly (real-time Slack channels initially, then daily batch jobs), slice by source/keyword/topic, and always pin model versions
- Implement guardrails as table stakes: toxicity, PII, copyright, expected language, and hallucinations; reference-free evals can double as guardrails
- Technical debt principles from traditional ML systems (data verification, feature engineering, monitoring, infrastructure) all apply to LLM applications

## Related
- [[BryanBischof]] — co-author and speaker (strategic section)
- [[HamelHussein]] — co-author and speaker (operational section)
- [[JasonLou]] — co-author and speaker (operational section)
- [[ShreyaShankar]] — co-author and speaker (tactical section)
- [[EugeneYan]] — co-author and speaker (tactical section)
- [[ModelIsNotTheMoat]] — core strategic thesis
- [[ContinuousImprovement]] — the unifying framework across all levels
- [[AIEngineer]] — the role and its skill gaps
- [[DataFlywheel]] — the virtuous cycle of evals, data, and improvement
- [[Guardrails]] — automated quality and safety checks in production
- [[LLM-as-Judge]] — evaluation technique discussed in depth
- [[RAG]] — mentioned as a common approach that shouldn't be solved by tool-churning
- [[MooresLawForLLMs]] — cost reduction trend enabling future applications
- [[FineTuning]] — discussed as a premature optimization without data
- [[ReferenceFreeEvals]] — technique usable as guardrails
- [[GenchiGenbutsu]] — Toyota principle applied to LLM data inspection
- [[BrandoliniLaw]] — adapted for LLM defect catching costs
- [[OReilly]] — publisher of the original white paper
- [[AlanKay]] — cited for PARC's Moore's Law projection technique
- [[EricRies]] — Lean Startup methodology as precursor to iterative improvement
- [[ShigeoShingo]] — Toyota production system figure quoted on value creation
- [[ToyotaProductionSystem]] — origin of Kaizen and continuous improvement principles
- [[XeroxPARC]] — historical example of building for future capabilities
- [[AndrejKarpathy]] — quoted on the difficulty of turning demos into products
- [[OpenAI]] — model provider discussed (GPT-4, DaVinci series)
- [[Anthropic]] — model provider (Sonnet mentioned as competitive alternative)
- [[GitHubCopilot]] — cited for specific, deliberate job titles
- [[Waymo]] — example of long timeline from demo (1988) to production (2020s)
- [[MLflow]] — traditional MLOps tool praised for traceability
- [[AppleIntelligence]] — cited as example shipping evals-backed features in beta
- [[Hex]] — cited as example shipping evals-backed features in beta
