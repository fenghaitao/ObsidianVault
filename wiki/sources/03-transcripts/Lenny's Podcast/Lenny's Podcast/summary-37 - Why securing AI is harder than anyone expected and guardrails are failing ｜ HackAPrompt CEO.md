---
title: "summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO"
type: source
tags: [source, podcast, transcript, ai-security, adversarial-robustness]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md"]
last_updated: 2026-07-10
---

## Core Summary

Sander Schulhoff, a leading AI red teaming researcher and CEO of HackAPrompt, argues that AI guardrails fundamentally do not work against prompt injection and jailbreaking attacks. The search space of possible attacks is effectively infinite, and current defenses are trivially bypassed by determined human attackers. The only reason there hasn't been a massive AI security breach is the early stage of adoption, not the effectiveness of security measures. As AI agents gain more power to take real-world actions, the risks become severe, and the solution lies at the intersection of classical cybersecurity (proper permissioning, data access controls) and AI expertise, rather than in guardrail products.

## Key Points

- AI guardrails are large language models that classify inputs/outputs as malicious or benign, but they are trivially defeated by human attackers (often in 10-30 attempts) and do not meaningfully dissuade attacks.
- The number of possible attacks against an LLM is essentially infinite (one followed by a million zeros for GPT-5), making any claimed 99% effectiveness rate statistically meaningless.
- Automated red teaming always finds vulnerabilities in any transformer-based system, so its results are not novel or useful for most enterprises who use off-the-shelf models.
- The distinction: jailbreaking is a direct user-to-model attack, while prompt injection involves a malicious user, a model, and a developer's system prompt that the user tries to override.
- Real-world damage has already occurred: ServiceNow's Assist AI was tricked into performing CRUD database operations and sending external emails; Comet browser leaked user data via malicious webpage text.
- The Camel framework from Google offers a promising defense by pre-restricting agent permissions based on what the user's prompt actually requires, though it doesn't help when both read and write permissions are needed.
- "You can patch a bug, but you can't patch a brain" — AI security is fundamentally different from classical cybersecurity because fixing one vulnerability doesn't eliminate the class of attack.
- The most valuable security professionals of the future will sit at the intersection of classical cybersecurity and AI security, understanding both permissioning and model behavior.
- Sander predicts a market correction in the AI guardrail industry within 6-12 months as companies realize these products don't deliver meaningful protection.
- For simple chatbots with no real-world actions, the risk is minimal since users can only harm themselves; the danger escalates dramatically with agents, AI-powered browsers, and LLM-powered robots.

## Related

- [[Sander Schulhoff]] — guest, AI security researcher
- [[HackAPrompt]] — organization running AI red teaming competitions
- [[Adversarial Robustness]] — core concept
- [[Prompt Injection]] — attack vector
- [[Jailbreaking (AI)]] — attack vector
- [[AI Guardrails]] — proposed defense
- [[Camel (framework)]] — Google's permissioning defense
