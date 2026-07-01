---
title: "Machine Payments Protocol"
type: concept
tags: [concept, payments, http, stripe, tempo, blockchain, agent-payments, determinism]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe.md"]
last_updated: 2026-06-30
---

## Definition
The Machine Payments Protocol is a payment layer for HTTP tool calls, co-developed by Stripe and Tempo. When an agent calls a paid API endpoint, the server returns HTTP 402 (Payment Required) with an encoded payload describing what is being purchased, who the seller is, and how to pay. The agent then supplies a shared payment token to complete the transaction.

## Key Information
- **HTTP 402**: Uses the standard "Payment Required" status code to signal that a tool/API call requires payment
- **Encoded payload**: The 402 response includes structured data about the purchase: what's being bought, the seller identity, the amount, and the payment mechanism
- **Ephemeral interactions**: Designed for pay-per-use tool calls where passing a long-lived API key is impractical
- **Blockchain settlement**: Transactions settle on the Tempo blockchain (using path USD); Stripe replicates a product view internally
- **Deterministic**: Closes the window of uncertainty between tool call and payment — the seller tells the agent exactly how to pay
- **Integration with Shared Payment Tokens**: The agent uses a shared payment token (with spend limits) to authorize the payment, maintaining the blast-radius control
- **Multi-chain**: Stripe supports multiple blockchain networks including Tempo and [[Base]]

## Related
- [[summary-20260606 - Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe]] — source
- [[Stripe]] — co-developer
- [[Tempo]] — blockchain partner
- [[Steve Kaliski]] — presenter
- [[Shared Payment Tokens]] — credential primitive used for payment
- [[Agent to Commerce Protocol]] — companion protocol for checkout flows
- [[Base]] — another supported blockchain network
