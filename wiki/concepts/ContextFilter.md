---
title: "ContextFilter"
type: concept
tags: [context, security, prompt-injection, agent-safety, filtering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - Context Is the New Code — Patrick Debois, Tessl.md"]
last_updated: 2026-06-29
---

## Definition
A Context Filter is a security mechanism that acts like a web application firewall (WAF) for AI context — filtering out prompt injections, malicious patterns, and other harmful content before it enters an agent's context window. It is necessary because agents load context files (agent.md, skills.md) without restrictions by default.

## Key Information
- Introduced by Patrick Debois as part of context security in the CDLC
- Analogous to a WAF (Web Application Firewall) but for context rather than HTTP traffic
- Necessary because coding agents load agent.md, skills.md, and other context files without any filtering by default
- Traditional sandboxing cannot prevent context-based attacks because the context is loaded before the sandbox applies
- Filters out: prompt injections, malicious patterns, credential exposure, and other harmful content
- Part of a broader context security approach that includes Snyk-like scanning and AI SBOM tracking

## Related
- [[summary-20260503 - Context Is the New Code — Patrick Debois, Tessl]] — source
- [[ContextSecurity]] — the broader security domain
- [[PromptInjection]] — the primary threat context filters defend against
- [[Agent Sandbox]] — complementary but insufficient protection
- [[AISBOM]] — tracking context provenance
