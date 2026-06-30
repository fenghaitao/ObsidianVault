---
title: "CCS"
type: entity
tags: [company, medical-supply, customer-support, enterprise-ai, customer]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML.md"]
last_updated: 2026-06-30
---

## Definition
CCS is a medical supply company that is a customer of Adaptive ML, using RL-trained models for customer support with containment rate as the primary optimization metric.

## Key Information
- **Use case**: Customer support system where the model handles calls end-to-end
- **Primary metric**: Containment rate — the percentage of calls brought end-to-end by the model without human escalation
- **RL application**: Containment rate can be directly maximized as a reward signal in RL training
- **Real-world complexity**: Customers calling CCS may be in panic situations; the model must handle difficult, emotional conversations and know when to escalate (e.g., call 911)
- **Data strategy**: Real customer-agent transcripts used to train mock users that simulate realistic (including panicked) customers
- **Platform**: Uses Adaptive ML's Adaptive Engine

## Related
- [[Adaptive ML]] — RL Ops platform provider
- [[Reward Signal]] — containment rate as a direct KPI-based reward
- [[Mock User]] — realistic customer simulation for agent training
- [[summary-20260512 - Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML]] — source
