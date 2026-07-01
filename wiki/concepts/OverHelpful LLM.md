---
title: "Over-Helpful LLM"
type: concept
tags: [security, llm, threat-model, ai-code, sandboxing]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Why, and how you need to sandbox AI-Generated Code — Harshil Agrawal, Cloudflare.md"]
last_updated: 2026-06-30
---

## Definition
The Over-Helpful LLM is an insidious threat vector where an LLM, in trying to be helpful and do its job well, inadvertently accesses and processes sensitive data. It is not malicious — it is just trying to help — but the effect is the same: sensitive data gets processed by code you did not audit.

## Key Information
- Described by Harshil Agrawal as "insidious" because the behavior looks reasonable
- Example: asked to configure a database connection, the LLM reads environment variables to see what's available — accessing API keys, database credentials, and secrets
- The LLM is not trying to steal secrets; it is trying to gather information to do its assigned task better
- Dangerous precisely because the behavior appears reasonable and helpful, making it hard to detect
- Runs with the same privileges as the application — the LLM's code can read anything the application can read
- Part of a three-vector threat model alongside AI Code Hallucination and Compromised Prompts
- Mitigated by capability-based security: only grant the LLM's code access to what it explicitly needs, never broad access
- Proxy pattern is a key defense: keep secrets outside the sandbox and proxy sensitive operations through your own audited code

## Related
- [[summary-20260408 - Why, and how you need to sandbox AI-Generated Code — Harshil Agrawal, Cloudflare]] — source
- [[AI Code Hallucination]] — related threat vector
- [[PromptInjection]] — related threat vector
- [[CapabilityBasedSecurity]] — security model for mitigation
- [[Proxy Pattern (Secrets)]] — key defense pattern
- [[Sandboxing]] — broader mitigation approach
- [[Untrusted Code Execution]] — the broader problem
