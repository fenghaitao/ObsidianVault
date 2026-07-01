---
title: "Vibe Checking"
type: concept
tags: [eval, testing, informal, anti-pattern]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md"]
last_updated: 2026-06-30
---

## Definition
Vibe checking is the informal practice of testing AI features by running a few queries and subjectively judging whether the output "looks right." It is the anti-pattern that formal evals are designed to replace — it doesn't scale, doesn't catch regressions, and doesn't run in CI.

## Key Information
- The "vibes problem": teams build an AI feature, test with a few queries, go "does this look right?", ship it, and discover failures on unexpected inputs
- Failures occur on: edge cases, adversarial inputs, and most commonly, users asking questions that are "dimmer than you were expecting" — using unexpected vocabulary
- Vibe checking doesn't scale because: it doesn't catch regressions, doesn't run in CI, and can't test prompt changes systematically
- Without evals, changing the system prompt to fix a tone issue might cause hallucinations that go undetected until user reports
- Every prompt change potentially affects every kind of input — vibe checking can't cover the combinatorial space
- Model upgrades are especially dangerous without evals: "Sonnet 4.5 does not work for Sonnet 4.6"
- The arc that real teams follow: start by shipping fast with vibes → discover it doesn't scale → move to formal evals
- Examples: Dscript, Bolt, Anthropic (with Claude Code) all followed this pattern
- The time to adopt evals is when "vibe checking becomes a bottleneck to improvement"

## Related
- [[Code Evals]] — the formal replacement for vibe checking
- [[LLMAsJudge]] — formal evaluation technique
- [[EvalEngineering]] — the practice of moving beyond vibes
- [[Capability Evals]] — systematic approach to improvement
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
