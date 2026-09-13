---
title: "Experimentation"
type: concept
tags: [engineering, ML, Meta, product-development]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story).md"]
last_updated: 2026-07-21
---

## Definition

Experimentation is the practice of running controlled tests (A/B tests, model experiments) to measure the impact of changes. It was central to Evan's work at Meta, where the Content Integrity team used experimentation to evaluate different models, thresholds, and detection strategies.

## Key Information

- Evan's first project (Estuary) was designed to enable experimentation: "plugging in different models, changing thresholds, running A/B tests"
- The experimentation workflow: train a model, run an experiment, check metrics, iterate
- Evan would wake up in the middle of the night to check if model training runs had finished
- The downside of a purely experimental approach: "it was easy to kind of experiment, see numbers go up... and if they went up, success"
- This led to a lack of deep understanding — knowing that something worked without knowing why
- The Golden Set Recall system was built to solve the experimentation measurement problem for rare events
- The balance: experimentation is essential for measuring impact, but should be paired with curiosity about underlying causes

## Related

- [[summary-20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story)]] — source summary
- [[Machine Learning]] — the domain where experimentation is central
- [[Model Training]] — the process of training models for experiments
- [[Golden Set Recall]] — evaluation system for experimentation
