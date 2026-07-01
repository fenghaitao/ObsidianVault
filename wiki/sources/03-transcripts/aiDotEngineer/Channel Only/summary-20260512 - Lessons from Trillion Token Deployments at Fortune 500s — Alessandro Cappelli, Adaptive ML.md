---
title: "Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML.md"
date: 2026-05-12
ingested: 2026-06-30
tags: [reinforcement-learning, rl-ops, enterprise-ai, model-production, agent-training, tokenomics, post-training, adaptive-ml, fortune-500]
---

## Core Thesis
Alessandro Cappelli, co-founder and chief customer officer at Adaptive ML, argues that reinforcement learning (RL) is not just another post-training algorithm — it is the essential algorithm for systematically and industrially bringing LLMs to production at enterprise scale. 95% of GenAI pilots fail to reach production because of the "myth of the last mile" — the false belief that getting to an MVP is the hard part and production is just a final polish step. In reality, the real marathon is going from MVP to production and beyond, which requires continuous improvement driven by real client feedback, business metrics, and environmental reward. RL uniquely enables this in a mathematical, systematic way. RL is disproportionately more effective than instruction fine-tuning and prompting, enabling smaller, cheaper, faster models that make enterprise tokenomics viable while also granting data ownership. In the era of agents, RL's advantages only widen because agents require more tokens, more complexity, and higher reliability standards.

## Key Topics
- **The Myth of the Last Mile**: The false belief that getting to an MVP/demo is the hard part and production is just the final mile. In reality, MVP is just the first mile. The real marathon is getting from MVP to production and beyond, which requires continuous improvement from real feedback. Most MVPs are built on proprietary models (where you can only change system prompts) or open-source models with instruction fine-tuning (where you must create expensive new datasets repeatedly). Neither approach provides a scientific, systematic way to improve.
- **RL as the Production Algorithm**: Reinforcement learning, by design and nature, allows integrating feedback in an almost mathematical way. It's not just another post-training technique — it's the one algorithm that industrializes bringing models to production. RL enables continuous retraining, refinement, and improvement driven by real client feedback, business metrics, and environmental reward.
- **RL's Outsized Performance**: Compared to prompting and instruction fine-tuning, RL is disproportionately more effective. You can get the same performance with RL as with SFT using a much smaller model. This unlocks: (1) cheaper serving at scale (enterprise tokenomics), (2) faster inference (critical for latency-constrained use cases like speech-to-speech), and (3) data/solution ownership (model is trained on your business data, no worry about upstream model updates shifting performance).
- **AT&T Case Study**: AT&T summarizes every customer-agent transcript. Just summarization costs millions of dollars at scale with large proprietary models. Training a smaller RL-optimized model dramatically reduces cost.
- **Manulife Case Study**: Manulife already had agents in production. Adaptive ML could directly plug a trained model into the existing agent workflow without recreating it.
- **CCS Case Study**: A medical supply company with a customer support system. The reward signal is containment rate — what percentage of calls are handled end-to-end by the model. This KPI can be directly maximized via RL. Real conversations (people in panic, needing escalation to 911) can be used to train mock users for realistic agent training.
- **Agents Amplify RL's Advantage**: Agents require more tokens, more complexity, and less room for errors (they access databases and change things). This raises the standard for production and makes tokenomics even more critical. RL was originally designed to train robots/agents in environments, so it naturally fits agent training. Agent training data doesn't exist in the wild — there's no scrapable data of agents using tools — but RL environments produce it as a byproduct.
- **Synthetic Data via RL Environments**: When you have an RL environment with a reward signal, you automatically create a synthetic data pipeline. As the agent explores, the reward tells you what's good and what's not. You can do rejection sampling to create a dataset to bootstrap the first model training. Companies can also leverage existing data (e.g., real customer-agent transcripts) to train mock users that simulate realistic, difficult customers.
- **Where Is the Human in the Loop?**: RLHF made RL famous, but the "human" often hides expensive, tedious annotation campaigns. In Cappelli's approach, the human defines rubrics, system prompts for LLM-as-judge evaluators, and scenarios — taking minutes to hours, not weeks, and not iteratively dozens of times. The reward signal comes from multiple sources: systematic rewards (does code run? is syntax correct?), direct KPIs/business outcomes (containment rate), and LLMs-as-judges (tone, business guideline compliance).
- **Reward Signal Scaling**: Early on, with limited feedback (10-20 data points), use the feedback to improve LLM-as-judge prompts. At production scale with thousands of feedbacks, train dedicated reward models to scale the human feedback signal efficiently.
- **Adaptive Engine**: Adaptive ML's RL Ops platform — an holistic platform to observe, train, and serve at once. It abstracts the complexity of RL (e.g., PPO requires orchestrating 4 LLMs simultaneously) by exposing pre-built recipes. Works on top of open-source models (Gemma, Mistral, Qwen, etc.).
- **RL Is Hard**: The only catch — RL is genuinely difficult. PPO requires orchestrating four large language models simultaneously. This is where platforms like Adaptive Engine provide value by handling the infrastructure complexity.

