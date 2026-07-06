---
title: "Claude Opus 4.6"
type: entity
tags: [claude, model, anthropic, llm, foundation-model, opus, finance, web-search]
sources: ["raw/01-articles/claude/2026-02-05 - Advancing finance with Claude Opus 4.6.md", "raw/01-articles/claude/2026-02-09 - Behind the model launch What customers discovered testing Claude Opus 4.6 early.md", "raw/01-articles/claude/2026-02-17 - Increase web search accuracy and efficiency with dynamic filtering.md"]
last_updated: 2026-07-04
---

## Definition

Claude Opus 4.6 is Anthropic's flagship model release (February 2026), positioned as a substantial step forward in financial reasoning, multitasking, sustained multi-step focus, and agentic web research.

## Key Information

- **Finance benchmarks**: +23 percentage points over Claude Sonnet 4.5 on Anthropic's internal ~50-task Real-World Finance evaluation; state-of-the-art 60.7% on Vals AI's Finance Agent (SEC filings research, +5.47% over Opus 4.5) and 76.0% on Vals AI's TaxEval.
- **Legal benchmark**: 90.2% on Harvey's BigLaw Bench — the first Anthropic model to break 90%, with 40% of tasks scoring perfectly.
- **Web search**: with [[WebSearch|dynamic filtering]] enabled, accuracy on BrowseComp rose from 45.3% to 61.6% and DeepSearchQA F1 from 69.8% to 77.3%.
- **Customer-reported qualitative gains**: diagnosed a bug on the first try that failed five-plus attempts with the previous model (bolt.new); improved instruction-following and one-shot large-scale porting (TypeScript → Ruby at Shopify); increased autonomy and longer safely-delegable task horizons (Lovable, Shopify).
- Powers new/updated products: [[ClaudeCowork|Cowork]] first-pass deliverables, [[ClaudeCode|Claude in Excel]] (complex model handling, pivot tables, finance-grade formatting), and the new Claude in PowerPoint (research preview beta).
- **1M context general availability (March 2026)**: full 1M-token context window at standard pricing ($5/$25 per million tokens) across the entire window, no long-context premium multiplier. Scores 78.3% on MRCR v2, the highest among frontier models at that context length.
- **METR time horizon**: completes software tasks taking a human ~12 hours about half the time — a ~41x jump from Sonnet 3.5 (new)'s ~21-minute time horizon 16 months earlier. Reliably one-shots Excalidraw feature requests (Claude Code's internal capability test) live on stage, versus only occasional success with [[Claude4Opus|Opus 4]]. System prompt and tool descriptions cut 20% relative to prior models. See [[summary-2026-03-19 - Product management on the AI exponential]].
- Supports [[ClaudeCode]]'s auto mode (March 2026), a classifier-gated permissions mode. See [[PermissionModes]].
- Vision capabilities used by TARA (Claude Code hackathon winner, April 2026) to analyze dashcam road footage for infrastructure investment appraisal — identifying surface conditions, distress patterns, and pedestrian/cyclist activity frame-by-frame. See [[TARA]].

## Related

- [[Claude4.6Sonnet]] — sibling model released alongside Opus 4.6
- [[ContextWindow]] — 1M-token context window reaching general availability
- [[ClaudeCode]] — now defaults to 1M context automatically for Max/Team/Enterprise users on this model
- [[METR]] — benchmark org measuring this model's time horizon
- [[PermissionModes]] — auto mode compatibility
- [[summary-2026-03-13 - 1M context is now generally available for Opus 4.6 and Sonnet 4.6]] — source summary
- [[summary-2026-03-19 - Product management on the AI exponential]] — METR benchmark citation
- [[summary-2026-03-24 - Auto mode for Claude Code]] — auto mode compatibility announcement
- [[TARA]] — hackathon project using this model's vision capabilities
- [[summary-2026-04-20 - Meet the winners of our Built with Opus 4.6 Claude Code hackathon]] — hackathon roundup
- [[WebSearch]] — dynamic filtering benchmarked on this model
- [[Harvey]] — BigLaw Bench customer testing this model
- [[BoltNew]] — early-access customer testing this model
- [[Shopify]] — early-access customer testing this model
- [[Lovable]] — early-access customer testing this model
- [[ClaudeCowork]] — product delivering Opus 4.6's finance capabilities
- [[summary-2026-02-05 - Advancing finance with Claude Opus 4.6]] — finance-focused launch article
- [[summary-2026-02-09 - Behind the model launch What customers discovered testing Claude Opus 4.6 early]] — customer early-access testing article
- [[summary-2026-02-17 - Increase web search accuracy and efficiency with dynamic filtering]] — dynamic filtering benchmarks
