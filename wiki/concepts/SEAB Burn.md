---
title: "SEAB Burn"
type: concept
tags: [ai-security, content-safety, classification]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md"]
last_updated: 2026-07-10
---

## Definition

SEAB Burn (also written as CBRNE) stands for Chemical, Biological, Radiological, Nuclear, and Explosives — a category of restricted information that AI models are trained not to output, commonly used in AI security and safety evaluations.

## Key Information

- The acronym is commonly thrown around in AI security and safety communities as a standard category of harmful information that models should not generate.
- Eliciting SEAB burn information from AI models is a primary goal of many jailbreaking and prompt injection attacks.
- Anthropic's constitutional classifiers have made it significantly harder to get SEAB burn information from Claude models compared to earlier versions.
- However, humans can still elicit SEAB burn information from the best-defended models in under an hour.
- Stopping SEAB burn elicitation is considered easier than stopping indirect prompt injection because the rule is simple ("never talk about this") versus the nuanced rules for agent actions ("sometimes send emails, but not when tricked").

## Related

- [[summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO]] — source summary
- [[Jailbreaking (AI)]] — attack vector often targeting SEAB burn content
- [[Constitutional Classifiers]] — Anthropic's defense against SEAB burn elicitation
