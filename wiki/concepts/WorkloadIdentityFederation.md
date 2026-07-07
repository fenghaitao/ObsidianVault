---
title: "WorkloadIdentityFederation"
type: concept
tags: [security, authentication, zero-trust, claude-platform, enterprise, identity]
sources: ["raw/01-articles/claude/2026-06-17 - Secure access to the Claude Platform with Workload Identity Federation.md"]
last_updated: 2026-07-07
---

## Definition

Workload Identity Federation (WIF) is an authentication mechanism on the [[Anthropic|Claude Platform]] that replaces static API keys with short-lived, scoped credentials issued at request time. It allows workloads (CI/CD pipelines, services, automated processes) to authenticate using their existing identity from any OIDC-compliant identity provider, eliminating the need to create, rotate, or protect long-lived Anthropic API keys.

## Key Information

### How It Works

WIF operates through three components working together:

1. **External Identity Provider**: The workload already has an identity -- an AWS IAM role, a GCP or Kubernetes service account, an Azure managed identity, a GitHub Actions token, Okta, or any other OIDC-compliant provider.

2. **Service Accounts**: Claude Platform service accounts give each workload its own identity, roles, and audit trail. This replaces the pattern of sharing a single API key across multiple workloads.

3. **Federation Rules**: A federation rule binds an external identity (from the identity provider) to a Claude Platform service account. When a workload requests access, the Claude Platform verifies the workload's signed OIDC token, matches its claims against the federation rules, and issues a short-lived access token bounded by the service account's roles and scopes.

Every token exchange and API request is recorded against the specific service account in audit logs.

### Compatibility

- Compatible with any OIDC-compliant identity provider
- Covers all Claude API endpoints
- Works through first-party SDKs and [[ClaudeCode]]
- The Admin API supports programmatic creation and management of issuers, service accounts, and federation rules for organizations operating at scale

### Setup

- The [[AnthropicConsole|Claude Console]] provides a guided setup flow with step-by-step validation and a test command to confirm successful authentication
- Federation rules support fine-grained scopes for least-privilege access
- API keys continue to work alongside WIF, enabling incremental migration one workload at a time

### Security Properties

- No static Anthropic credentials to create, rotate, or leak
- Each workload gets its own identity with scoped permissions, rather than sharing a broad-scope API key
- Audit trail is per-service-account, providing granular visibility into which workload performed which actions
- Aligns with [[ZeroTrustAIAgents|Zero Trust]] principles: cryptographically rooted identities, no long-lived secrets, least-privilege access

## Related

- [[summary-2026-06-17 - Secure access to the Claude Platform with Workload Identity Federation]] — source article
- [[ZeroTrustAIAgents]] — security framework WIF aligns with
- [[AnthropicConsole]] — the Claude Console for guided WIF setup
- [[ClaudeCode]] — supports WIF authentication
- [[CodeSecurity]] — broader security patterns in the Claude ecosystem
- [[Anthropic]] — the company providing the Claude Platform
