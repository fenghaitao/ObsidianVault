---
title: "Math GPT"
type: entity
tags: [tool, ai, education, security-incident, prompt-injection]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md"]
last_updated: 2026-07-10
---

## Definition

Math GPT was a website that solved math problems using GPT-3, notable for being one of the earliest documented prompt injection attacks that resulted in data exfiltration.

## Key Information

- Users would upload math problems in natural language, and the system would do two things: ask GPT-3 to solve the problem, and ask GPT-3 to write code to solve it, then execute that code on the same server.
- A user realized they could prompt-inject the system to write malicious code, resulting in the exfiltration of the OpenAI API key from the application server.
- The vulnerability was responsibly disclosed. The site was run by a professor from South America.
- The incident was documented in a MITRE report.
- This is a classic example of how prompt injection can lead to real security breaches when AI-generated code is executed without sandboxing.

## Related

- [[summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO]] — source summary
- [[Prompt Injection]] — attack vector demonstrated
- [[GPT-3]] — model used
