---
title: "Adversarial Robustness"
type: concept
tags: [ai-security, ml, defense, research]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md"]
last_updated: 2026-07-10
---

## Definition

Adversarial robustness refers to how well AI models or systems can defend themselves against adversarial attacks such as prompt injection and jailbreaking. It is a measure of a system's resistance to being tricked into producing malicious outputs.

## Key Information

- The term has been used in ML research for 20-50 years, originally applied to image classifiers, but now extends to LLMs and AI agents.
- Attack Success Rate (ASR) is the primary metric: if 100 attacks are thrown and 1 gets through, the ASR is 1% and the system is 99% adversarially robust.
- Measuring adversarial robustness is extremely difficult because the search space of possible attacks is effectively infinite — for GPT-5, the number of possible attacks is one followed by a million zeros.
- The best measurement approach is adaptive evaluation, where an attacker learns over time and improves their attacks. Humans are the best adaptive attackers.
- Sander Schulhoff argues that no meaningful progress has been made toward solving adversarial robustness in the last couple of years since the problem was discovered for LLMs.
- All currently deployed transformer-based chatbots are vulnerable to adversarial attacks, and automated red teaming always finds vulnerabilities.
- "You can patch a bug, but you can't patch a brain" — unlike classical software bugs, fixing one adversarial vulnerability doesn't eliminate the class of attack.

## Related

- [[summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO]] — source summary
- [[Prompt Injection]] — attack vector
- [[Jailbreaking (AI)]] — attack vector
- [[AI Guardrails]] — proposed defense
- [[Attack Success Rate (ASR)]] — measurement metric
- [[Adaptive Evaluation]] — measurement approach
