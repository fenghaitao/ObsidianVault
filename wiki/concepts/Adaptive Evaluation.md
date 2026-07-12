---
title: "Adaptive Evaluation"
type: concept
tags: [ai-security, evaluation, research, methodology]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md"]
last_updated: 2026-07-10
---

## Definition

Adaptive evaluation is a method of measuring adversarial robustness where the attacker can learn over time and improve their attacks based on what works against a specific defense, rather than using a static set of pre-constructed prompts.

## Key Information

- Considered the best measurement approach for adversarial robustness, as opposed to static evaluations using pre-constructed datasets of malicious prompts.
- Humans are the best adaptive attackers because they test, observe what works, and iteratively refine their approach.
- In HackAPrompt's research, human attackers break 100% of defenses in 10-30 attempts, while automated adaptive systems require orders of magnitude more attempts.
- Static evaluations are "quite useless" because they use prompts constructed for earlier models — a new model wasn't built to defend against those specific prompts, making the comparison unfair.
- The HackAPrompt paper co-authored with OpenAI, Google DeepMind, and Anthropic extensively studied adaptive attacks using RL, search-based methods, and human attackers against state-of-the-art models including GPT-5.
- Sander Schulhoff recommends frontier labs shift focus from static datasets to adaptive evaluations that include human evals.

## Related

- [[summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO]] — source summary
- [[Adversarial Robustness]] — what adaptive evaluation measures
- [[Attack Success Rate (ASR)]] — the metric produced by evaluation
- [[HackAPrompt]] — organization conducting adaptive evaluations
