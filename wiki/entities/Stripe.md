---
title: "Stripe"
type: entity
tags: [platform, payments, billing, ai-pricing, agent-payments, autonomous-economy]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260501 - Mastering AI Pricing — Mayank Pant, Stripe.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe.md"]
last_updated: 2026-06-30
---

## Definition
Stripe is a payment and billing platform that has become the dominant billing infrastructure for AI companies, with 78% of AI companies building on Stripe. It offers subscription, usage-based, and hybrid pricing models, plus enterprise contract management via Metronome. Stripe is also building infrastructure for agent-to-business payments, including shared payment tokens, machine payments protocol, and the agent to commerce protocol.

## Key Information
- 78% of AI companies build on Stripe for billing infrastructure
- Stripe Billing supports subscription pricing, usage pricing, and hybrid pricing
- Metronome (acquired/integrated) handles enterprise contracts with minimum commitments, pre-commitments, and overage prices
- Full platform includes payments, tax, invoicing, and revenue recognition on AI pricing
- Companies building on Stripe include Anthropic, OpenAI, Lovable, ElevenLabs, and Intercom
- Manus automatically sets up Stripe webhooks for applications built on the platform
- Manus can receive Stripe webhooks, enabling payment processing in agent-built apps
- Provides testing tools for webhook verification
- Future plans include autoscaling and warm deployments for Stripe-integrated apps
- Differentiates Manus from platforms that only provide front-end capabilities without webhook support

### Agent Payment Infrastructure
- **Shared Payment Tokens**: Credential-sharing primitive that encodes spend limits (amount, currency, time, seller) and enforces them server-side
- **Machine Payments Protocol**: HTTP 402-based payment layer for agent tool calls, co-developed with [[Tempo]]; settles on blockchain
- **Agent to Commerce Protocol (ACP)**: Structured checkout APIs co-developed with [[OpenAI]]; expresses product catalogs and cart state as JSON for deterministic agent purchases
- **Stripe Projects**: SaaS billing product built on shared payment tokens for agent-friendly recurring payments
- **Design principle**: Non-determinism for discovery, determinism for transactions — agents prefer code/APIs over browser UIs

## Related
- [[summary-20260606 - Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe]] — source (agent payment infrastructure)
- [[summary-20260501 - Mastering AI Pricing — Mayank Pant, Stripe]] — source (AI pricing framework)
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[Steve Kaliski]] — principal engineer, agent payments lead
- [[Mayank Pant]] — billing solution architect at Stripe
- [[Shared Payment Tokens]] — credential scoping primitive
- [[Machine Payments Protocol]] — HTTP 402 payment protocol
- [[Agent to Commerce Protocol]] — structured checkout standard
- [[Stripe Projects]] — product built on shared payment tokens
- [[AI Pricing]] — core discipline Stripe supports
- [[Hybrid Pricing]] — pricing model enabled by Stripe Billing
- [[ManusAI]] — platform with Stripe integration
- [[Agent Sandbox]] — enables full Docker-based apps with webhooks
