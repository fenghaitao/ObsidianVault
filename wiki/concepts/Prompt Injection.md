---
title: "Prompt Injection"
type: concept
tags: [ai-security, attack-vector, llm, agent]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We've passed the inflection point & dark factories are coming.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/18 - From skeptic to true believer： How OpenClaw changed my life ｜ Claire Vo.md"]
last_updated: 2026-07-11
---

## Definition

Prompt injection is an attack vector where a malicious user overrides a developer's system prompt by providing crafted input that causes the AI model to ignore its original instructions and perform unintended actions.

## Key Information

- Differs from jailbreaking: prompt injection involves a malicious user, a model, AND a developer's system prompt that the attacker tries to override. Jailbreaking is just user vs. model with no system prompt.
- The first publicly documented prompt injection was against remotely.io's Twitter chatbot, where attackers made it threaten the president instead of promoting remote work.
- The Math GPT incident demonstrated prompt injection leading to code execution: attackers got the model to write code that exfiltrated the OpenAI API key from the application server.
- The ServiceNow Assist AI attack was a "second-order prompt injection" where a benign agent was instructed to recruit more powerful agents to perform malicious database operations.
- Indirect prompt injection occurs when an attacker places malicious text in data sources that the AI agent later reads (e.g., a malicious email in an inbox, malicious text on a webpage).
- The Comet browser incident demonstrated indirect prompt injection: simply browsing to a webpage with crafted text caused the AI to leak user data.
- Prompt injection is considered much harder to solve than jailbreaking because it involves legitimate actions (like sending emails) that the model must sometimes do, making the boundary harder to define.
- Prompt-based defenses (where the system prompt instructs the model to ignore malicious inputs) are considered the worst form of defense, known to be ineffective since early 2023.

- The term was coined by Simon Wilson in 2022 (before ChatGPT launched), though he regrets the name because it misleadingly implies the problem is solvable like SQL injection (which has known fixes). Prompt injection is fundamentally different and possibly unsolvable.
- Simon's second attempt at naming: the "lethal trifecta" — a subset of prompt injection requiring three conditions: access to private information, exposure to malicious instructions, and exfiltration capability. Cut off any one leg to make the system safe.
- Simon's prediction: the "Challenger disaster of AI" — the industry keeps using these systems unsafely without consequences, normalizing deviance until a catastrophic failure occurs.
- Simon: "You can get to like 97% effectiveness on those filters. I think that's a failing grade. That means that three out of a hundred of these attacks will steal all of your information."
- The CAMEL paper (Google DeepMind) proposed a solution: split the agent into a privileged agent and a quarantined agent, with tainted data tracking and human-in-the-loop on high-risk actions only.
- Open Claw demonstrates the demand for digital assistants despite the prompt injection risk — hundreds of thousands of people set it up despite security vulnerabilities.

## Related

- [[summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO]] — source summary
- [[Jailbreaking (AI)]] — related attack vector
- [[Indirect Prompt Injection]] — subcategory of prompt injection
- [[AI Guardrails]] — proposed defense against prompt injection
- [[Camel (framework)]] — permission-based defense
