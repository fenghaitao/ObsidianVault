---
title: "Microservices Architecture"
type: concept
tags: [architecture, software-engineering, infrastructure, security]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20240708 - Getting To Staff (IC6) at FAANG Panel (Full, Sept 2023).md"]
last_updated: 2026-07-21
---

## Definition

Microservices Architecture is a software architecture pattern where applications are built as collections of small, independently deployable services. It creates both advantages (individual ownership) and challenges (security complexity across many services).

## Key Information

- Zach described the duality at Netflix: "One of the things that's awesome about microservices is you have this individual ownership; one of the things that's terrible about microservices is security"
- At Netflix's scale, instead of one app to secure, there were "3,000 or 4,000 or 5,000 apps to hack, each with their own different vulnerabilities and code-based problems"
- This security challenge was a "big nightmare" that Netflix was trying to figure out
- Zach's Asset Inventory Knowledge Graph was built specifically to address this microservices security challenge
- The Knowledge Graph mapped all applications, code bases, data sets, and how they were connected, providing visibility across the microservices landscape
- This illustrates how infrastructure-level problems at scale can create staff-level scope

## Related

- [[summary-20240708 - Getting To Staff (IC6) at FAANG Panel (Full, Sept 2023)]] — source summary
- [[Netflix]] — company known for microservices architecture
- [[Knowledge Graph]] — the solution built to address microservices security
- [[Zach Wilson]] — built the Knowledge Graph at Netflix
- [[Staff Engineer]] — the level of the work addressing this challenge
