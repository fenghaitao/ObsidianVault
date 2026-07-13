---
title: "summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md"]
last_updated: 2026-07-12
---

## Core Summary

[[Lenny Rachitsky]] interviews [[Sander Schulhoff]] (CEO of [[HackAPrompt]] and [[Learn Prompting]], a leading AI red-teaming/adversarial-robustness researcher and a prior podcast guest) about why AI guardrails fundamentally do not work, why the AI security industry is largely selling ineffective products, and what companies can actually do about it. Schulhoff's central claims: the attack space against any LLM is effectively infinite (roughly 10^1,000,000 possible prompts), so any "99% blocked" guardrail statistic is not statistically meaningful; automated red-teaming tools always find exploits against any transformer-based model (so their findings reveal nothing novel); and — his most quotable line — "you can patch a bug, but you can't patch a brain." He argues the real, current risk isn't chatbots telling people bad things, but agentic systems and AI-powered browsers/robots that can take real actions, and walks through concrete incidents (ServiceNow's "Now Assist" agent-recruiting-agent attack, a Comet browser data-exfiltration bug, and a Claude Code-orchestrated cyberattack) as evidence the threat is no longer theoretical. His practical advice: most simple chatbot deployments don't need defenses at all (an attacker could get the same info from ChatGPT directly); classical cyber-security discipline (data/action permissioning) plus a dedicated AI-security-literate hire matters far more than buying guardrail products; the [[CAMEL Pattern]] is a legitimately useful (if narrow) architectural mitigation; and education/awareness is the highest-leverage lever available today. He predicts a market correction in AI-security-vendor revenue within the next year as buyers realize guardrails don't meaningfully help, alongside the first real-world, consequential AI-agent security incidents.

## Key Points

- **Guardrails do not work**: guardrail vendors' "we catch 99% of attacks" claims are statistically meaningless against an effectively infinite attack space (~10^1,000,000 possible prompts for a model like GPT-5); adaptive attackers (especially humans) break state-of-the-art guardrails in 10-30 attempts, per a joint research paper Schulhoff co-published with OpenAI, Google DeepMind, and Anthropic.
- **You can patch a bug, but you can't patch a brain**: unlike a classical software bug, once "fixed" you can be near-certain a model vulnerability persists even after a patch — because the underlying failure mode is linguistic/behavioral, not a discrete code defect.
- **Automated red-teaming works "too well"**: it reliably finds exploits against any transformer-based model, so its findings are not novel information for anyone who understands the space — but can look alarming to non-technical buyers, fueling guardrail sales.
- **Jailbreaking vs. prompt injection vs. indirect prompt injection**: jailbreaking is a malicious user tricking a model directly (no developer system prompt to bypass); prompt injection involves a developer's system prompt that a malicious user tries to override; indirect/second-order prompt injection (the ServiceNow and email-agent examples) involves malicious instructions embedded in external content an agent reads, which the agent then acts on without any direct user malice.
- **Real incidents discussed**: the first public prompt injection (remotely.io's Twitter chatbot, tricked into threatening the president); MathGPT (tricked into exfiltrating its own OpenAI API key via generated code); the Las Vegas Cybertruck bombing (attacker allegedly used a chatbot to help plan it); a [[Claude Code]]-orchestrated cyberattack (defenses bypassed by splitting a malicious request across separate, individually-innocuous-looking agent sessions); ServiceNow's "Now Assist" agent tricked into recruiting more-privileged internal agents to perform unauthorized database writes and email exfiltration despite an active prompt-injection-protection feature; and a Comet browser bug where a malicious web page tricked the AI browser into leaking the logged-in user's account data.
- **[[CAMEL Pattern]]** (Google-originated): restrict an agent's *permissions* based on what the user's request actually requires, before execution, rather than trying to filter/classify inputs and outputs after the fact — effective for simple single-purpose requests, but breaks down when a single request legitimately needs both read and write access (e.g., "read my inbox and forward anything ops-related").
- **Practical recommendations**: (1) simple read-only/no-action chatbots usually need no additional defense, since an attacker could get the same harmful output directly from ChatGPT/Claude/Gemini; (2) get classical cyber-security data/action permissioning right — an agent should only ever be able to damage the user interacting with it, never others; (3) hire or contract a genuine AI-security researcher, since the discipline sits at an underserved intersection of classical cyber security and AI research; (4) don't deploy blanket guardrails/automated red-teaming products — they add product friction without meaningful security benefit; (5) invest in education and awareness across the org.
- **Prediction**: a market correction in AI-guardrail/red-teaming vendor revenue within the next 6-12 months, alongside the first genuinely damaging, publicly visible AI-agent security incidents, as agentic and browser/robotic AI deployment expands.
- Related AI-safety framing: Schulhoff connects the problem to the broader alignment "god in a box" metaphor and namechecks "control" (the AI-safety subfield studying how to safely operate a possibly-malicious AI) via his work with the [[MATS]] research-scholar program.

## Related

- [[Sander Schulhoff]] — episode guest, CEO of HackAPrompt and Learn Prompting
- [[HackAPrompt]] — his AI red-teaming company/competition
- [[Learn Prompting]] — his prompt-engineering education company
- [[Lenny Rachitsky]] — podcast host
- [[Prompt Injection]] — core subject of the episode
- [[CAMEL Pattern]] — core mitigation discussed
- [[Guardrails Do Not Work]] — episode's central thesis
