---
title: "Reward Signal"
type: concept
tags: [reinforcement-learning, evaluation, llm-as-judge, kpi, model-training]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML.md"]
last_updated: 2026-06-30
---

## Definition
A reward signal in reinforcement learning for LLMs is the feedback mechanism that tells the model what constitutes good behavior. It can come from systematic rewards (does code run?), direct KPIs (containment rate), or LLM-as-judge evaluators (tone, business guideline compliance). The reward signal is the most critical component of RL training — without it, there is no training signal.

## Key Information
- **Three sources**: (1) Systematic rewards — verifiable, deterministic checks (code execution, syntax correctness), (2) Direct KPIs and business outcomes — measurable metrics like containment rate, (3) LLMs-as-judges — for open-ended qualities like tone, vocabulary, and business guideline adherence
- **Human role**: Humans define the rubrics, system prompts for LLM judges, and evaluation scenarios — taking minutes to hours, not weeks of annotation campaigns
- **Scaling strategy**: Early stage (10-20 feedbacks) — use feedback to improve LLM-as-judge prompts. Production stage (thousands of feedbacks) — train dedicated reward models from the accumulated data
- **Reward model training**: At scale, accumulated human feedback data is used to train reward models that can score outputs automatically, scaling the human feedback signal
- **RLHF distinction**: Traditional RLHF often hides expensive annotation campaigns; the reward signal approach aims to minimize human annotation burden

## Related
- [[ReinforcementLearningWithLLMs]] — the technique that depends on reward signals
- [[LLMAsJudge]] — one source of reward signals
- [[CCS]] — containment rate as a KPI-based reward signal
- [[Mock User]] — used to create environments where rewards can be evaluated
- [[summary-20260512 - Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML]] — source
