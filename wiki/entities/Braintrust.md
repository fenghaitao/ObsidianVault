---
title: "Braintrust"
type: entity
tags: [company, evals, observability, ai-platform]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260501 - Shipping complex AI applications — Braintrust & Trainline.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260515 - Combine Skills and MCP to Close the Context Gap — Pedro Rodrigues, Supabase.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260525 - Does GenAI ＂belong＂ to data scientists — Phil Hetzel, Braintrust.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition

Braintrust is an AI observability and evaluation platform that helps organizations ship quality AI applications at scale. Founded by Ankur Goyal, it raised $80M Series B at an $800M valuation from investors including a16z and Greylock.

## Key Information

- Founded approximately 3 years ago, Series B company
- $80M raised at $800M valuation; investors include Iconic, Andreessen Horowitz, Greylock
- Founder Ankur Goyal previously founded Impira (acquired by Figma) and led ML at Figma
- Created Brainstorm, a custom database for semi-structured AI evaluation data
- Tool-agnostic: works with any agent framework or LLM provider
- Key concept: the evaluation flywheel (start with evals, identify failures, remediate, ship, monitor, repeat)
- Two pillars of agent quality: evals (experimentation confidence) and observability (production confidence)
- Treats observability and evals as the same problem from a systems perspective — only difference is evals run in batch with known inputs
- Built a custom database (Brainstorm) from the ground up for agent traces, moving away from ClickHouse because of text-based indexing requirements
- Uses Tantivy (Rust-based full-text indexing framework, similar to Apache Lucene) for text search across traces
- Recently rolled out automated topic modeling on agent traces using lightweight LLMs for embedding and clustering
- Solutions engineering team (led by Phil Hetzel) ensures customers get maximum value quickly
- Platform includes human labeling component for domain expert annotation workflows
- Agent and prompt playground lets both technical and non-technical users experiment with prompts
- European customers include Lovable, Doctolib, Trainline

## Related

- [[summary-20260501 - Shipping complex AI applications — Braintrust & Trainline]] — source
- [[summary-20260525 - Does GenAI ＂belong＂ to data scientists — Phil Hetzel, Braintrust]] — source
- [[PhilHetzel]] — solutions engineering lead
- [[EvalEngineering]] — evaluation engineering
- [[AgentObservability]] — agent observability
- [[EvalFlywheel]] — iterative evaluation cycle
- [[HumanAnnotation]] — human labeling component of the platform
- [[CrossFunctionalAgentTeams]] — team composition advocated by Braintrust's Phil Hetzel
- [[summary-20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust]] — source
- [[summary-20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust]] — source
- [[EvalPracticePhases]] — practitioner maturity model from Braintrust's Phil Hetzel
- [[EvalPrimitives]] — task, dataset, scoring function framework
- [[Tantivy]] — text indexing framework used in Brainstorm database
- [[ClickHouse]] — OLAP database Braintrust previously used
- [[TopicModelingForAgents]] — automated trace clustering feature
- [[TextBasedIndexing]] — full-text search requirement driving custom database
- [[AgentTraceData]] — semi-structured, voluminous trace data challenges
