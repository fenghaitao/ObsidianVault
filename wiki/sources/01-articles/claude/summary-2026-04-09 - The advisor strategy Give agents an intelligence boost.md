---
title: "summary-2026-04-09 - The advisor strategy Give agents an intelligence boost"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-04-09 - The advisor strategy Give agents an intelligence boost.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic formalizes the "advisor strategy" — pairing a smaller, cost-effective executor model (Sonnet or Haiku) that runs a task end-to-end with a larger model (Opus) that only advises when the executor hits a decision it can't reasonably solve — as a first-class API primitive: the `advisor` tool (`advisor_20260301`). The advisor never calls tools or produces user-facing output; it only receives curated shared context and returns a plan, correction, or stop signal, after which the executor resumes. This inverts the common orchestrator-subagent pattern (a large model decomposing and delegating to smaller workers): here a smaller model drives the whole run and escalates selectively, so frontier-level reasoning is invoked only when needed while the rest of the run stays at executor-level cost. The tool is a single addition to the `tools` array in a `/v1/messages` call — no extra round-trips or custom orchestration — and is available now in beta on the Claude Platform.

## Key Points

- Declared as `advisor_20260301` in the `tools` array of a Messages API request; the executor model (e.g. `claude-sonnet-4-6`) decides when to invoke it, and the advisor model (e.g. `claude-opus-4-6`) is specified via the tool config, with `max_uses` capping calls per request.
- Handoff happens inside a single `/v1/messages` request: curated context is routed to the advisor, a plan is returned, and the executor continues — no extra round-trips or manual context management required.
- **Pricing**: advisor tokens are billed at the advisor model's rates, executor tokens at the executor model's rates, and are reported separately in the usage block. Since the advisor typically only generates a short plan (~400-700 text tokens) while the executor handles the full output at its lower rate, total cost stays well below running the advisor model end-to-end.
- **Benchmark results (Sonnet executor + Opus advisor vs. Sonnet alone)**: +2.7 percentage points on SWE-bench Multilingual while reducing cost per agentic task by 11.9%; improved scores on BrowseComp and Terminal-Bench 2.0 while costing less per task than Sonnet alone.
- **Haiku as executor**: with an Opus advisor, BrowseComp score reached 41.2% (more than double Haiku's solo score of 19.7%). This trails Sonnet solo by 29% in score but costs 85% less per task — positioned as a strong option for high-volume tasks balancing intelligence and cost.
- Works alongside other tools in the same agent loop (web search, code execution, etc.) — the advisor tool is just another entry in the `tools` array.
- Anthropic recommends running an existing eval suite against three configurations to decide whether to adopt it: Sonnet solo, Sonnet executor + Opus advisor, and Opus solo.
- **Anomaly**: the raw article contains duplicated boilerplate lines (the opening summary sentence and the "Pair Opus as an advisor..." line appear twice in a row) and trailing page-widget cruft ("Get the developer newsletter... Delivered monthly to your inbox.") — standard scraped-page artifacts, not prompt injection, and not treated as content.

## Related

- [[AdvisorStrategy]] — the concept this article formally introduces as a named API tool
- [[Anthropic]] — publisher of this article
