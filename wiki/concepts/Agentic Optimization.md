---
title: "Agentic Optimization"
type: concept
tags: [optimization, agents, self-improving, autonomous, gepa]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md"]
last_updated: 2026-06-29
---

## Definition
Agentic Optimization is the use of an AI agent (the proposer agent) to generate and refine the configuration of another AI agent, creating a meta-optimization loop. In GEPA, a Pydantic AI agent proposes new prompts to optimize another Pydantic AI agent.

## Key Information
- **Meta-agent pattern**: One agent (the proposer) optimizes another agent (the task agent)
- **GEPA implementation**: A Pydantic AI agent serves as the proposer, receiving context about past performance and generating new prompt candidates
- **Proposer prompt engineering**: The proposer agent itself has a prompt that can be optimized — leading to infinite regress ("optimizing the prompt of optimizing the prompt")
- **Self-driving vision**: The end goal is for the platform to autonomously run the optimization loop without human intervention
- **Colvin's assessment**: While state-of-the-art, the technique is "not actually that groundbreaking" — it's a relatively crude sense of "ask an agent to generate a new prompt, if it does better, take bits of that, put it into a new prompt, keep doing that"
- **Complexity perception**: People love to say AI is incredibly sophisticated, but this optimization technique is relatively simple compared to the complexity of the models themselves
- **Managed variables integration**: The vision is to wire agentic optimization directly into managed variables for continuous autonomous improvement

## Related
- [[Agent Optimization]] — the broader optimization process
- [[GEPA]] — the algorithm enabling agentic optimization
- [[Self-Improving Agents]] — related concept of agents improving themselves
- [[Managed Variables]] — deployment mechanism
- [[Pareto Frontier]] — selection strategy
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — source
