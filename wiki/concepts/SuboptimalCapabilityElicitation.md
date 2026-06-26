---
title: "SuboptimalCapabilityElicitation"
type: concept
tags: [ai, capability-elicitation, prompting, agent-design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR.md"]
last_updated: 2026-06-25
---

## Definition
Suboptimal Capability Elicitation is the gap between what an underlying AI model can theoretically do and what it actually achieves in a given tool or deployment, due to insufficient prompt engineering, scaffolding, or integration work.

## Key Information
- METR puts "a huge amount of work" into making agents as performant as possible given underlying models, "churning through a load of AI tokens"
- Commercial tools like Cursor (at the time of the March 2025 study) may not have elicited the full capabilities of the underlying Claude 3.6/3.7 Sonnet models
- This is one hypothesis for why benchmark results (with optimized elicitation) show stronger AI performance than real-world tool usage
- As tools improve their elicitation, the gap between benchmark potential and real-world performance may narrow

## Related
- [[summary-20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR]] — source
- [[METR]] — organization that invests heavily in capability elicitation
- [[PromptLearning]] — technique for improving elicitation
- [[Cursor]] — tool that may have had suboptimal elicitation at study time
