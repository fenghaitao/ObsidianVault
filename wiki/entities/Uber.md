---
title: "Uber"
type: entity
tags: [company, ride-sharing, arize-customer, hypergrowth, quality]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Taste & Craft： A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @pragmaticengineer.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - How AI is changing Software Engineering： A Conversation with Gergely Orosz, @pragmaticengineer.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260607 - LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize.md"]
last_updated: 2026-06-26
---

## Definition
Uber is a ride-sharing and technology company. Both Tuomas Artman (CTO of Linear) and Gergely Orosz (@pragmaticengineer) are former Uber engineers who draw on their hypergrowth experience to inform modern engineering practices. Uber is also a customer of Arize, using the platform for AI observability and evaluation.

## Key Information
- Arize customer alongside other tech-forward companies like Instacart, Reddit, and Duolingo.
- Uses Arize for monitoring and evaluating AI/ML systems in production.
- **Cadence**: Created the Cadence workflow orchestration project internally; virtually every application at Uber runs on Cadence. Temporal was forked from Cadence.
- **Hypergrowth experience**: Tuomas Artman described Uber's hypergrowth as "I never want to go through again" — fighting fires, keeping infrastructure running, scaling as quickly as possible, trying everything to win a winner-takes-all market.
- **Quality at Uber**: Revenue was the golden metric everyone optimized for. Quality didn't affect revenue until Lyft launched a competing product at the same price point. Early Uber had engineers who cared deeply about quality (e.g., a PR rejected for being "off by two pixels"), but this eroded as the team grew and incentives shifted to revenue.
- **Uber Pool vs Lyft Pool**: Used as a case study in how quality becomes a differentiator only when two products reach feature and price parity.
- Gergely Orosz joined Uber in 2012 and had his first PR reviewed by the first iOS engineer, who measured a UI element and found it two pixels off.
- Had layoffs during COVID that hit Gergely Orosz's team, leading him to start The Pragmatic Engineer
- Many Uber alumni started companies based on internal Uber tech: Temporal (from Cadence), Chronosphere
- Building internal AI infra alongside Airbnb, Intercom, Meta, and Microsoft — custom coding agents, MCP gateways, retooled on-call tooling

## Related
- [[Arize]] — observability platform used by Uber
- [[ArizeAX]] — enterprise Arize product used by Uber
- [[Cadence]] — workflow orchestration project created at Uber
- [[Temporal]] — forked from Cadence
- [[Lyft]] — primary competitor
- [[TuomasArtman]] — former Uber engineer, now CTO of Linear
- [[GergelyOrosz]] — former Uber engineer, author of The Pragmatic Engineer
- [[Hypergrowth]] — experience at Uber
- [[CompetitionThroughQuality]] — concept illustrated by Uber vs Lyft
- [[summary-20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize]] — source
- [[summary-20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal]] — source for Cadence
- [[summary-20260421 - How AI is changing Software Engineering： A Conversation with Gergely Orosz, @pragmaticengineer]] — source (layoffs, spinouts, internal AI infra)
- [[PragmaticEngineer]] — newsletter Gergely started after Uber layoffs
- [[Chronosphere]] — Uber spinout
- [[InternalAIPlatform]] — building custom AI infra
