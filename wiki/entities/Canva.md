---
title: "Canva"
type: entity
tags: [company, design, platform, ai]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - Japan/02 - Code with Claude 2026 ｜ Tokyo.md, "raw/01-articles/claude/2026-02-12 - Claude Enterprise, now available self-serve.md", "raw/01-articles/claude/2026-06-17 - Claude Design now stays on brand for daily work.md", raw/01-articles/claude/2026-06-18 - Centrally manage authorization for MCP connectors.md]
last_updated: 2026-07-07
---

## Definition

Canva is an Australian graphic design and visual communication platform used by hundreds of millions of people. Canva AI 2.0 is a complex agentic system built on Claude that orchestrates design agents, code agents, and hundreds of tools behind a simple text interface.

## Key Information

- Has used Claude since the Sonnet 3 model days.
- Canva AI 2.0 orchestrates design agents, code agents (Canva Code), and hundreds of tools (image generation, background removal, etc.).
- **Key lessons from building with Claude:**
  - Design is subjective; human touch matters (average design edited ~110 times before publishing).
  - Latency correlates more strongly with user satisfaction than quality metrics.
  - Flexible deployment (Bedrock, Vertex, Foundry) enables AWS-native integration with IAM roles and cost tracking.
  - Distributed AI team model: each product group owns their AI features.
- Canva Code lets non-coders create interactive mini-apps within designs using Claude.
- ~5,500 employees; broad range of design jobs to be done.
- Uses [[ClaudeEnterprise|Claude Enterprise]]. Samantha Garrett, Head of the AI & Automation Platform team: "Never before have we seen new technologies adopted so quickly and integrated so meaningfully as part of the day-to-day."
- **Skill-from-connector distribution (April 2026)**: Canva is cited as one of the providers (with Notion and Sentry) that publishes a companion skill alongside its MCP server in Claude's connector directory. See [[ModelContextProtocol]].
- **Enterprise-Managed Authorization (June 2026):** Canva was among the MCP providers supporting [[EnterpriseManagedAuthorization|EMA]] at its launch, enabling admins to provision the Canva connector centrally through identity provider groups and roles.

## Related

- [[summary-02 - Code with Claude 2026 ｜ Tokyo]] — Canva presentation source
- [[ClaudeFable5]] — the model powering Canva AI
- [[Anthropic]] — the company behind Claude
- [[ClaudeEnterprise]] — the plan Canva uses
- [[summary-2026-02-12 - Claude Enterprise, now available self-serve]] — source article
- [[summary-2026-04-22 - Building agents that reach production systems with MCP]] — skill-from-connector distribution example
- [[ClaudeDesign]] — exports to Canva as a connector destination
- [[summary-2026-06-17 - Claude Design now stays on brand for daily work]] — source listing Canva as a connector
- [[EnterpriseManagedAuthorization]] — enterprise auth mechanism Canva's MCP connector supports
- [[summary-2026-06-18 - Centrally manage authorization for MCP connectors]] — EMA launch announcement
