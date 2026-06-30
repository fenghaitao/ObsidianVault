---
title: "AuthKit"
type: entity
tags: [product, authentication, workos, nextjs, tanstack]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS.md"]
last_updated: 2026-06-30
---

## Definition

AuthKit is WorkOS's authentication product that provides ready-to-use auth for applications. It supports multiple frameworks (Next.js, React, TanStack Start, Ruby, etc.) and can be installed automatically via the WorkOS CLI in under 5 minutes.

## Key Information

- **Product family**: AuthKit Next.js, AuthKit React, and framework-specific packages
- **Installation**: Automated via `workos install` CLI command — detects project type and handles setup
- **Competitor migration**: CLI can detect and remove existing auth setups (e.g., Auth0) before installing AuthKit
- **Zero-friction onboarding**: Provisions a WorkOS account if the user doesn't have one, claimable later
- **Framework support**: Next.js, TanStack Start, Ruby, and more
- **Agentic positioning**: Designed to be installed by AI agents, not just humans — part of WorkOS's "agentically forward" strategy
- **Common gotchas**: Framework-specific pitfalls like TanStack Start's implicit `start.ts` export contract

## Related

- [[summary-20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS]] — source
- [[WorkOS]] — company
- [[WorkOS CLI]] — installation tool
- [[NickNisi]] — DX engineer working on it
- [[NextJS]] — supported framework
- [[TanStack Start]] — supported framework
- [[Gotchas]] — approach for agent guidance during installation
- [[Agentic Experience]] — strategic product philosophy
