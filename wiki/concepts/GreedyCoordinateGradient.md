---
title: "GreedyCoordinateGradient"
type: concept
tags: [security, attack, llm, alignment, adversarial]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero.md"]
last_updated: 2026-06-26
---

## Definition

Greedy Coordinate Gradient (GCG) is an adversarial attack technique that searches for gibberish suffix tokens which, when appended to a harmful query, shift the model's next-token probability distribution out of the refusal region, causing it to begin with a positive affirmation and then auto-complete a harmful response.

## Key Information

- Works by initializing placeholder tokens (e.g., 20 exclamation marks providing sufficient exploratory space) and defining a loss function that maximizes the probability of the model beginning with an affirmative response
- Iterative process: compute loss → compute gradient → select candidate tokens in the direction that minimizes loss → repeat
- Exploits the fact that model alignment is a probabilistic preference, not a hard constraint
- Once the model begins with "Sure, here is how to..." the auto-completion effect forces it to continue providing the harmful information
- Transferable to black-box models: models trained on similar data with similar RL pipelines develop geometrically similar refusal boundaries that can be broken with the same gibberish tokens
- Requires open weights for the gradient search but the discovered tokens transfer to closed models

## Related

- [[summary-20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero]] — source
- [[PromptInjection]] — related attack vector class
- [[Guardrails]] — defensive mechanism
- [[ModelAlignment]] — the probabilistic preference being exploited
