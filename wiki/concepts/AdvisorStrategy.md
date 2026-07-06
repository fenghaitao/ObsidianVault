---
title: "AdvisorStrategy"
type: concept
tags: [claude, cost-optimization, model-strategy, api]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London/01 - Code with Claude London 2026： Opening Keynote.md]
last_updated: 2026-06-23
---

## Definition

The advisor strategy is a Claude API pattern that splits execution from advising: a smaller model (Haiku or Sonnet) executes tasks, and when it needs help, it reaches out to a larger model (Opus) for advice. This delivers frontier model quality at significantly lower cost.

## Key Information

- **How it works:** update the tools array on the Messages API. The smaller model executes; when stuck, it calls the larger model as an advisor.
- **Results:** Sonnet + Opus advisor performed better than Sonnet alone and was cheaper because Opus advised it to complete work more efficiently.
- **Eve Legal case study:** achieved frontier model quality at 5x lower cost using the advisor strategy.
- **Use cases:** premium product experiences where cost matters, extremely high-volume agentic workloads where ROI must be tracked.
- **Implementation:** simple -- just update the tools configuration; no complex orchestration needed.
- **Productized as the `advisor` tool** (`advisor_20260301`, April 2026): a server-side Messages API tool. The executor model (e.g. Sonnet 4.6) calls tools/iterates on its own; the advisor (e.g. Opus 4.6) never calls tools or produces user-facing output — it only returns a plan, correction, or stop signal from curated shared context, then the executor resumes. `max_uses` caps advisor calls per request; advisor and executor tokens are billed separately at each model's own rate, and reported separately in the usage block. Advisor responses are typically short (400-700 text tokens), keeping total cost well below running the advisor model end-to-end.
- **Inverts the orchestrator-subagent pattern**: rather than a large orchestrator decomposing work for smaller workers, a smaller executor drives the entire run and escalates selectively — no decomposition, worker pool, or orchestration logic required. See [[MultiAgentSystem]].
- **Benchmarks (Sonnet executor + Opus advisor vs. Sonnet alone)**: +2.7pp on SWE-bench Multilingual with an 11.9% cost reduction per agentic task; improved BrowseComp and Terminal-Bench 2.0 scores at lower cost than Sonnet alone.
- **Haiku as executor**: Opus-advised Haiku scored 41.2% on BrowseComp (vs. 19.7% solo — more than double), trailing Sonnet solo by 29% in score but costing 85% less per task — a fit for high-volume, cost-sensitive workloads.
- Available now in beta natively on the Claude Platform; Anthropic recommends evaluating three configurations before adopting: Sonnet solo, Sonnet+Opus advisor, Opus solo.
- **Applied to [[ComputerUse|computer use]] (May 2026)**: pairs a mechanical executor (e.g. Sonnet 4.6) with a higher-intelligence advisor (e.g. Opus 4.7) consulted mid-generation for planning/course-correction moments — choosing a tab, recovering from an unexpected modal, abandoning a failing strategy — while the bulk of token generation stays at executor rates. The advisor runs without tools and without context management (text advice only). Two operational gotchas: if the advisor tool is later dropped from the tools array (cap hit, config/model change), prior `server_tool_use`/`advisor_tool_result` blocks become orphaned and cause a 400 error unless stripped first; and because the executor can forget the advisor exists on long sessions, a ~20-turn reminder nudge helps keep it in use. See [[summary-2026-05-13 - Best practices for computer and browser use with Claude]].

## Related

- [[summary-01 - Code with Claude London 2026： Opening Keynote]] — keynote where it was introduced
- [[summary-10 - Picking the right model]] — related model selection framework
- [[ClaudeManagedAgents]] — platform that can leverage this strategy
- [[summary-2026-04-09 - The advisor strategy Give agents an intelligence boost]] — dedicated article formalizing the advisor tool, with benchmarks and API mechanics
- [[MultiAgentSystem]] — the orchestrator-subagent pattern this strategy explicitly inverts
- [[summary-2026-05-13 - Best practices for computer and browser use with Claude]] — advisor tool applied to a computer-use executor/advisor pairing, with orphaned-block and reminder-nudge gotchas
- [[ComputerUse]] — capability where this executor/advisor pattern is applied
