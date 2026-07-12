---
title: "Attack Success Rate (ASR)"
type: concept
tags: [ai-security, metric, adversarial-robustness]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md"]
last_updated: 2026-07-10
---

## Definition

Attack Success Rate (ASR) is the primary metric for measuring adversarial robustness, representing the percentage of attacks that successfully bypass a system's defenses out of the total number attempted.

## Key Information

- If 100 attacks are thrown at a system and only 1 gets through, the ASR is 1% and the system is 99% adversarially robust.
- Sander Schulhoff argues that ASR claims are fundamentally unreliable because the attack space is effectively infinite — testing even millions of attacks is not statistically significant when the total possible attacks is one followed by a million zeros.
- Guardrail companies often claim 99% effectiveness (1% ASR), but 1% of an effectively infinite attack space is still an effectively infinite number of successful attacks.
- The best way to measure ASR is through adaptive evaluation (using attackers that learn and improve), not static datasets of pre-constructed malicious prompts.
- Static evaluations are considered "quite useless" because prompts constructed for earlier models don't fairly test newer models.
- Human attackers consistently achieve very low ASR for defenses (meaning they break through almost everything), confirming that claimed ASR figures from static testing are misleading.

## Related

- [[summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO]] — source summary
- [[Adversarial Robustness]] — the property ASR measures
- [[Adaptive Evaluation]] — the preferred measurement approach
- [[AI Guardrails]] — products that claim low ASR
