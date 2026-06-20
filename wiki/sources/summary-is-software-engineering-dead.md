---
title: "summary-is-software-engineering-dead"
type: source
tags: [source, original-material, intent-engineering, industry-analysis, ai-coding]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260305 - Is Software Engineering Finally Dead.md"]
last_updated: 2026-06-20
---

## Core Summary

[[ColeMedin]] argues software engineering is **not** dying — the coding *part* is increasingly automated, but the role evolves and endures. Two caveats the hype ignores: (1) enterprise adoption of AI coding is far slower than headlines suggest, and (2) software engineering is much more than coding. He traces the discipline's evolution **prompt engineering → [[ContextEngineering]] → [[IntentEngineering]]**, showing how working with agents increasingly *is* senior-engineering work. Tech-leader "SWE is dead" claims are dismissed as biased ("follow the money").

## Key Points

- **The recurring "6 months from dead" narrative**: Dario Amodei (Anthropic) said AI would write 90% of code within 6 months (March 2025) — didn't happen — then claimed SWEs could "go extinct in 2026." Jensen Huang ("kids shouldn't learn to code"), Sam Altman ("mastering AI is the new learn to code"), and the Microsoft AI CEO ("all white-collar tasks automated within ~18 months") echo it.
- **Follow the money (bias)**: these leaders benefit directly — Anthropic's valuation went **$61.5B → $380B** in under a year; Nvidia's Jensen ~$3B (2019) → ~$90B (2024); OpenAI >$730B with Sam in line for a ~$10B equity stake. Cole calls them "living in a bubble."
- **Boris Cherny nuance** (Claude Code creator): said "coding is largely solved" on podcasts (Y Combinator, Lenny's), widely *misinterpreted*. He clarified on X that software engineering is **more important than ever**: "someone has to prompt the [agents], talk to the customers, coordinate with other teams, decide what to build next." Cole notes the same-company contradiction (Dario vs Boris) is itself evidence of bubble-think.
- **The evolution to [[IntentEngineering]]**: prompt engineering (word a single prompt) → context engineering (build a whole context ecosystem) → **intent engineering** (Nate B. Jones): be explicit about success criteria, how the agent validates its own work, and alignment on *what* is being built — so the code is correct **and** it's the right thing. Each step looks more like senior software engineering ("everything except the coding is our responsibility").
- **Enterprise adoption is slow** (Cole trains teams firsthand): corporate red tape, procurement, security reviews, and resistant senior engineers (who know LLMs hallucinate and introduce security issues). An individual can adopt Cole's system in a day; a company must turn it into a team-wide standard, taking weeks-to-months. Data on the disconnect:
  - 90% of engineering teams "use AI" — but only **51%** of professional developers use AI tools *daily* (Stack Overflow).
  - **76%** of executives believe their teams embraced AI vs only **52%** of engineers.
  - **21%** of AI licenses go underutilized.
- **Cole's own arc**: refused AI coding until **Nov 2024** (first tool: Windsurf), then over ~6 months built his **[[PIVLoop]]** (plan-implement-validate) system; now delegates nearly all coding while owning architecture, requirements-translation, code review, and validation — "not vibe coding."
- **Recommendations**: never [[VibeCoding|vibe code]] to production; keep technical skills sharp (disagrees with Jensen — learning to code matters for review); use the agent as an **educator, not just a coder** to keep understanding of your codebase; don't cede agency — the engineers who thrive use AI as a force multiplier while retaining deep craft, while those who fully give up agency "crumble" when AI errs.

## Related

- [[IntentEngineering]] — the latest evolution beyond context engineering
- [[ContextEngineering]] — the middle stage of the evolution
- [[AgenticEngineering]] — the practitioner discipline that replaces "coding" with system-design work
- [[PIVLoop]] — Cole's plan-implement-validate system
- [[ClaudeCode]] — Boris Cherny's "coding largely solved" nuance
- [[Anthropic]] — valuation/bias datapoint
- [[VibeCoding]] — the thing not to do in production
