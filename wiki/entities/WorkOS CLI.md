---
title: "WorkOS CLI"
type: entity
tags: [tool, cli, workos, authkit, agentic-experience, onboarding]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS.md"]
last_updated: 2026-06-30
---

## Definition

The WorkOS CLI is a public-facing command-line tool that automates AuthKit installation for WorkOS customers. It detects the user's project framework, removes competing auth solutions, installs AuthKit, and provisions a WorkOS account — all in under 5 minutes with zero friction.

## Key Information

- **Headlining feature**: `workos install` — zero-friction AuthKit setup
- **Project detection**: Automatically identifies framework (Next.js, TanStack Start, Ruby, etc.)
- **Competitor removal**: Can detect and remove existing auth setups like Auth0 before installing AuthKit
- **Account provisioning**: If the user doesn't have a WorkOS account, it provisions one that can be claimed later
- **Time**: Completes full setup in under 5 minutes
- **Purpose**: Eliminates the friction of reading docs and manual setup — key to being "agentically forward" in WorkOS's public-facing persona
- **Challenge**: Models are overly confident and claim success when they've actually broken things (e.g., modifying TanStack Start's `start.ts` and breaking its implicit export contract)
- **Gotchas approach**: Instead of comprehensive docs-based skills (10,000+ lines), the CLI uses 553 lines of gotchas — common pitfalls identified through evals

## Related

- [[summary-20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS]] — source
- [[WorkOS]] — company
- [[AuthKit]] — the product being installed
- [[NickNisi]] — creator
- [[Gotchas]] — the approach used for agent guidance
- [[Agentic Experience]] — the strategic goal
- [[TanStack Start]] — framework that revealed gotcha-based approach
- [[EvalPrimitives]] — measurement that revealed skills were hurting performance
