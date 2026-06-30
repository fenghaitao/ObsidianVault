---
title: "ModelAsAPI"
type: concept
tags: [llm, api, genai, data-science, model-providers]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260525 - Does GenAI ＂belong＂ to data scientists — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition

Model-as-API is the observation that frontier LLMs from providers like Anthropic, OpenAI, and Mistral are pre-built, pre-trained, and deployed as endpoints — fundamentally changing the workflow from traditional ML. Instead of building a data pipeline to train a model, teams consume these models as APIs and change their behavior through prompts and context rather than retraining or feature engineering.

## Key Information

- Frontier model providers (Anthropic, OpenAI, Mistral) have already done the data pipeline: gathering data, training the underlying LLM, and deploying it through an endpoint
- The traditional ML workflow (data pipeline → training → testing → deployment) is no longer the primary task for agent builders
- Teams still need to perform evals after implementing those APIs in their products
- Behavior changes come from changing inputs (prompts, context) rather than retraining or feature engineering
- Fine-tuning is described as "pretty rare" — context engineering is the primary lever
- This shift means product engineers (who are skilled at consuming APIs) are natural contributors to agent development
- LLMs are "just APIs" — reaching out to another system based on a payload and bringing information back in a useful way is what product engineers do every day

## Related

- [[summary-20260525 - Does GenAI ＂belong＂ to data scientists — Phil Hetzel, Braintrust]] — source
- [[PhilHetzel]] — presenter
- [[Anthropic]] — model provider
- [[OpenAI]] — model provider
- [[Mistral]] — model provider
- [[ContextEngineering]] — the primary lever for changing model behavior
- [[CrossFunctionalAgentTeams]] — why product engineers belong on agent teams
- [[TraditionalEnterpriseVsAINatives]] — enterprises that haven't adapted to this shift
