---
title: "summary-2026-04-30 - Lessons from building Claude Code Prompt caching is everything"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-04-30 - Lessons from building Claude Code Prompt caching is everything.md"]
last_updated: 2026-07-04
---

## Core Summary

Thariq Shihipar (Claude Code team) shares engineering lessons from building [[ClaudeCode|Claude Code]]'s harness around [[PromptCaching|prompt caching]], framing it as the foundation the entire product is built on: Anthropic tracks the prompt cache hit rate as an alerting metric and declares SEVs (incidents) when it drops too low, because a high hit rate both cuts cost and enables more generous subscription rate limits. Since caching works by exact-prefix matching up to each `cache_control` breakpoint, the article works through several unintuitive consequences and the design patterns Claude Code uses to avoid cache breaks: ordering static content before dynamic content; pushing time-sensitive or file-state updates into a `<system-reminder>` tag in the next turn instead of editing the system prompt; treating model switches as expensive because caches are model-specific (so mid-conversation model switches should go through a subagent "hand-off" message rather than direct in-place switching); never changing the tool set mid-conversation (the reason Plan Mode is implemented as two toggle tools, EnterPlanMode/ExitPlanMode, rather than swapping in a read-only tool subset); using the tool search tool's `defer_loading` stub mechanism instead of removing MCP tools to keep large tool sets cheap without invalidating the cache; and, for [[ContextWindow|compaction]], "cache-safe forking" — sending the compaction call with the exact same system prompt/tools/history as the parent conversation (just appending a compaction-request user message) so the cache still applies, rather than a naive separate summarization call with a different system prompt and no tools, which would be fully uncached and disproportionately expensive on exactly the long conversations that need compaction most. The article notes these compaction-caching patterns have since been built directly into the Claude [[MessagesAPI|API]]'s native compaction feature so other developers can reuse them.

## Key Points

- Anthropic runs alerts on Claude Code's prompt cache hit rate and declares SEVs (incidents) if it drops too low — cache hit rate is treated as a first-class reliability metric, not just a cost optimization.
- A high cache hit rate both decreases direct API cost and lets Anthropic offer more generous rate limits on subscription plans.
- Prompt caching works via prefix matching: the API caches everything from the start of the request up to each `cache_control` breakpoint, so requests should be structured "static content first, dynamic content last" to maximize shared-prefix cache hits across sessions.
- Named causes of accidental cache breaks at Claude Code: putting an in-depth timestamp in the static system prompt, non-deterministic shuffling of tool definition order, and updating tool parameters (e.g., changing which agents the Agent tool can call).
- Recommended fix for stale/dynamic prompt info: don't edit the system prompt (causes a cache miss); instead pass the updated information via a `<system-reminder>` tag in the next user message or tool result, preserving the cache.
- Prompt caches are model-specific. Example given: 100k tokens into an Opus conversation, answering an easy follow-up question via Haiku would actually be *more expensive* than answering with Opus, because switching models forces a full cache rebuild.
- Recommended pattern for mid-conversation model switches: use a subagent to have the current model (e.g., Opus) prepare a "hand-off" message summarizing the task for the next model — this is how Claude Code's Explore agents (which use Haiku) are dispatched.
- Changing the tool set mid-conversation is called out as "one of the most common ways people break prompt caching" — even though restricting tools to only what's currently needed feels intuitive, tools are part of the cached prefix, so adding/removing one invalidates the cache for the entire conversation.
- **Plan Mode** is implemented by keeping *all* tools present at all times and adding EnterPlanMode / ExitPlanMode as callable tools themselves, with a system message explaining Plan Mode's rules (explore, don't edit, call ExitPlanMode when done) — rather than swapping in a read-only tool subset. Bonus: because EnterPlanMode is itself a tool, the model can autonomously enter plan mode on a hard problem with no cache break.
- **Tool search / `defer_loading`**: Claude Code can have dozens of MCP tools loaded; instead of removing unused ones (which would break the cache), it sends lightweight stubs (just the tool name, `defer_loading: true`) that the model can "discover" via the tool search tool, with full schemas loaded only once selected — the cached prefix stays stable because the same stubs appear in the same order every time. Available via the Anthropic API's tool search tool.
- **Compaction cost trap**: naively compacting via a separate API call (its own "summarize this" system prompt, no tools) diverges from the main conversation's cached prefix at the very first token, so none of the cache applies — you pay full uncached input rate for the entire (often very long) conversation being summarized, and the longer the conversation, the worse this gets.
- **Cache-safe forking** (the fix): run compaction using the *exact same* system prompt, user/system context, and tool definitions as the parent conversation, prepending the parent's messages and appending only the compaction prompt as a new final user message — from the API's perspective this looks nearly identical to the parent's last request, so the cached prefix is reused and only the compaction-prompt tokens are new.
- Cache-safe forking requires reserving a "compaction buffer" of headroom in the context window for the compact message and its summary output tokens.
- These compaction-caching patterns have been built directly into the Claude API's native [[ContextWindow|compaction]] feature, so other developers building agents can get the same behavior without re-deriving it.
- Article written by Thariq Shihipar, member of technical staff on the Claude Code team; published 2026-04-30 on the Anthropic/Claude blog.
- **Anomaly**: no prompt-injection-style embedded instructions were found in the raw file; the only non-substantive artifacts are a trailing newsletter-signup CTA ("Get the developer newsletter...") and a duplicated opening paragraph (verbatim repeated twice), both cosmetic scraping artifacts rather than injected instructions.

## Related

- [[PromptCaching]] — the core API mechanism this article's lessons are about
- [[ClaudeCode]] — the product whose harness these caching lessons were derived from
- [[ContextWindow]] — houses the compaction concept extended by "cache-safe forking"
- [[ClaudeAgentSDK]] — general-purpose agent harness that could apply these same patterns
- [[ToolUse]] — tool-set stability is central to several of the lessons
