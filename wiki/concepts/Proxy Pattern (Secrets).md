---
title: "Proxy Pattern (Secrets)"
type: concept
tags: [security, secrets, sandboxing, pattern, architecture]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Why, and how you need to sandbox AI-Generated Code — Harshil Agrawal, Cloudflare.md"]
last_updated: 2026-06-30
---

## Definition
The Proxy Pattern for secrets is a security architecture where API keys and sensitive credentials never enter the sandbox environment. Instead, sandboxed code makes requests to a proxy endpoint in the trusted worker, which adds authentication headers with the real credentials and forwards the request to the external service.

## Key Information
- The common (wrong) pattern: passing API keys as environment variables to the sandbox — any code inside, including AI-generated or prompt-injected code, can read them
- The correct pattern: sandboxed code calls a proxy endpoint on your worker → your worker receives the request → adds authentication header with real API key → forwards to external service → returns response
- The secret lives in the worker's environment, which the sandbox cannot access
- This should be the default for any secret that AI-generated code might need
- Applies to both isolate-based and container-based sandboxing approaches
- Part of the universal sandboxing checklist: "Keep secrets outside the sandbox"
- Also applicable to network control: route all outbound traffic through your own service for allow-listing, logging, authentication, and rate limiting

## Related
- [[summary-20260408 - Why, and how you need to sandbox AI-Generated Code — Harshil Agrawal, Cloudflare]] — source
- [[Sandboxing]] — broader security context
- [[ContainerBased Sandboxing]] — applies to containers
- [[Isolate-based Sandboxing]] — applies to isolates
- [[CapabilityBasedSecurity]] — underlying security model
- [[OverHelpful LLM]] — threat this pattern defends against
- [[Lethal Trifecta]] — security model this pattern helps address
