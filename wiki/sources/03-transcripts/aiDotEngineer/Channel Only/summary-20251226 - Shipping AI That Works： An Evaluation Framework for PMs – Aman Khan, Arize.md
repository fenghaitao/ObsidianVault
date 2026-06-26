---
title: "Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md"
date: 2025-12-26
speaker: Aman Khan
organization: Arize
tags: [eval, llm, ai-pm, evaluation-framework, observability, agent-evaluation]
---

## Core Thesis

Aman Khan presents an evaluation framework for AI product managers, arguing that LLM evals are essential for shipping reliable AI products and should replace traditional PRDs as the new form of product requirements. He demonstrates moving from "vibe coding" to "thrive coding" using data-driven evaluation with human labels to validate LLM judges, and positions evals as a moat for AI startups.

## Key Takeaways

1. **LLMs hallucinate by design** — both OpenAI and Anthropic CPOs publicly state their models hallucinate and that writing evals is essential. When the people selling the product tell you it's unreliable, you should listen.

2. **Evals vs. software testing** — LLM agents are nondeterministic (unlike deterministic software tests), rely on your data rather than existing codebases, and can be manipulated. You actually want some hallucination, just in the right way.

3. **LLM-as-Judge structure** — An eval consists of: role (task definition), context (text to evaluate), goal (what to determine), and terminology/labels (text labels mapped to scores, not raw numeric scores — LLMs are bad at numbers).

4. **From Vibe Coding to Thrive Coding** — Instead of evaluating AI outputs by gut feel ("looks good to me"), use data-driven evaluation to build confidence in outputs.

5. **Evals as the new requirements** — Instead of handing engineers a PRD, give them an eval dataset and eval criteria as acceptance criteria.

6. **Evals need evals** — LLM-as-judge systems must be validated against human labels. The speaker demonstrated that his friendly/robotic eval had near-zero agreement with human labels, showing the need for iterative improvement.

7. **Agent visualization matters for PMs** — Being able to see what the agent system looks like (traces, spans, parallel calls) gives PMs leverage to ask better questions of engineering teams.

8. **Development-to-production loop** — Start with small datasets in development, curate hard examples, iterate until team confidence is high, then ship to production and repeat with production data.

## Entities Referenced

- [[AmanKhan]] — AI product manager at Arize
- [[Arize]] — AI observability and evaluation platform
- [[OpenAI]] — LLM provider; CPO Kevin Weil stated models hallucinate
- [[Anthropic]] — LLM provider; CPO Mike Krieger stated models hallucinate
- [[Waymo]] — Self-driving car company; real-world AI example
- [[Cruise]] — Self-driving car company where Aman Khan previously worked
- [[Spotify]] — Arize customer; Aman Khan previously worked on ML platform there
- [[Uber]] — Arize customer
- [[Instacart]] — Arize customer
- [[Reddit]] — Arize customer
- [[Duolingo]] — Arize customer
- [[LangGraph]] — Agent framework used in the demo
- [[CrewAI]] — Multi-agent framework mentioned as alternative
- [[Phoenix]] — Open-source version of Arize
- [[LennyPodcast]] — Lenny's Podcast; Aman Khan collaborates on AI PM educational content
- [[Datadog]] — Investor in Arize (Series C)
- [[Microsoft]] — Investor in Arize (Series C)
- [[Cursor]] — AI code editor used to build the demo agent
- [[GregBrockman]] — OpenAI co-founder who emphasized eval importance

## Concepts Referenced

- [[LLM-as-Judge]] — Core evaluation technique: using an LLM to classify and explain outputs
- [[EvalEngineering]] — Practice of crafting high-quality eval prompts; demonstrated by iterating on eval prompts
- [[VibeCoding]] — Building by gut feel without systematic evaluation
- [[ThriveCoding]] — Data-driven development with evals for confidence
- [[AIPM]] — AI Product Manager; emerging role with higher expectations
- [[EvalAsRequirements]] — Using eval datasets as product requirements instead of PRDs
- [[AgentVisualization]] — Visual representation of agent traces and spans for debugging
- [[TracesAndSpans]] — Observability primitives: traces (input/output/metadata) and spans (units of work)
- [[HumanInTheLoopEvaluation]] — Validating LLM judges against human labels
- [[PromptPlayground]] — Interface for iterating on prompts with production data
- [[FewShotExamples]] — Providing examples in eval prompts to improve classification accuracy
- [[TemperatureInAI]] — Parameter to reduce variance in LLM judge outputs
- [[MultiAgentArchitecture]] — Multiple specialized agents feeding into a summarization agent

## Related

- [[summary-20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize]] — earlier Arize talk on prompt learning
