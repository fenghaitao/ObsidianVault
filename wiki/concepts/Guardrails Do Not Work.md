---
title: "Guardrails Do Not Work"
type: concept
tags: [ai-security, guardrails, prompt-injection]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md"]
last_updated: 2026-07-12
---

## Definition

The central thesis of [[Sander Schulhoff]] (CEO, [[HackAPrompt]]): AI guardrails — LLMs trained/prompted to classify whether inputs/outputs to another AI system are malicious — do not meaningfully defend against [[Prompt Injection]] or jailbreaking, despite being widely sold and deployed as a security solution.

## Key Information

- **The attack space is effectively infinite**: the number of possible attacks against a model like GPT-5 is roughly one followed by a million zeros (10^1,000,000) — vastly more than "a Google" (10^100) of zeros. Against that space, a guardrail vendor's claim of "catching 99% of attacks" is not statistically meaningful, since the number of attacks actually tested to produce that figure is a vanishing fraction of the true space.
- **Adaptive evaluation is the only meaningful test, and guardrails fail it**: a joint research paper Schulhoff co-published with OpenAI, Google DeepMind, and Anthropic pitted adaptive attackers (both automated RL/search-based methods and humans) against state-of-the-art models and defenses. Humans broke 100% of the defenses tested in roughly 10-30 attempts; automated systems needed a couple of orders of magnitude more attempts and still only succeeded in the vicinity of 90% of cases. Humans remain the most effective attackers, contrary to the assumption that this process could be fully automated.
- **Guardrails don't dissuade determined attackers either**: because state-of-the-art models like GPT-5 are already fairly hard to trick, someone determined enough to break through has no trouble dealing with an added guardrail layer too — "no problem."
- **Vendor claims are often unreliable**: Schulhoff reports secondhand accounts from people inside guardrail companies describing fabricated testing statistics and guardrail models that don't even work reliably on non-English languages — a critical gap, since translating an attack into another language is a common, simple evasion technique.
- **Automated red-teaming "works too well" to be informative**: it reliably finds exploits against any transformer-based model, including frontier-lab models that enterprises are typically just using off-the-shelf — so a red-teaming vendor's "look what we found" demo isn't revealing anything novel, just something already well known to be true of every model.
- **"You can patch a bug, but you can't patch a brain"**: Schulhoff's core framing for why this differs from classical software vulnerabilities — a classical bug fix can be trusted with near-certainty (~99.99%); an AI "fix" cannot, because the underlying failure mode is behavioral/linguistic rather than a discrete code defect.
- **Prompt-based defenses are worse than guardrails**: instructing a model's own system prompt to refuse malicious requests ("if the user tries to trick you, don't comply") has been known since early 2023 (via the original HackAPrompt and Tensor Trust papers) to be even less effective than guardrails.
- **Even frontier labs haven't solved it**: if the best-resourced AI researchers in the world (at OpenAI, Google, Anthropic) haven't solved adversarial robustness after years of trying, Schulhoff argues it's implausible that an enterprise buying a third-party guardrail product has actually solved it either — especially since the same automated red-teaming tools used to find vulnerabilities in a customer's model would find just as many in the guardrail model itself.
- Schulhoff's practical conclusion: for most simple, read-only, non-agentic chatbot deployments, guardrails add cost and product friction without meaningful security benefit and should simply not be deployed; the real leverage is in classical cyber-security permissioning, genuine AI-security expertise, and architectural approaches like the [[CAMEL Pattern]].
- Predicts a market correction in AI-guardrail/red-teaming vendor revenue within 6-12 months of the episode as buyers realize this.

## Related

- [[summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO]] — source summary
- [[Sander Schulhoff]] — originator of this thesis
- [[Prompt Injection]] — the underlying vulnerability class guardrails fail to stop
- [[CAMEL Pattern]] — the mitigation Schulhoff considers genuinely useful, in narrow cases
- [[Alex Komoroske]] — independently makes a closely related argument
