---
title: "summary-2026-04-16 - Best practices for using Claude Opus 4.7 with Claude Code"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-04-16 - Best practices for using Claude Opus 4.7 with Claude Code.md"]
last_updated: 2026-07-04
---

## Core Summary

This Anthropic blog post gives practical guidance for adapting Claude Code usage to [[Claude4.7Opus|Opus 4.7]], the successor to [[Claude4.6Opus|Opus 4.6]] and Anthropic's strongest generally-available model for coding, enterprise workflows, and long-running agentic tasks at time of publication. Two underlying changes — an updated tokenizer and a tendency to think more at higher effort levels (especially on later turns in long sessions) — alter token usage relative to Opus 4.6, so prompts and harnesses tuned for the old model may need retuning. The post recommends treating Opus 4.7 like a capable engineer being delegated to rather than a pair programmer guided line-by-line, introduces a new `xhigh` effort level (between `high` and `max`) that is now Claude Code's default, and explains that Opus 4.7 uses [[AdaptiveThinking|adaptive thinking]] rather than fixed-budget extended thinking. It also flags default-behavior shifts versus Opus 4.6: less verbose responses calibrated to task complexity, fewer tool calls with more reasoning per call, and fewer subagents spawned by default unless explicitly directed to fan out.

## Key Points

- **Opus 4.7 capabilities**: handles ambiguity better than Opus 4.6, is more capable at finding bugs and reviewing code, carries context across sessions more reliably, and reasons through ambiguous tasks with less direction; performs better on long-running tasks (complex multi-file changes, ambiguous debugging, service-wide code review, multi-step agentic work).
- **Token usage drivers**: an updated tokenizer plus a greater proclivity to think at higher effort levels — especially on later turns in longer sessions — increase token consumption versus Opus 4.6.
- **Interactive vs. autonomous agents**: in interactive (multi-turn) settings Opus 4.7 reasons more after each user turn, improving coherence, instruction-following, and code quality over long sessions but using more tokens; behavior differs for single-turn autonomous/asynchronous agents.
- **New effort level `xhigh`**: sits between `high` and `max`, trading more reasoning for latency on hard problems; now the **default** effort level for Opus 4.7 in Claude Code and the recommended setting for most agentic coding work, especially intelligence-sensitive tasks (API/schema design, legacy-code migration, large-codebase review). Existing Claude Code users who haven't manually set effort are auto-upgraded to `xhigh` but can still override it. Users are encouraged to experiment with effort per-task rather than porting over old settings, and can toggle effort levels mid-task.
- **Adaptive thinking replaces fixed-budget extended thinking**: Opus 4.7 does not support extended thinking with a fixed token budget; instead thinking is optional at each step, letting the model decide when more thinking is worthwhile, skip it when unhelpful, and invest tokens where they matter most — improving speed and UX over a full agentic run. Adaptive thinking has improved in this release and is less prone to overthinking than before. Users wanting more control over the thinking rate should prompt for it directly.
- **Default-behavior changes vs. Opus 4.6** (relevant to prompts/harnesses tuned for the old model):
  - Response length is calibrated to task complexity rather than being default-verbose; users needing a specific length/style should state it explicitly, with positive voice examples working better than "don't do this" negative instructions.
  - The model calls tools less often and reasons more; users wanting more aggressive tool use (e.g., more search/file reading) should explicitly describe when and why a tool should be used.
  - The model spawns fewer subagents by default, being more judicious about delegation; users whose use case benefits from parallel subagents (fanning out across files/independent items) should spell that out explicitly — e.g., don't spawn a subagent for work completable directly in one response, but do spawn multiple subagents in the same turn when fanning out.
- **Recommendation**: keep effort at `xhigh` and let the first turn run further before intervening; further guidance pointed to a companion "Opus 4.7 prompting guide" and an article on context/session management in Claude Code (neither linked with retrievable content in this article).
- **Anomaly**: the raw source is a scraped marketing/blog page containing boilerplate duplication (the description sentence is repeated verbatim in the body) and a trailing newsletter-signup widget ("Get the developer newsletter... Delivered monthly to your inbox") — noted as scraping artifacts, not content to act on. No prompt-injection attempt was present in this file.

## Related

- [[Claude4.7Opus]] — the model this article provides best practices for
- [[Claude4.6Opus]] — predecessor model being replaced/upgraded from
- [[ClaudeCode]] — the tool whose defaults (effort level, subagent behavior) this article covers
- [[AdaptiveThinking]] — the thinking paradigm Opus 4.7 uses instead of fixed-budget extended thinking
- [[ClaudeCodeSubagents]] — subagent delegation behavior changed in this release
