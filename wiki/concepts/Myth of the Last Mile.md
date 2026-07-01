---
title: "Myth of the Last Mile"
type: concept
tags: [production, mvp, enterprise-ai, reinforcement-learning, model-deployment]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML.md"]
last_updated: 2026-06-30
---

## Definition
The myth of the last mile is the false belief that the hard part of bringing an AI solution to production is getting to an MVP or demo, and that production deployment is just the final, easy polish step. In reality, the MVP is just the first mile — the real marathon is the continuous, systematic improvement required to go from MVP to production and beyond.

## Key Information
- **Origin**: Alessandro Cappelli, co-founder of Adaptive ML
- **The false narrative**: Build an MVP that looks nice in front of stakeholders, then just handle the "last mile" to production
- **Why it's a myth**: Most MVPs are built on proprietary models (only system prompt changes possible) or open-source models with instruction fine-tuning (requires expensive new datasets for each iteration). Neither provides a systematic, mathematical way to improve.
- **The reality**: Getting to MVP is the first mile. The real marathon — getting from MVP to production and beyond — requires continuous retraining, refinement, and improvement driven by real client feedback, business metrics, and environmental reward
- **Solution**: Reinforcement learning provides the systematic improvement mechanism that bridges MVP to production
- **Statistic cited**: 95% of GenAI pilots fail to reach production

## Related
- [[ReinforcementLearningWithLLMs]] — the solution to the myth
- [[Continuous Model Improvement]] — the actual requirement for production
- [[Instruction FineTuning vs RL]] — why instruction fine-tuning alone can't solve the problem
- [[Tokenomics]] — the cost economics that become apparent only at production scale
- [[summary-20260512 - Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML]] — source
