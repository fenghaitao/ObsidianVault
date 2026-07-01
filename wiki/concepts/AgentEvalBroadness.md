---
title: "AgentEvalBroadness"
type: concept
tags: [evals, agents, metrics, evaluation, genai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260525 - Does GenAI ＂belong＂ to data scientists — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition

Agent evaluation broadness is the principle that evaluating AI agents requires assessing functional performance across a much wider surface area than traditional ML metrics (precision, recall, F1). Data scientists accustomed to those narrow technical metrics may need to expand their evaluation approach to cover the full behavioral scope of an agent.

## Key Information

- Traditional ML metrics (precision, recall, F1) measure technical performance on a two-box classification problem
- Agent evaluation must assess functional performance: does the agent accomplish what the user needs across diverse, real-world scenarios?
- Data scientists may "obsess over" traditional metrics because those metrics have served them well historically, but agents demand broader evaluation
- The evaluation surface area includes: correctness of outputs, appropriateness of tool use, handling of edge cases, adherence to guardrails, user experience quality, and domain-specific functional requirements
- LLM-as-judge evals can help cover this broader surface, but must themselves be validated using traditional metrics on labeled datasets
- Human annotation by domain experts is essential for covering evaluation dimensions that automated metrics cannot capture

## Related

- [[summary-20260525 - Does GenAI ＂belong＂ to data scientists — Phil Hetzel, Braintrust]] — source
- [[PhilHetzel]] — presenter who identified this gap
- [[CrossFunctionalAgentTeams]] — diverse teams needed for broad evaluation
- [[HumanAnnotation]] — domain expert evaluation of agent behavior
- [[LLMAsJudge]] — technique for covering broader evaluation surface
- [[EvalFlywheel]] — continuous evaluation loop connecting production to experimentation
