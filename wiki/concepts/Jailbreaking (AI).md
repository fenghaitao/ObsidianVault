---
title: "Jailbreaking (AI)"
type: concept
tags: [ai-security, attack-vector, llm]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md"]
last_updated: 2026-07-10
---

## Definition

Jailbreaking in AI security refers to the act of tricking a large language model into outputting malicious or restricted information (such as hate speech, bomb-making instructions, or SEAB burn content) when the model is directly interacting with the user without a developer's system prompt in between.

## Key Information

- Differs from prompt injection: jailbreaking is just the user and the model, with no developer system prompt to override. Prompt injection adds a third party (the developer's instructions).
- The Vegas Cybertruck bombing incident is cited as a potential example: the perpetrator used ChatGPT to plan the bombing, possibly by framing it as "an experiment."
- Jailbreaking has been demonstrated against LLM-powered robotic systems, where someone could trick a robot into physically harming a person.
- Human attackers can jailbreak even the most state-of-the-art models (including GPT-5) in 10-30 attempts.
- Automated jailbreaking systems require orders of magnitude more attempts than humans but can still succeed ~90% of the time on average.
- Despite improvements like Anthropic's constitutional classifiers, humans can still jailbreak the best-defended models in under an hour.
- Sander Schulhoff advises against writing jailbreak papers or doing offensive adversarial research, as it's well-established that models can be broken and new papers only provide more attack vectors.

## Related

- [[summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO]] — source summary
- [[Prompt Injection]] — related but distinct attack vector
- [[Adversarial Robustness]] — the defense metric
- [[SEAB Burn]] — category of restricted content often targeted by jailbreaks
