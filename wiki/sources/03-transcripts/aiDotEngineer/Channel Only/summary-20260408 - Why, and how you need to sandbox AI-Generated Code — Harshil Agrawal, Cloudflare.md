---
title: "summary-20260408 - Why, and how you need to sandbox AI-Generated Code — Harshil Agrawal, Cloudflare"
type: source
tags: [source, transcript, security, sandboxing, ai-generated-code]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Why, and how you need to sandbox AI-Generated Code — Harshil Agrawal, Cloudflare.md"]
last_updated: 2026-06-30
---

## Core Summary

Harshil Agrawal from Cloudflare presents the security case for sandboxing AI-generated code. Running LLM-generated code is "running untrusted code from the internet" with production privileges. Three threat vectors: hallucination (wrong code), helpful LLM (reads credentials to "help"), and compromised prompts (injection attacks). The solution: browser-style sandboxing that's been standard for decades.

## Key Points

- Strip away the AI framing: running LLM code is running untrusted code from the internet with your production credentials.
- Three threat vectors: (1) Hallucination — wrong code, infinite loops, bad imports. (2) Helpful LLM — reads env vars and secrets to "configure properly." (3) Prompt injection — adversarial input exfiltrating data.
- AI-generated code runs with the same privileges as your application: file system, network, database, API keys.
- Solution: sandboxing. Browsers have done this for decades — every tab runs isolated. Same principle applies to AI code.
- Cloudflare's approach leverages existing sandboxing infrastructure at the edge.

## Related

- [[Harshil Agrawal]] — speaker, Cloudflare
- [[Cloudflare]] — company
- [[AISecurity]] — security for AI-generated code
- [[CodeSandboxing]] — sandboxing technique
- [[PromptInjection]] — attack vector
- [[LLMHallucination]] — baseline threat
