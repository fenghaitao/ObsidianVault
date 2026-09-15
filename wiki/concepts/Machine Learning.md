---
title: "Machine Learning"
type: concept
tags: [engineering, AI, ML, Meta, content-moderation]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story).md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20250421 - Meta Staff Eng (IC6) Promotion by 28 ｜ Rahul Pandey.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20250815 - Meta Senior Manager (M2)： Manager Career Growth, PIPs, Amazon vs Meta ｜ Stefan Mai.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260126 - Ex-Citadel Quant and AI Researcher： Breaking In, Tech vs Finance Careers ｜ Nimit Sohoni.md"]
last_updated: 2026-09-14
---

## Definition

Machine Learning (ML) is a field of artificial intelligence focused on building systems that learn from data. Both Evan and Ryan worked extensively with ML at Meta, though in different contexts — Evan in content moderation and Ryan in infrastructure.

## Key Information

- Evan's team (Content Integrity) built ML models to identify and take action on violating content
- The work involved training models, fine-tuning hyperparameters, doing feature engineering, and running experiments
- The ML workflow at Meta involved: crude quick checks, then expensive models, photo matching, scoring, human review routing, and action
- Evan's breakthrough came from a non-ML insight: incorporating comment signals into models rather than only focusing on pixel and audio analysis
- Evan noted that ML PhDs tend to focus on "how to optimize the model in the most sophisticated technical means possible" — sometimes missing simpler solutions
- Model training takes time, which led to Evan waking up in the middle of the night to check if training runs had finished
- Ryan's ML work was in infrastructure — optimizing compute efficiency for video encoding workloads
- The applied ML work at Meta involved "sophisticated sequencing, temporal modeling" and core embeddings from the AI org

### Stefan Mai's ML Transition
- Stefan moved into ML by reading books, doing Kaggle competitions, and building models on the side
- The fundamentals matter, but the real unlock was the intuition and judgment that only come from building — not treating it as a study session
- ML has "shades of gray": training-pipeline bugs can hide for years and only show up as a marginal perf fix, unlike deterministic SU code

- Nimit Sohoni: transformers store a key-value (KV) cache that grows linearly with sequence length (like a database), while state space models compress context into a fixed-size state (like a brain); hybrid models that interleave both are the cutting edge for open-source text
- Cartesia found SSMs are "almost a free lunch" for audio — better quality and faster inference — because audio frames are low-information and compress well, unlike densely informational text

## Related

- [[summary-20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story)]] — source summary
- [[Content Integrity]] — org that built ML models for content moderation
- [[Model Training]] — the process of training ML models
- [[Feature Engineering]] — creating features for ML models
- [[Temporal Modeling]] — time-based ML modeling approach
- [[summary-20250815 - Meta Senior Manager (M2)： Manager Career Growth, PIPs, Amazon vs Meta ｜ Stefan Mai]] — source summary (ML transition)
- [[Stefan Mai]] — Kaggle and building as the real unlock
- [[Nimit Sohoni]] — SSM vs transformer primer
- [[State Space Models]] — the architecture at issue
- [[Cartesia]] — applies SSMs to audio
- [[summary-20260126 - Ex-Citadel Quant and AI Researcher： Breaking In, Tech vs Finance Careers ｜ Nimit Sohoni]] — source summary
