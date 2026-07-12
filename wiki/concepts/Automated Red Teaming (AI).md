---
title: "Automated Red Teaming (AI)"
type: concept
tags: [ai-security, testing, llm, industry]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md"]
last_updated: 2026-07-10
---

## Definition

Automated red teaming refers to tools (usually large language models themselves) that automatically generate prompts designed to trick other AI models into outputting malicious information such as hate speech, SEAB burn content, or misinformation.

## Key Information

- Automated red teaming systems are algorithms that generate adversarial prompts to elicit restricted outputs from target models.
- Sander Schulhoff argues that automated red teaming "works too well" — it always finds vulnerabilities in any transformer-based system, making its results unsurprising and not particularly useful for enterprises.
- Most enterprises deploy off-the-shelf models from frontier labs, so automated red teaming shows nothing novel — it's "plainly obvious" that these models can be tricked.
- The finding is often used to scare non-technical CISOs into buying guardrails, which Schulhoff considers manipulative.
- There are thousands of automated red teaming systems, many open source, and they all work against all platforms.
- Automated systems require orders of magnitude more attempts than human attackers but can still beat ~90% of defenses on average.
- The first HackAPrompt competition produced the first and largest open-source dataset of prompt injections, now used by every frontier lab and most Fortune 500 companies.

## Related

- [[summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO]] — source summary
- [[AI Guardrails]] — often sold as a complementary product
- [[Adversarial Robustness]] — what red teaming measures
- [[HackAPrompt]] — organization running red teaming competitions
