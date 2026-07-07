---
title: "summary-2026-06-17 - Secure access to the Claude Platform with Workload Identity Federation"
type: source
tags: [source, claude-blog]
sources: ["raw/01-articles/claude/2026-06-17 - Secure access to the Claude Platform with Workload Identity Federation.md"]
last_updated: 2026-07-07
---

## Core Summary

Workload Identity Federation (WIF) is now generally available on the Claude Platform, replacing static API keys with short-lived, scoped credentials issued at request time. WIF is compatible with any OIDC-compliant identity provider (AWS IAM, GCP, Azure, Kubernetes, GitHub Actions, Okta, and others) and covers all Claude API endpoints, including first-party SDKs and Claude Code. The system introduces service accounts so each workload gets its own identity, roles, and audit trail, with federation rules binding external identities to those accounts. An Admin API enables programmatic configuration at scale, and API keys remain supported alongside WIF for gradual migration.

## Key Points

- WIF eliminates static Anthropic credentials entirely -- no keys to create, rotate, or leak; workloads authenticate with their existing identity from any OIDC-compliant provider.
- Service accounts give each workload its own identity with fine-grained scopes and per-account audit logging, replacing shared API keys.
- Federation rules bind external identities (AWS IAM roles, GCP service accounts, etc.) to Claude Platform service accounts; the platform verifies signed OIDC tokens and issues scoped access tokens at request time.
- The Claude Console provides a guided setup flow with validation and a test command; the Admin API supports fully programmatic federation management for organizations operating at scale.
- API keys continue to work alongside WIF, enabling incremental migration one workload at a time.

## Related

- [[WorkloadIdentityFederation]] — the authentication pattern this article announces
- [[AnthropicConsole]] — the Claude Console used for guided WIF setup
- [[ClaudeCode]] — supports WIF for authentication
- [[ZeroTrustAIAgents]] — WIF aligns with zero-trust principles (cryptographically rooted identities, no static credentials)
