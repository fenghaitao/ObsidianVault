---
title: "Topic Modeling for Agents"
type: concept
category: methodology
tags: [topic-modeling, clustering, agent-traces, observability, embeddings, production-monitoring]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition

Topic modeling for agents is an automated technique that runs lightweight LLMs on incoming agent traces to perform embedding and clustering, surfacing patterns in how users interact with agents. It reveals user intent, sentiment, and common failure modes without requiring manual trace review, shortening the iteration loop between detecting a problem in production and running an experiment to fix it.

## Key Information

- Braintrust rolled out this feature approximately one month before the May 2026 talk
- A lightweight LLM processes incoming observability traces to generate embeddings
- Clustering is then performed on those embeddings to group similar traces
- Surfaces three key insights:
  - **User intent**: What are people actually using the agent for?
  - **Sentiment**: How are people feeling about interacting with the agent?
  - **Issues**: What problems are users running into?
- Goal: shorten the iteration loop between detecting a production problem and running an experiment to fix it
- Addresses the "unknown unknowns" — problems you don't know to look for, surfaced automatically rather than requiring manual discovery
- Complements human annotation by handling scale: humans review a sample, topic modeling covers the full production volume
- Represents the frontier of agent observability — moving from reactive trace inspection to proactive pattern discovery

## Related

- [[summary-20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust]] — source
- [[AgentObservability]] — the observability paradigm this technique advances
- [[Braintrust]] — platform that implemented topic modeling
- [[HumanAnnotation]] — complementary approach at smaller scale
- [[AgentTraceData]] — the data source for topic modeling
- [[EvalFlywheel]] — the feedback loop topic modeling accelerates
