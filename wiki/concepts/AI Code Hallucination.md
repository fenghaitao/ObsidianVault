---
title: "AI Code Hallucination"
type: concept
tags: [security, llm, ai-code, threat-model, sandboxing]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Why, and how you need to sandbox AI-Generated Code — Harshil Agrawal, Cloudflare.md"]
last_updated: 2026-06-30
---

## Definition
AI Code Hallucination is a threat vector where LLMs generate incorrect code that is not malicious but still dangerous when executed in production. The model is doing its best, but wrong code running with production privileges can still cause crashes, resource exhaustion, and service disruption.

## Key Information
- Not adversarial — the model is genuinely trying to produce correct code but makes mistakes
- Common examples: importing non-existent packages, writing recursive functions with no base case, generating infinite loops from misunderstood termination conditions
- An infinite loop can consume compute resources; a bad import can crash processes; an unbounded recursive function can blow the stack
- This is the baseline threat — even in a world with no bad actors, protection is still needed
- Hallucinating code runs with the same privileges as the application: file system access, environment variables, network, database, API keys
- Part of a three-vector threat model alongside Over-Helpful LLMs and Compromised Prompts
- Mitigated by sandboxing: resource limits (timeouts, memory caps, CPU limits) prevent a hallucinated infinite loop from taking down servers

## Related
- [[summary-20260408 - Why, and how you need to sandbox AI-Generated Code — Harshil Agrawal, Cloudflare]] — source
- [[OverHelpful LLM]] — related threat vector
- [[PromptInjection]] — related threat vector
- [[Sandboxing]] — mitigation approach
- [[Untrusted Code Execution]] — the broader problem
- [[CapabilityBasedSecurity]] — security model for mitigation
