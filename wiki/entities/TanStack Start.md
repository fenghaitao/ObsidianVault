---
title: "TanStack Start"
type: entity
tags: [framework, javascript, typescript, react, tanstack]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS.md"]
last_updated: 2026-06-30
---

## Definition

TanStack Start is a relatively new React-based framework (still in RC as of mid-2026) that is part of the TanStack ecosystem. It has an implicit contract with certain files like `start.ts` that must export specific things, making it a source of common gotchas for agent-driven development.

## Key Information

- **Status**: Still in RC (release candidate), changing constantly as of mid-2026
- **Implicit contracts**: Files like `start.ts` have implicit export contracts — breaking them silently breaks the app
- **Agent challenge**: AI models confidently make changes that look correct but break TanStack Start's implicit contracts
- **WorkOS example**: The WorkOS CLI's agent modified `start.ts` during AuthKit installation in a way that looked correct to both Nick and Claude but broke the TanStack Start contract
- **Gotcha source**: This experience drove Nick's shift from comprehensive skills to targeted gotchas

## Related

- [[summary-20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS]] — source
- [[WorkOS CLI]] — tool that encountered TanStack Start gotchas
- [[AuthKit]] — product being installed into TanStack Start projects
- [[Gotchas]] — the approach inspired by TanStack Start's implicit contracts
- [[Agentic Experience]] — designing for agent consumers of frameworks
