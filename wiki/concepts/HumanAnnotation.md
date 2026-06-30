---
title: "HumanAnnotation"
type: concept
tags: [evals, agents, human-in-the-loop, domain-expertise, annotation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260525 - Does GenAI ＂belong＂ to data scientists — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition

Human annotation is the practice of having non-technical domain experts review agent traces and describe whether and why the agent performed well or poorly. It is a critical component of agent evaluation that captures functional and domain-specific quality dimensions automated metrics cannot assess.

## Key Information

- Domain experts (subject matter experts, product managers) have the closest proximity to the problem the agent is solving
- These non-technical people can look into an agent trace and describe whether the agent is performing well and, most importantly, why
- Human annotation is part of a larger feedback workflow that feeds into the eval and observability loop
- It enables organizations to bring non-technical stakeholders into the agent development process rather than isolating it within engineering teams
- Combined with LLM-as-judge and traditional metrics, human annotation provides the ground truth for validating automated evaluation approaches
- Braintrust's platform includes a human labeling component to facilitate this workflow

## Related

- [[summary-20260525 - Does GenAI ＂belong＂ to data scientists — Phil Hetzel, Braintrust]] — source
- [[PhilHetzel]] — presenter
- [[Braintrust]] — platform with human labeling component
- [[CrossFunctionalAgentTeams]] — team structure that includes domain experts for annotation
- [[AgentEvalBroadness]] — why human annotation is needed beyond automated metrics
- [[EvalFlywheel]] — the continuous loop human annotation feeds into
- [[LLM-as-Judge]] — automated evaluation validated by human annotation
