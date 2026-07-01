---
title: "Agent to Commerce Protocol"
type: concept
tags: [concept, payments, checkout, stripe, openai, agent-payments, ecommerce, determinism]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe.md"]
last_updated: 2026-06-30
---

## Definition
The Agent to Commerce Protocol (ACP) is a standard set of APIs and objects co-developed by Stripe and OpenAI that enables structured, deterministic checkout flows between AI agents and e-commerce sellers. Instead of agents stumbling through browser UIs, ACP expresses product catalogs and cart state as structured JSON data with programmatic back-and-forth negotiation.

## Key Information
- **Co-developed with OpenAI**: Stripe and OpenAI partnered to create ACP as a standard for agent-friendly commerce
- **Product catalog expression**: Sellers expose products as JSON with images, descriptions, and pricing — agents can query and select without web crawling
- **Checkout initiation**: Agents specify buyer identity, line items, and quantities to create a checkout session
- **Structured cart relay**: Sellers respond with structured cart state: line items, base prices, applicable tax, fulfillment options — eliminating parsing errors
- **Deterministic negotiation**: Every state change (quantity, shipping, payment method) is a programmatic API back-and-forth, not a browser interaction
- **Payment integration**: Final payment uses [[Shared Payment Tokens]] or other credentials
- **Seller remains in control**: Sellers maintain customer relationships and receive risk signals they need
- **Multi-payment-method**: Flexible to crypto, cards, and hundreds of other payment methods
- **Example**: Stripe Press (Stripe's book store) implemented ACP — the "robot-friendly" JSON catalog as an alternative to the human-friendly web UI

## Related
- [[summary-20260606 - Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe]] — source
- [[Stripe]] — co-developer
- [[OpenAI]] — co-developer
- [[Steve Kaliski]] — presenter
- [[Shared Payment Tokens]] — payment credential used in checkout
- [[Machine Payments Protocol]] — companion protocol for API-based payments
- [[Stripe Projects]] — related product for SaaS commerce