## Entities
- [[Adaptive ML]] — RL Ops platform company, builds the Adaptive Engine
- [[Alessandro Cappelli]] — co-founder and chief customer officer at Adaptive ML, previously on the Falcon training team
- [[AT&T]] — enterprise customer, summarization use case at millions-of-dollars scale
- [[Manulife]] — enterprise customer, agent workflow integration use case
- [[CCS]] — medical supply company customer, customer support with containment rate optimization
- [[Falcon (LLM)]] — open-source model, Alessandro was on the team that trained it ~3 years ago
- [[aiDotEngineer]] — conference where talk was presented
- [[OpenAI]] — Frontier lab, ChatGPT and RLHF origin
- [[Anthropic]] — Frontier lab mentioned for Sonnet comparison

## Concepts
- [[Myth of the Last Mile]] — the false belief that MVP is the hard part; production is the real marathon
- [[Tokenomics]] — cost economics of serving LLMs at enterprise scale; smaller RL-optimized models make the numbers work
- [[RL Ops]] — reinforcement learning operations platform for evaluating, tuning, and serving LLMs
- [[Model Ownership]] — owning your trained model, data, and solution; no dependency on upstream model updates
- [[Reward Signal]] — systematic, KPI-based, or LLM-as-judge rewards that drive RL training
- [[Rejection Sampling for Bootstrapping]] — using RL environment trajectories to create synthetic training datasets
- [[Mock User]] — using LLMs to simulate realistic users (including difficult ones) for agent training environments
- [[Environment for RL Training]] — mock tools and users that create the training loop for RL-based agent development
- [[Continuous Model Improvement]] — ongoing retraining and refinement driven by real feedback from production
- [[Instruction FineTuning vs RL]] — comparison of post-training techniques; RL is disproportionately more effective
- [[Agent Tokenomics]] — the heightened economic challenge of agents at scale (10x tokens vs summarization)
- [[Model Lifecycle Acceleration]] — speeding up the evaluate-train-serve cycle through holistic RL platforms
- [[ReinforcementLearningWithLLMs]] — RL combined with LLMs for post-training
- [[LLMAsJudge]] — using LLMs to evaluate model outputs as part of the reward signal
- [[Synthetic Data Generation]] — creating training data from RL environment trajectories

## Related
- [[summary-20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench]] — model evaluation and LLM-as-judge
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — agent optimization with feedback loops
- [[summary-20260510 - Feedback Loops are All You Need — Mehedi Hassan, Granola]] — feedback loops for improvement
- [[summary-20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI]] — small model training
- [[summary-20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora]] — agent complexity beyond chat
- [[summary-20240719 - Lessons From A Year Building With LLMs]] — LLM production lessons and LLM-as-judge trade-offs
