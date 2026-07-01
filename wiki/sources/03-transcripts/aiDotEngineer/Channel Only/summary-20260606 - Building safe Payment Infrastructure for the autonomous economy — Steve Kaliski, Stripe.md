---
title: "summary-20260606 - Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe"
type: source
tags: [source, transcript, payments, stripe, autonomous-economy, agent-payments, payment-tokens, agent-to-commerce, determinism]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe.md"]
last_updated: 2026-06-30
---

## Core Summary
Steve Kaliski, Principal Software Engineer at Stripe, presents three infrastructure primitives for enabling safe payments between AI agents and businesses: Shared Payment Tokens, the Machine Payments Protocol, and the Agent to Commerce Protocol (ACP). The central thesis is that discovery and exploration benefit from non-determinism (LLMs excel here), but credentials, payments, and checkout REQUIRE determinism. The key is isolating "what to find" from "how to transact." Agents are already economic actors — they consume tokens and spend money proxied through subscriptions — and the challenge is enabling them to transact with any business safely.

## Key Points
- **Core Thesis**: Non-determinism for discovery, determinism for transactions. Credentials, payments, and checkout require deterministic flows to prevent wrong-place, wrong-thing, wrong-amount, and wrong-credential failures.
- **Agents as Economic Actors**: Agents already spend money — through LLM provider subscriptions and token consumption. The question is how to extend this to any business and any payment method.
- **The Browser Approach is Flawed**: Letting agents operate browsers like humans introduces risk: wrong domain (phishing), wrong product (parsing errors), wrong amount (price drift, currency, tax), wrong credential (card theft). It's slow, finicky, and hard to observe.
- **The API Approach**: Agents prefer code over dashboards. The ideal is API-driven, programmatic payment flows with verifiable identities and enforced spend policies.

### Three Stripe Primitives

**1. Shared Payment Tokens**: An agent collects a payment credential and shares a scoped token with a seller. The token encodes spend limits (amount, currency, time window) and is scoped to a specific seller. Enforced by Stripe server-side — even if the seller attempts to charge more, Stripe blocks it. Works across hundreds of payment method types. Sellers still receive brand/last-four information for risk analysis. Built into Stripe Projects.

**2. Machine Payments Protocol** (with Tempo): Extends HTTP tool calls with a payment layer. When an agent calls a paid API endpoint, the server returns HTTP 402 with an encoded payload describing what's being purchased and how to pay. The agent supplies a shared payment token to complete the transaction. Enables ephemeral, pay-per-use tool interactions. Transactions settle on blockchain (Tempo, Base).

**3. Agent to Commerce Protocol (ACP)** (with OpenAI): A standard set of APIs and objects for structured checkout flows. Instead of agents stumbling through browser UIs, sellers express product catalogs in JSON (images, descriptions, pricing). Agents initiate checkouts programmatically. Sellers relay back cart state (line items, tax, shipping options) as structured data. Every interaction — changing quantity, shipping, payment method — is a deterministic API back-and-forth. Payment completes via shared payment tokens or other credentials.

### Design Principles
- **Seller remains in control**: Sellers maintain customer relationships and receive risk signals (brand, last four digits, etc.)
- **Minimized blast radius**: Scoped tokens with amount/time/seller limits prevent runaway spending
- **Auditable**: All transactions are observable and traceable
- **Agent-friendly businesses**: Companies should expose API-driven commerce flows, not just web UIs, to maximize determinism
- **Non-deterministic planner + deterministic constraints + verifiable parties + structured negotiation = small radius of risk**

### Q&A Highlights
- **Blockchain**: Transaction data lives on-chain (Tempo, Base); Stripe replicates a product view internally
- **Recurring budgets**: Shared payment tokens can support refresh flows (similar to OAuth access/refresh) for recurring spending. Budget-based limits work by creating multiple scoped tokens
- **Stripe Projects**: Built on shared payment tokens; expresses seller products and recurring payment patterns for SaaS businesses

## Related
- [[Steve Kaliski]] — speaker, Principal Software Engineer at Stripe
- [[Stripe]] — payment infrastructure platform
- [[Shared Payment Tokens]] — credential scoping primitive
- [[Machine Payments Protocol]] — HTTP 402-based payment protocol
- [[Agent to Commerce Protocol]] — structured checkout API standard
- [[Agents as Economic Actors]] — framing agents as spenders
- [[Stripe Projects]] — product built on shared payment tokens
- [[Tempo]] — blockchain partner for Machine Payments Protocol
- [[OpenAI]] — partner on Agent to Commerce Protocol
- [[aiDotEngineer]] — event host
