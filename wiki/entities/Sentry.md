---
title: "Sentry"
type: entity
tags: [company, monitoring, error-tracking, observability, agent-monitoring]
sources:
  - "raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil.md"
  - "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.md"
  - "raw/03-transcripts/aiDotEngineer/Channel Only/20260527 - The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry.md"
  - "raw/03-transcripts/aiDotEngineer/Channel Only/20260527 - Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry.md"
last_updated: 2026-06-30
---

## Definition
Sentry is a full observability platform that started with error and performance monitoring and has grown to include metrics, profiling, and agentic monitoring tools. Founded in 2010, it has 15+ years of code, approximately 400 employees globally, and serves 100,000+ organizations. Sentry is fair source — external contributors can contribute to the codebase. Armin Ronacher (creator of Flask) previously worked at Sentry before leaving in April 2024. Priscila Andre de Oliveira, a Senior Software Engineer at Sentry, describes the company as "going all in AI" with multiple internal AI tools.

## Key Information
- Full observability platform: error monitoring, performance monitoring, metrics, profiling, and agentic monitoring
- Founded in 2010; 15+ years of code
- ~400 employees globally across 4 offices
- 100,000+ organizations depend on the codebase
- ~100 PRs merged every day
- Fair source — external contributors can contribute
- Constantly deprecating components, adding new components, adding new lint rules
- Armin Ronacher's previous employer (left April 2024)
- "Going all in AI" — multiple internal AI tools built during hackathons
- Daniel Szoke is the Rust SDK maintainer at Sentry; presented at AI Engineer Summit 2026 on Rust as the ideal language for vibe coding
- Sentry was a sponsor of the AI Engineer Summit, with a booth and agent monitoring features

### Sentry Internal AI Tools
- **Abacus**: Tracks AI usage internally at Sentry
- **Warden**: A code review agent that operates on PRs
- **Junior**: A Slack bot that analyzes threads reporting bugs or UI issues and creates PRs to fix them
- **AI SDK Testing Repository**: A repository for testing AI integrations where contributors are instructed to only prompt, never code directly

### Quality Practices
- Ran a three-month "quality quarter" focused on: removing `any` types from TypeScript, eliminating TODO comments, simplifying code, removing unused feature flags
- Priscila Andre de Oliveira advocates for shipping "keynote code" (high quality) over "slop code"

## Related
- [[summary-20260418 - The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil]] — source transcript
- [[summary-20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop]] — source (used alongside Raindrop)
- [[summary-20260527 - The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry]] — source transcript
- [[summary-20260527 - Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry]] — source transcript
- [[ArminRonacher]] — former employee
- [[DanielSzoke]] — Rust SDK maintainer
- [[Priscila Andre de Oliveira]] — Senior Software Engineer, speaker
- [[Earendil]] — company Ronacher co-founded after leaving
- [[Raindrop]] — complementary agent observability platform
- [[LogRocket]] — used alongside Sentry at Raindrop
- [[Quality Quarter]] — Sentry's three-month technical debt cleanup initiative
- [[Keynote Code]] — quality standard advocated at Sentry
