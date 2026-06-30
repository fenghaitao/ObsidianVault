---
title: "Does GenAI ＂belong＂ to data scientists? — Phil Hetzel, Braintrust"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260525 - Does GenAI ＂belong＂ to data scientists — Phil Hetzel, Braintrust.md"
author: "Phil Hetzel"
company: "Braintrust"
date: 2026-05-25
tags: [genai, data-science, agent-teams, cross-functional, evals, organizational-structure, context-engineering]
---

# Does GenAI ＂belong＂ to data scientists? — Phil Hetzel, Braintrust

## Core Thesis

GenAI agents do not exclusively "belong" to data scientists or ML engineers. The model is already built by providers like Anthropic, OpenAI, and Mistral, so the traditional ML pipeline of training and testing is no longer the primary workflow. Instead, behavior is changed via prompts and context engineering rather than feature engineering or retraining. Agent evaluation requires broader functional assessment beyond traditional ML metrics (precision, recall, F1). The ideal approach is a diverse, cross-functional team: data scientists provide guardrails and statistical rigor, product and systems engineers handle API integration and distributed infrastructure, and domain experts contribute prompt/context engineering and human annotation. The answer is in the middle — data scientists add critical value but must bring others into the room.

## Key Points

### Two Organizational Archetypes

- **Traditional Enterprise**: CEO/CIO reads about agents in a magazine, delegates to existing ML/data science platform teams. Because "generative AI has AI in the name," it seems like a natural fit. These teams have existing tooling but may be isolated from the end problem the agent is meant to solve.
- **AI Natives**: Smaller, cross-functional teams with no pre-existing AI/ML platform team. Everyone is agile and cross-functional across product engineering and AI engineering. Each person has closer proximity to the problem the agent is solving.

### The Model Is Already Built

- Anthropic, OpenAI, and Mistral have already done the data pipeline of training the underlying LLM and deploying it through an endpoint.
- The traditional ML workflow (data pipeline → training → testing → deployment) is no longer the primary task for agent builders.
- Teams still need to perform evals after implementing those APIs in their product — that is the key remaining responsibility.

### Behavior Changes via Context, Not Retraining

- Traditional ML: add more data, perform feature engineering, run A/B testing to measure lift.
- GenAI: change the inputs — prompts and context. Fine-tuning is rare. Context engineering replaces feature engineering as the primary lever for changing model behavior.
- This shift brings in people with better understanding of real user behavior and closer proximity to the problem.

### The Case FOR Data Scientists Owning Agents

- Agents use models, and data scientists govern models in most organizations.
- Data scientists have deep knowledge of how neural networks and LLMs work, giving them better appreciation of the risks.
- They bring rigorous processes for pushing models to production and a rigorous testing mindset.

### The Case AGAINST Data Scientists Owning Agents

- The model is already built — no training/testing pipeline needed. An entirely different pipeline.
- Data scientists may obsess over traditional ML metrics (precision, recall, F1) that are too narrow for agent evaluation. Agent evaluation requires assessing functional performance across a much broader surface area.
- LLMs are just APIs — product engineers are very used to consuming APIs and integrating them into applications.
- Complex distributed agents (supervisor with child sub-agents across different infrastructure) create systems problems that may not suit someone with a statistics/math background.
- Non-technical domain experts should control prompts and perform human annotation — they have the most proximity to the problem.

### How Data Scientists Add Value to Agent Development

- **Guardrails**: Data scientists can be "the adult in the room," reminding teams that LLMs just predict token after token — they don't actually "know" anything. Understanding the underlying technology prevents aggressive or naive implementations.
- **LLM-as-Judge validation**: People are tempted to trust LLM-as-judge evals blindly. Data scientists can create labeled datasets and apply traditional recall, precision, and F1 metrics to validate those LLM judges.
- **Fine-tuning**: When an open-source model needs to be fine-tuned for a specific use case, data scientists and ML engineers provide the most technical value.

### The Ideal Team Mix

- **Domain experts (non-technical)**: Human annotation, prompt and context engineering — they have closest proximity to the problem.
- **Product, application, and systems engineers**: Implement requirements into the product, ensure great user experience, handle distributed agent infrastructure.
- **Data scientists**: Guardrails, LLM-as-judge validation, eval and observability pipelines, fine-tuning.
- Everyone contributes to the eval and observability feedback loop connecting production to experimentation.

## Entities

- [[PhilHetzel]] — Solutions engineering lead at Braintrust, presenter
- [[Braintrust]] — Agent quality platform combining evals and observability
- [[SlalomConsulting]] — Consulting firm where Phil led the global Databricks business unit
- [[Anthropic]] — Frontier model provider, already built and deployed LLMs
- [[OpenAI]] — Frontier model provider, already built and deployed LLMs
- [[Mistral]] — Open-source model provider, already built and deployed LLMs
- [[aiDotEngineer]] — Conference hosting the talk

## Concepts

- [[CrossFunctionalAgentTeams]] — Diverse team composition for building agents
- [[AgentEvalBroadness]] — Agent evaluation is broader than traditional ML metrics
- [[HumanAnnotation]] — Non-technical domain experts annotating agent traces
- [[DataScientistsAsGuardrails]] — Data scientists as responsible AI guardians in GenAI
- [[TraditionalEnterpriseVsAINatives]] — Two organizational approaches to agentic development
- [[ModelAsAPI]] — LLMs as pre-built APIs, not models needing training
- [[ContextEngineering]] — Replacing feature engineering as the primary lever for behavior change
- [[LLM-as-Judge]] — Using LLMs to evaluate other LLM outputs; needs data scientist validation
- [[EvalFlywheel]] — The feedback loop connecting production observability to offline experimentation

## Related

- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — earlier talk by the same speaker
- [[Braintrust]] — the company behind this talk
- [[PhilHetzel]] — the presenter
