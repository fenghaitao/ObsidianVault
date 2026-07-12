---
title: "Adversarial Training"
type: concept
tags: [ai-security, ml, training, defense]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md"]
last_updated: 2026-07-10
---

## Definition

Adversarial training is a defense technique where an AI model is trained to resist adversarial attacks by being exposed to adversarial examples during the training process, potentially making it more robust against prompt injection and jailbreaking.

## Key Information

- Sander Schulhoff and other experts have discussed the idea of doing adversarial training earlier in the pre-training stack — when the AI is "a very small baby" — so it grows up more robust.
- The analogy used: like an orphan having a hard life and growing up tough and street-smart, not easily tricked.
- There is a concern that adversarial training could "turn the AI crazy" or make it angry and malicious.
- No significant deployment of adversarial training at scale has been observed yet, and no meaningful progress has been made in solving adversarial robustness through this approach.
- Schulhoff considers adversarial training deeper in the stack as somewhat promising but unproven.
- There is also a hypothesis that as AI capabilities improve, adversarial robustness will improve as a byproduct — but this hasn't been observed yet; humans can still jailbreak state-of-the-art models in under an hour.

## Related

- [[summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO]] — source summary
- [[Adversarial Robustness]] — the property adversarial training aims to improve
- [[Constitutional Classifiers]] — Anthropic's alternative defense approach
