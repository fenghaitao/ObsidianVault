---
title: "Agents as Economic Actors"
type: concept
tags: [concept, agents, payments, economics, autonomous-economy]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe.md"]
last_updated: 2026-06-30
---

## Definition
Agents as Economic Actors is the framing that AI agents are already spenders of money — consuming tokens and proxying payments through LLM provider subscriptions — and the challenge is to extend this capability to transact with any business using any payment method, safely.

## Key Information
- **Already spending**: Agents in tools like Codex, Cursor, or Claude Code are already spending money — through token consumption converted to dollars, or proxied through the subscription backing the agent harness
- **Current limitation**: Agents can only spend with their LLM provider, not with arbitrary businesses
- **Goal**: Enable agents to use other currencies, spend patterns, payment methods, and interact with any business
- **Required infrastructure**: Credential management (who pays), payment flows (how to pay), and checkout (what is being bought) — all must be deterministic
- **Risk categories**: Wrong place (phishing), wrong thing (misidentified product), wrong amount (price drift, tax, currency), wrong credential (card theft)
- **Solution approach**: Non-deterministic planner for discovery + deterministic constraints for transactions + verifiable parties + structured negotiation = small radius of risk

## Related
- [[summary-20260606 - Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe]] — source
- [[Steve Kaliski]] — presenter
- [[Stripe]] — infrastructure provider
- [[Shared Payment Tokens]] — credential management primitive
- [[Machine Payments Protocol]] — payment flow primitive
- [[Agent to Commerce Protocol]] — checkout primitive
- [[Stripe Projects]] — SaaS billing built on these primitives
