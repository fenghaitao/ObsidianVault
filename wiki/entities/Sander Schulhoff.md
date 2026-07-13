---
title: "Sander Schulhoff"
type: entity
tags: [person, ai-security, red-teaming]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md"]
last_updated: 2026-07-12
---

## Definition

Sander Schulhoff is CEO of [[HackAPrompt]] and [[Learn Prompting]], a leading AI red-teaming/adversarial-robustness researcher, and a two-time [[Lenny's Podcast]] guest (episode 17 and, as the dedicated subject, episode 37). [[Simon Willison]] and [[Lenny Rachitsky]] cite his view that [[Prompt Injection]] will never be fully solved, since a sufficiently motivated attacker can always eventually find a working exploit even against a ~97%-effective filter.

## Key Information

- Also recommended the "[[CAMEL Pattern]]" (Google DeepMind's privileged/quarantined agent split) as the best available mitigation — the same conclusion Willison independently reached.
- AI researcher for roughly seven years; wrote the first public guide on prompt engineering (Learn Prompting) shortly before ChatGPT's release, now taught to millions. Founded and runs [[HackAPrompt]], the first and largest AI red-teaming competition (sponsored by OpenAI, Scale, Hugging Face, and ~10 other AI companies), which produced the first and largest open-source dataset of prompt injections; the associated paper won Best Theme Paper at EMNLP 2023 out of ~20,000 submissions and is now used by every frontier lab and most Fortune 500 companies to benchmark AI security.
- Central thesis of episode 37: "[[Guardrails Do Not Work]]." Guardrail vendors' "we catch 99% of attacks" claims are statistically meaningless against an effectively infinite attack space (~10^1,000,000 possible prompts for a model like GPT-5); a joint research paper he co-published with OpenAI, Google DeepMind, and Anthropic found adaptive human attackers break every state-of-the-art guardrail tested in 10-30 attempts, while automated attack methods need orders of magnitude more attempts and still only succeed ~90% of the time.
- Coined/popularized "you can patch a bug, but you can't patch a brain" — unlike a classical software bug, a "fixed" model vulnerability can rarely be trusted to actually be gone, since the failure mode is linguistic/behavioral rather than a discrete code defect.
- Distinguishes jailbreaking (malicious user directly tricking a model, no system prompt to bypass) from prompt injection (a user trying to override a developer's system prompt) from indirect/second-order prompt injection (malicious instructions embedded in external content — like an email or web page — that an agent reads and then acts on, without the end user doing anything malicious themselves).
- Walks through concrete incidents: ServiceNow's "Now Assist" agent tricked into recruiting more-privileged internal agents to perform unauthorized database writes and email exfiltration, despite an active prompt-injection-protection feature; a Comet-browser bug where a malicious web page tricked the AI browser into leaking the logged-in user's account data; a [[Claude Code]]-orchestrated cyberattack that bypassed defenses by splitting a malicious request across separate, individually-innocuous-looking agent sessions; and older cases (remotely.io's Twitter chatbot tricked into threatening the president; MathGPT tricked into exfiltrating its own OpenAI API key).
- Practical recommendations for companies: simple read-only/no-action chatbots usually need no additional defense at all (an attacker could get the same output directly from ChatGPT/Claude/Gemini); get classical cyber-security data/action permissioning right so an agent can only ever damage the user interacting with it, never others; hire or contract a genuine AI-security researcher (an underserved intersection of classical cyber security and AI research); skip blanket guardrail/automated-red-teaming products, which add product friction without meaningful security benefit; and invest in team education/awareness, which he considers the single highest-leverage lever available today.
- Predicts a market correction in AI-guardrail/red-teaming vendor revenue within 6-12 months of the episode, alongside the first genuinely damaging, publicly visible AI-agent security incidents.
- Runs a research-incubator-adjacent involvement with [[MATS]] (ML Alignment & Theory Scholars), and connects his industry findings to the broader AI-safety subfield of "control" — how to safely operate a potentially malicious/misaligned AI ("a god in a box that's angry").
- Advises against publishing new offensive jailbreak/attack research for its own sake ("don't write that jailbreak paper") — the field already knows models can be broken in a near-infinite number of ways, so further such research mostly just hands attackers new techniques without materially improving defenses.
- Recommends [[Trustable]] and [[Repello]] as companies doing comparatively strong work in AI governance/compliance and applied AI-security tooling, respectively.
- Teaches an AI-security/red-teaming course (with Learn Prompting and HackAPrompt staff) on Maven, at hackai.co.
- Found on Twitter/X as @SanderSchulhoff (or close misspellings).

## Related

- [[summary-17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming]] — source summary
- [[summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO]] — source summary
- [[Simon Willison]] — cites his view
- [[Prompt Injection]] — subject of his professional red-teaming work
- [[CAMEL Pattern]] — mitigation he also recommends
- [[HackAPrompt]] — company/competition he runs
- [[Learn Prompting]] — education company he runs
- [[Guardrails Do Not Work]] — his central thesis in episode 37
- [[Trustable]] / [[Repello]] — AI-security-adjacent companies he recommends
- [[MATS]] — AI safety research program he's involved with
