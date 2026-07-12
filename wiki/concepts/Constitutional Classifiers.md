---
title: "Constitutional Classifiers"
type: concept
tags: [ai-security, defense, anthropic, llm]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md"]
last_updated: 2026-07-10
---

## Definition

Constitutional classifiers are a defense mechanism developed by Anthropic that makes it significantly harder to elicit SEAB burn and other harmful outputs from Claude models by training the model with constitutional principles that define acceptable and unacceptable behavior.

## Key Information

- Anthropic's constitutional classifiers have made it much more difficult to get SEAB burn information (chemical, biological, radiological, nuclear, explosives) out of Claude models compared to earlier versions.
- Despite the improvement, humans can still jailbreak Claude models with constitutional classifiers in under an hour.
- Automated systems can also still defeat constitutional classifiers.
- The way Anthropic reports adversarial robustness for these classifiers still relies heavily on static evaluations (using pre-constructed malicious prompts from earlier models), which Schulhoff considers an unfair comparison.
- Anthropic is noted as doing better than other labs at including human evaluations in their robustness reporting, though there's room for improvement.
- Constitutional classifiers are an example of the frontier labs doing meaningful security research, as opposed to the guardrail products sold by enterprise AI security companies.

## Related

- [[summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO]] — source summary
- [[Anthropic]] — developer of constitutional classifiers
- [[Claude]] — model protected by constitutional classifiers
- [[SEAB Burn]] — category of content these classifiers help block
- [[Adversarial Robustness]] — the property constitutional classifiers aim to improve
