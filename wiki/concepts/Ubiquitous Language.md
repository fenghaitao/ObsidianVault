---
title: "Ubiquitous Language"
type: concept
tags: [domain-driven-design, ddd, communication, ai, software-design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - ＂Software Fundamentals Matter More Than Ever＂ — Matt Pocock.md"]
last_updated: 2026-06-26
---

## Definition
Ubiquitous Language is a concept from Domain-Driven Design (DDD) where conversations among developers, expressions in code, and conversations with domain experts are all derived from the same domain model. It is a shared terminology that ensures everyone — including AI — uses the same terms with the same meanings.

## Key Information
- From Domain-Driven Design by Eric Evans
- Establishes a common vocabulary between developers, domain experts, and now AI agents
- Matt Pocock created a "Ubiquitous Language" skill that scans a codebase for terminology and creates a markdown file with shared terms
- The skill produces markdown tables with all terminology that both the human and AI agree on
- Pocock keeps the ubiquitous language file open during planning and "grilling" sessions with AI
- Reading AI thinking traces showed that ubiquitous language not only improves planning but allows the AI to think less verbosely
- Results in implementations that are more aligned with what was actually planned
- Addresses the failure mode where AI is "way too verbose" and talks at cross-purposes with the developer
- Analogous to the communication gap between developers and domain experts in traditional software development

## Related
- [[summary-20260423 - ＂Software Fundamentals Matter More Than Ever＂ — Matt Pocock]] — source transcript
- [[MattPocock]] — creator of the Ubiquitous Language skill
- [[Design Concept]] — complementary concept for shared understanding
- [[Grill Me]] — used together with ubiquitous language
- [[Skills]] — the Ubiquitous Language skill is part of macpocockskills
