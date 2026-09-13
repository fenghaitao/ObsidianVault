---
title: "Model Training"
type: concept
tags: [engineering, ML, Meta, infrastructure]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story).md"]
last_updated: 2026-07-21
---

## Definition

Model Training is the process of teaching machine learning models to recognize patterns by feeding them training data. It was a core part of Evan's work at Meta, where models were trained to detect violating content.

## Key Information

- Model training takes time — Evan would "wake up in the middle of the night being like 'did my run finish?'" because he was excited about the results
- Training on limited data creates overfitting risk: "you train on the couple of examples that you have, and then obviously they were in your training data, so you're overfitting to them"
- The measurement problem: "the fact that you detect them now is not representative of anything, but we don't have any other examples to evaluate ourselves on"
- The feedback loop was critical: once models started detecting more content, they had more training data, which improved the models further
- Evan did "fine-tuning hyperparameters and doing feature engineering" alongside ML PhDs, despite being primarily an infrastructure engineer
- The team did "sophisticated sequencing, temporal modeling" and leveraged core embeddings from Meta's AI org
- The training process was part of the broader experimentation workflow at Meta

## Related

- [[summary-20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story)]] — source summary
- [[Machine Learning]] — the broader field
- [[Experimentation]] — the process that model training feeds into
- [[Feature Engineering]] — creating features for model training
- [[Temporal Modeling]] — a specific modeling approach
