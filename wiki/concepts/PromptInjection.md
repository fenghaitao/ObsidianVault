---
title: "PromptInjection"
type: concept
tags: [security, llm, vulnerability, ai-safety]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251219 - From Arc to Dia： Lessons learned building AI Browsers – Samir Mody, The Browser Company of New York.md"]
last_updated: 2026-06-25
---

## Definition

Prompt injection is a security attack in which a third party overrides the instructions of an LLM to cause harm, such as data exfiltration, execution of malicious commands, or ignoring safety rules. It is particularly dangerous in browsers due to the "lethal trifecta" of access to private data, exposure to untrusted content, and ability to externally communicate.

## Key Information

- Attack vector: hidden instructions in third-party content (e.g., website HTML) that override the LLM's system instructions
- Example: instructing an LLM to summarize a webpage, but hidden injection causes it to open a URL with exfiltrated personal data as GET parameters
- Technical mitigations: wrapping untrusted context in tags, separating data from instructions via system/user roles, random delimiter tags — but no guarantees
- The Browser Company's approach: blend technology with UX confirmation steps (autofill, scheduling, email all require user confirmation before execution)
- Confirmation steps don't prevent injections but give users control, awareness, and trust

## Related

- [[summary-20251219 - From Arc to Dia： Lessons learned building AI Browsers – Samir Mody, The Browser Company of New York]] — source
- [[DiaBrowser]] — product with injection mitigations
- [[AIBrowsers]] — category with heightened injection risk
- [[ModelBehavior]] — related discipline for shaping LLM outputs
