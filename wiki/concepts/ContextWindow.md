---
title: "ContextWindow"
type: concept
tags: [llm, context, memory, ai]
sources: [raw/03-transcripts/Claude/Claude Code 101/01 - What is Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/07 - Context Management in Claude Code.md, raw/01-articles/claude/2025-08-12 - Claude Sonnet 4 now supports 1M tokens of context.md]
last_updated: 2026-06-28
---

## Definition

The context window is an LLM's working memory -- the maximum amount of text (tokens) it can hold and reason about at once. It can hold a lot, but not everything simultaneously.

## Key Information

- Acts as a constraint on what an LLM can process in a single interaction.
- AI agents work around context window limits by strategically retrieving only relevant information rather than loading everything at once.
- Effective use of Claude Code requires understanding this limitation and structuring prompts and workflows accordingly.
- [[ClaudeEnterprise]] offers a 500K context window, enabling processing of hundreds of sales transcripts, dozens of 100+ page documents, or medium-sized codebases.
- **Retrieval vs. capacity**: a large context window doesn't guarantee accurate retrieval of embedded facts. [[Claude2.1]] (200K tokens) initially showed reluctance to answer based on an "out of place" embedded sentence — see [[LongContextRetrieval]] for the evaluation and the prompting fix that raised accuracy from 27% to 98%.
- [[Claude4Sonnet]] supports a **1 million token context window** (public beta, August 2025) — a 5x increase enabling processing of entire codebases (75,000+ lines), large document sets, and context-aware agents that maintain coherence across hundreds of tool calls. Pricing scales for prompts exceeding 200K tokens; [[PromptCaching]] and [[BatchProcessing]] can offset the additional cost.
- **1M context general availability (March 2026)**: [[Claude4.6Opus|Claude Opus 4.6]] and [[Claude4.6Sonnet|Claude Sonnet 4.6]] reach GA for the full 1M-token context window at standard per-token pricing (no long-context premium multiplier). Opus 4.6 scores 78.3% on MRCR v2, the highest among frontier models at that context length. [[ClaudeCode]] for Max/Team/Enterprise users on Opus 4.6 now defaults to the full window automatically. Media limits expand to 600 images or PDF pages. Available natively on the Claude Platform and via [[AmazonBedrock|Amazon Bedrock]], [[VertexAI|Vertex AI]], and Microsoft Foundry.

### Context Management in Claude Code

- **Auto-compaction:** triggers near the limit, summarizes important details and removes unnecessary tool call results (may lose conversation details).
- **`/compact`:** manual compaction; preserves a summary of previous work while freeing context.
- **`/clear`:** full reset; starts from scratch with no memory of prior conversation.
- **`/context`:** displays context size breakdown by category with a visual graph.
- **Rule of thumb:** compact when continuing on the same feature but running out of context; clear when starting a new feature.
- **Be specific in prompts:** vague prompts force Claude to explore more, consuming more context than a slightly longer but clearer prompt.
- **MCP servers:** all tools load into context by default; disable unrelated ones to save space.
- **Skills:** work like MCP but don't load everything into context.
- **Sub-agents:** run in separate context windows; delegate tasks where only the answer is needed — mental test (April 2026): "will I need this tool output again, or just the conclusion?"
- **CLAUDE.md:** put persistent information here so Claude doesn't rediscover it each session.
- **`/rewind` (double-tap Esc, April 2026):** jumps back to any prior message, dropping later messages from context; preferred over appending a correction to a failed approach — rewind to just after the useful exploration and re-prompt with the learning. Can produce a "summarize from here" handoff note between iterations.
- **Bad compacts (April 2026):** occur when the model can't predict the direction of upcoming work — e.g. autocompact after a long debugging session drops an unrelated warning the user then asks about fixing. Compaction happens exactly when the model is most affected by context rot, so with 1M context there's more room to `/compact` proactively with an explicit description of the next direction rather than waiting for autocompact.
- **`/usage` (April 2026):** slash command showing a user's Claude Code usage; introduced partly because of high variance in how users manage sessions under the 1M-token window.

### Platform-Level Context Management (September 2025)

Anthropic introduced two platform-level features to address context limits in production agents:

- **[[ContextEditing]]**: Automatically removes stale tool calls and results from the context window as an agent approaches token limits. Preserves conversation flow; delivered 29% performance improvement alone and 84% token reduction in a 100-turn web search evaluation.
- **Memory Tool**: File-based CRUD storage that lives outside the context window in developer-managed infrastructure, persisting across conversations. Together with context editing, yields a 39% performance improvement over baseline on internal agentic search evaluations.
- [[Claude4.5Sonnet]] adds built-in context awareness — tracking available tokens throughout a conversation — to power these features.

