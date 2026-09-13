---
title: "Knowledge Graph"
type: concept
tags: [data-engineering, infrastructure, graph-database, security]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20240708 - Getting To Staff (IC6) at FAANG Panel (Full, Sept 2023).md"]
last_updated: 2026-07-21
---

## Definition

A Knowledge Graph is a graph database that describes entities and their relationships. In the context of the panel, Zach Wilson built a Knowledge Graph at Netflix called Asset Inventory that mapped all applications, code bases, data sets, and employees and how they were connected.

## Key Information

- Zach built this at Netflix over two years as the project that Airbnb recognized as staff-level work
- It was designed to address Netflix's microservices security challenge: with 3,000-5,000 apps, each with potential vulnerabilities, a unified view of infrastructure was critical
- The system described: all applications, code bases, data sets, and employees at the company, and how they're all connected and interact with one another
- Zach described it as "this big ass knowledge graph of everything"
- The project was particularly intense and took two years to complete
- This project was a key pivot in Zach's career — he transitioned from detection work to this infrastructure project because it had more "branching use cases" and better promotion potential
- The Knowledge Graph enabled security teams to understand the full scope of the company's infrastructure and identify vulnerabilities across the microservices landscape

## Related

- [[summary-20240708 - Getting To Staff (IC6) at FAANG Panel (Full, Sept 2023)]] — source summary
- [[Zach Wilson]] — built the Asset Inventory Knowledge Graph
- [[Netflix]] — where the project was built
- [[Microservices Architecture]] — the context that created the need for this system
- [[Staff Engineer]] — the level of work this project represented
- [[Asset Inventory]] — the name of the project at Netflix
