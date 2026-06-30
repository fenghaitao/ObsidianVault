---
title: "CrossFunctionalAgentTeams"
type: concept
tags: [agents, team-composition, organizational-design, genai, collaboration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260525 - Does GenAI ＂belong＂ to data scientists — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition

Cross-functional agent teams are diverse groups that bring together data scientists, product/systems engineers, and non-technical domain experts to build AI agents. Rather than isolating agent development within a single function (typically ML engineering), this approach distributes responsibilities according to each role's strengths: domain experts handle prompts and human annotation, engineers handle API integration and infrastructure, and data scientists provide guardrails and evaluation rigor.

## Key Information

- The ideal mix: domain experts (prompt/context engineering, human annotation) + product/systems engineers (implementation, UX, distributed infrastructure) + data scientists (guardrails, LLM-as-judge validation, fine-tuning)
- Domain experts have the closest proximity to the problem the agent is solving and should control the actual prompts
- Product engineers are already skilled at consuming APIs and integrating them into applications — LLMs are just another API
- Complex distributed agents with supervisor/sub-agent architectures create systems problems suited for engineers, not statisticians
- Data scientists contribute guardrails by understanding LLM limitations at a fundamental level
- Human annotation workflows are critical: non-technical domain experts review agent traces and describe whether and why the agent performed well
- The eval and observability feedback loop (production → experimentation → improvement) is a shared responsibility across the team

## Related

- [[summary-20260525 - Does GenAI ＂belong＂ to data scientists — Phil Hetzel, Braintrust]] — source
- [[PhilHetzel]] — presenter who advocated this approach
- [[AgentEvalBroadness]] — why evaluation requires diverse perspectives
- [[HumanAnnotation]] — the domain expert contribution
- [[DataScientistsAsGuardrails]] — the data scientist contribution
- [[TraditionalEnterpriseVsAINatives]] — contrasting organizational approaches
- [[ModelAsAPI]] — why product engineers belong on the team
