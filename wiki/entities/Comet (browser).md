---
title: "Comet (browser)"
type: entity
tags: [tool, browser, ai, agent, security-incident]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz.md"]
last_updated: 2026-07-10
---

## Definition

Comet is an AI-powered browser that experienced a prompt injection vulnerability where malicious text on a webpage tricked the AI into exfiltrating user data and account information.

## Key Information

- A malicious actor crafted text on a web page that, when the AI-powered browser navigated to it, tricked the AI into leaking the main user's data and account data.
- This demonstrates the danger of indirect prompt injection in AI browser agents: simply browsing the web can trigger data exfiltration.
- Sander Schulhoff, who uses Comet himself, noted this vulnerability is likely shared by other AI browsers like Atlas.
- The incident highlights the escalating risk as AI agents are given access to browsing and user data.
- Zevi Arnovitz used Comet (described as "the Perplexity browser") to run analyses on Lewis Lynn's PM interview question bank
- Zevi had Comet's agent analyze which questions were most frequently asked in real PM interviews, helping him prioritize his preparation

## Related

- [[summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO]] — source summary
- [[summary-31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz]] — source summary
- [[Prompt Injection]] — attack vector
- [[Indirect Prompt Injection]] — the specific attack type
- [[Zevi Arnovitz]] — used for interview prep research
- [[AI Interview Prep]] — related concept