### Compaction and Memory-Folder Benchmarks (April 2026)

On BrowseComp, Claude's ability to use a compaction budget scaled sharply across generations: Sonnet 4.5 stayed flat at 43% regardless of budget, Opus 4.5 reached 68%, and Opus 4.6 reached 84% under the same setup. Separately, giving Sonnet 4.5 a memory folder (files it writes and later reads) lifted BrowseComp-Plus accuracy from 60.4% to 67.2%. A qualitative illustration: in a long-horizon Pokémon-playing test, Sonnet 3.5 treated memory as an undifferentiated transcript (31 files including near-duplicates after 14,000 steps, still in the second town), while Opus 4.6 at the same step count had 10 files organized into directories, three gym badges, and a distilled `learnings.md` of tactical lessons from its own failures. See [[summary-2026-04-02 - Harnessing Claude’s intelligence]].

### Screenshot-Heavy Agents and Server-Side Compaction (`compact_20260112`, May 2026)

Long-running [[ComputerUse|computer-use]] agents accumulate screenshots fast (~1,000–1,800 tokens each; a 200K window can fill in well under 100 screenshots). Recommended layering: (1) a **rolling buffer** that replaces older image blocks with a `"[Image omitted]"` text placeholder, pruned in *batches* (not one at a time, which invalidates the prompt cache every turn) — suggested defaults `keep_n=3`, `interval=25`; (2) **compaction** once the buffer alone isn't enough, using a structured summarization prompt (user instructions verbatim, task template, constraints, actions taken, errors/fixes, progress, current state, next step) so the agent can resume without re-reading history; (3) the new **`compact_20260112`** server-side beta tool (`context_management.edits`, beta header `compact-2026-01-12`), which accepts a custom `instructions` prompt and an `input_tokens` trigger threshold, with `pause_after_compaction` to retain recent screenshots across compaction events. Because the server drops pre-compaction content on its side while the client's local message array still holds full history, client code must mirror the truncation (drop messages before `message_index_after_compaction`) to keep the client and server views — and any rolling-buffer pruner — aligned. See [[summary-2026-05-13 - Best practices for computer and browser use with Claude]].

## Related

- [[summary-01 - What is Claude Code]] — source summary
- [[summary-07 - Context Management in Claude Code]] — source on context management
- [[summary-2026-05-13 - Best practices for computer and browser use with Claude]] — rolling-buffer screenshot pruning and the compact_20260112 server-side compaction tool
- [[ComputerUse]] — capability driving screenshot-heavy long-horizon context management
- [[ClaudeCode]] — tool that operates within context window constraints
- [[AIAgent]] — paradigm for working around context window limits
- [[CLAUDE-md]] — persistent memory across sessions
- [[ClaudeEnterprise]] — enterprise product with 500K context window
- [[Claude4Sonnet]] — model with 1M token context window (public beta, August 2025)
- [[BatchProcessing]] — 50% additional cost savings when used with long context
- [[PromptCaching]] — reduces latency and cost for repeated long-context requests
- [[summary-2024-09-10 - Claude for Enterprise]] — announcement of enterprise context window
- [[summary-2025-08-12 - Claude Sonnet 4 now supports 1M tokens of context]] — 1M context window announcement
- [[ContextEditing]] — platform feature for automatic stale-content removal from context
- [[AgenticMemory]] — external memory mechanism to extend effective context across sessions
- [[Claude4.5Sonnet]] — model with built-in token tracking for context awareness
- [[summary-2025-09-29 - Managing context on the Claude Developer Platform]] — context editing and memory tool announcement
- [[Claude2.1]] — early 200K-token model whose retrieval behavior motivated long-context prompting research
- [[LongContextRetrieval]] — the retrieval pattern and prompting fix for long-context reluctance
- [[Claude4.6Opus]] — model reaching 1M context GA, highest MRCR v2 score among frontier models
- [[Claude4.6Sonnet]] — sibling model reaching 1M context GA
- [[summary-2026-03-13 - 1M context is now generally available for Opus 4.6 and Sonnet 4.6]] — GA announcement
- [[summary-2026-04-02 - Harnessing Claude’s intelligence]] — compaction and memory-folder benchmarks across model generations
- [[summary-2026-04-15 - Using Claude Code session management and 1M context]] — /rewind, compact-vs-clear decision framework, and bad-compact causes
