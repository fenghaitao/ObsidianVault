---
title: "Shared Payment Tokens"
type: concept
tags: [concept, payments, stripe, agent-payments, credentials, security, determinism]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe.md"]
last_updated: 2026-06-30
---

## Definition
Shared Payment Tokens are Stripe's credential-sharing primitive that lets an agent collect a payment method, encode spend limits (amount, currency, time, seller), and share a scoped token with a seller. Limits are enforced server-side by Stripe, preventing the seller from exceeding the mandated constraints.

## Key Information
- **Scoped to seller**: Each token is bound to a specific merchant, preventing misuse by other parties
- **Enforced by Stripe**: Even if the seller attempts to charge more than the mandated amount, Stripe blocks the transaction server-side
- **Usage limits**: Can apply limits on amount, currency, and time window (e.g., $25 max, 30-day expiry)
- **Cross-payment-method**: Works across hundreds of different payment method types, not just credit cards
- **Seller transparency**: Sellers still receive brand and last-four digits for existing risk analysis systems — not a secret from the seller
- **Auditable**: All token usage is observable and traceable
- **Contrast with raw card sharing**: Handing a card number to an agent trusts the agent to charge correctly; shared tokens enforce limits at the infrastructure level
- **Foundation for Stripe Projects**: The Stripe Projects product is built on shared payment tokens for SaaS billing

## Related
- [[summary-20260606 - Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe]] — source
- [[Stripe]] — platform providing the primitive
- [[Steve Kaliski]] — presenter
- [[Machine Payments Protocol]] — uses shared payment tokens for payment
- [[Agent to Commerce Protocol]] — uses shared payment tokens for checkout
- [[Stripe Projects]] — built on shared payment tokens
- [[Agents as Economic Actors]] — broader framing
