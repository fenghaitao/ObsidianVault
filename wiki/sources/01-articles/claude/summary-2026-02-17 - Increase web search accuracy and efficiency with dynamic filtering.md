---
title: "summary-2026-02-17 - Increase web search accuracy and efficiency with dynamic filtering"
type: source
tags: [source, web-search, dynamic-filtering, code-execution, api]
sources: ["raw/01-articles/claude/2026-02-17 - Increase web search accuracy and efficiency with dynamic filtering.md"]
last_updated: 2026-07-04
---

## Core Summary

Alongside [[Claude4.6Opus|Claude Opus 4.6]] and [[Claude4.6Sonnet|Sonnet 4.6]], Anthropic's web search and web fetch tools gained **dynamic filtering**: Claude now writes and executes code to post-process search results, filtering out irrelevant content before it reaches the context window, instead of reasoning over full raw HTML. Across BrowseComp and DeepSearchQA, this improved accuracy by an average of 11% while using 24% fewer input tokens.

## Key Points

- **Mechanism**: extends the same code-execution/programmatic-tool-calling technique Anthropic previously found effective in other agentic workflows — Claude writes code to parse, filter, and cross-reference results, "like an actual researcher," instead of reasoning over unfiltered HTML in context.
- **BrowseComp** (finding one specific, deliberately hard-to-find fact): accuracy rose from 33.3% → 46.6% for Sonnet 4.6 and 45.3% → 61.6% for Opus 4.6 with dynamic filtering enabled.
- **DeepSearchQA** (finding many correct answers via systematic multi-step search, scored by F1): rose from 52.6% → 59.4% for Sonnet 4.6 and 69.8% → 77.3% for Opus 4.6.
- **Token cost caveat**: price-weighted tokens decreased for Sonnet 4.6 on both benchmarks but increased for Opus 4.6 — Anthropic recommends evaluating against representative production queries rather than assuming savings.
- Turned on by default with the new web search/web fetch tools (`web_search_20260209`, `web_fetch_20260209`) on Sonnet 4.6 and Opus 4.6 via the API.
- Customer example: [[Poe]] (Quora) found Opus 4.6 with dynamic filtering achieved the highest accuracy on internal evals against other frontier models.
- Several other agentic tools graduated to general availability alongside this release: code execution, memory, programmatic tool calling, tool search, and tool use examples.

## Related

- [[WebSearch]] — the concept this article substantially updates
- [[CodeExecutionTool]] — the underlying technique dynamic filtering extends
- [[Claude4.6Opus]] — model benchmarked
- [[Claude4.6Sonnet]] — model benchmarked
- [[Poe]] — cited customer example
