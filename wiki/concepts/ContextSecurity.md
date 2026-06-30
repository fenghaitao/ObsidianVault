---
title: "ContextSecurity"
type: concept
tags: [context, security, prompt-injection, supply-chain, scanning]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - Context Is the New Code — Patrick Debois, Tessl.md"]
last_updated: 2026-06-29
---

## Definition
Context Security is the practice of securing AI context (prompts, skills, instructions) against threats including credential exposure, prompt injection, malicious third-party content, and supply chain attacks. It applies DevSecOps principles to the context supply chain.

## Key Information
- Introduced by Patrick Debois as part of the Context Development Life Cycle
- Multiple layers of security:
  - **Scanning**: Tools like Snyk scan context for credential exposure and third-party risks
  - **Provenance tracking**: AI SBOM tracks who built a skill, with what model, and how
  - **Context filters**: WAF-like filters that block prompt injections and malicious patterns before they enter the agent's context
  - **Sandboxing**: Running agents in isolated environments (but insufficient alone since context loads before sandboxing)
- Context files (agent.md, skills.md) are loaded without restrictions by default — there's no filtering
- As context becomes a shared, distributed artifact, the attack surface grows significantly
- Mirrors traditional software supply chain security but with AI-specific threats

## Related
- [[summary-20260503 - Context Is the New Code — Patrick Debois, Tessl]] — source
- [[ContextFilter]] — the WAF-like filtering mechanism
- [[AISBOM]] — provenance tracking for context
- [[PromptInjection]] — the primary threat
- [[Snyk]] — company providing context scanning
- [[ContextDistribution]] — the practice that creates security risks
- [[SupplyChainAttack]] — the broader threat category
