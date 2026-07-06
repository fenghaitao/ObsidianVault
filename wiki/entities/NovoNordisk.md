---
title: "Novo Nordisk"
type: entity
tags: [enterprise, pharmaceutical, healthcare, ai-adopter, documentation]
sources: ["raw/01-articles/claude/2025-10-01 - How enterprises are driving AI transformation with Claude.md", "raw/01-articles/claude/2025-10-30 - Building AI agents for healthcare and life sciences.md"]
last_updated: 2026-07-04
---

## Definition

Novo Nordisk is a pharmaceutical company and creator of Ozempic. Its documentation process for pharmaceutical development — clinical study reports that can run 300 pages — was a critical bottleneck, with staff writers historically averaging just 2.3 reports annually and each day of delay costing up to $15 million in potential revenue.

## Key Information

- Built **NovoScribe**, an AI-powered documentation platform using [[Claude]] models on [[AmazonBedrock]], [[ClaudeCode]], and MongoDB Atlas.
- Combines semantic search (Anthropic's contextual retrieval) with domain-expert-approved text to produce regulatory-grade documentation that consistently earns positive regulator feedback.
- **Impact**: documentation that took 10+ weeks now takes 10 minutes (90% reduction in writing time); device verification protocols that needed entire departments now need just one user; review cycles dropped 50%; complete study booklets generated in under a minute (previously months via external agencies).
- With [[ClaudeCode]], even non-technical team members prototype features in hours instead of weeks, letting an 11-person development team expand capabilities without scaling headcount.
- Quote: *"In a highly regulated industry, we can't just throw our data into a large language model and hope for the best. Our conversations with Anthropic guided us on how to securely use Claude for planning, strategic tasks, and code generation."* — Waheed Jowiya, Digitalization Strategy Director.

## Related

- [[ClaudeCode]] — used for non-technical prototyping within NovoScribe's development
- [[AmazonBedrock]] — deployment platform for Claude models in NovoScribe
- [[Claude4.5Sonnet]] — the release cited as driving this transformation
- [[Anthropic]] — model provider
- [[summary-2025-10-01 - How enterprises are driving AI transformation with Claude]] — source case study
- [[HealthcareAI]] — the broader practice Novo Nordisk exemplifies
- [[Pfizer]] — sibling life-sciences customer example
- [[summary-2025-10-30 - Building AI agents for healthcare and life sciences]] — source article
