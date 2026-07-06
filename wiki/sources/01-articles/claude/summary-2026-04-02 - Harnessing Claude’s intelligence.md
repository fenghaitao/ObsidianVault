---
title: "summary-2026-04-02 - Harnessing Claude’s intelligence"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-04-02 - Harnessing Claude’s intelligence.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic argues that agent harnesses encode assumptions about what Claude can't do on its own, and those assumptions grow stale as Claude's underlying intelligence improves — generative AI systems are "grown," not built, so capabilities emerge unpredictably. The article proposes three patterns for keeping application harnesses in step with Claude's evolving intelligence while balancing latency and cost: (1) build on general-purpose tools Claude already knows well (bash, text editor) rather than bespoke ones, since these compose into higher-level patterns like Agent Skills, programmatic tool calling, and the memory tool; (2) progressively hand orchestration decisions back to Claude itself — letting it filter its own tool outputs via code execution, assemble its own context via Skills, and persist its own memory via compaction and the memory tool — instead of hard-coding those decisions into the harness; and (3) keep the parts of the harness that must stay (declarative tools for security/UX/observability boundaries, cache-friendly context design) while continually re-evaluating and removing scaffolding (e.g., context-anxiety workarounds) that newer models no longer need. The piece is illustrated throughout with benchmark deltas across Claude model generations (Sonnet 4.5, Opus 4.5, Opus 4.6) on BrowseComp and BrowseComp-Plus, plus a qualitative example of Claude playing Pokémon to show memory-quality improvement over time.

## Key Points

- **Pattern 1 — use what Claude already knows**: Claude 3.5 Sonnet hit 49% on SWE-bench Verified (state of the art at the time) using only a bash tool and a text editor tool; Claude Code is grounded in the same two tools. General tools that Claude "knows how to use" compose into higher-level patterns (Agent Skills, programmatic tool calling, the memory tool) rather than needing bespoke tooling per task.
- **Let Claude orchestrate its own actions**: giving Claude a code execution tool (bash or a language-specific REPL) lets it write code to express tool calls and filter/pipe results itself, so only the code's output — not every raw tool result — reaches the context window. On BrowseComp, giving Opus 4.6 the ability to filter its own tool outputs raised accuracy from 45.3% to 61.6%. Since code is a general orchestration mechanism, a strong coding model is framed as also being a strong general agent.
- **Let Claude manage its own context**: Agent Skills let Claude keep only a short YAML description pre-loaded in context, progressively disclosing full skill content via a read-file tool only when needed — avoiding the attention-budget cost of pre-loading rarely-used instructions into the system prompt. Context editing is described as the inverse: selectively removing stale context (old tool results **or thinking blocks**) once it's no longer needed. Subagents let Claude fork into a fresh context window to isolate work; with Opus 4.6, the ability to spawn subagents improved BrowseComp results by 2.8% over the best single-agent runs.
- **Let Claude persist its own context**: compaction lets Claude summarize its own past context for continuity on long-horizon tasks — on BrowseComp, Sonnet 4.5 stayed flat at 43% regardless of compaction budget, while Opus 4.5 scaled to 68% and Opus 4.6 reached 84% under the same setup. A memory folder (files Claude writes and later reads) lifted Sonnet 4.5's BrowseComp-Plus accuracy from 60.4% to 67.2%. In a long-horizon Pokémon-playing test, Sonnet 3.5 treated memory as an undifferentiated transcript (31 files, including near-duplicate notes, after 14,000 steps, still in the second town), while Opus 4.6 at the same step count had 10 files organized into directories, three gym badges earned, and a distilled `learnings.md` file of tactical lessons from its own failures.
- **Design context to maximize cache hits**: the Messages API is stateless, so the harness must resend full context each turn; prompt caching writes context to a cache up to a set breakpoint, and cached tokens cost 10% of base input tokens.
- **Use declarative tools for security/UX/observability boundaries**: a bash tool gives Claude broad leverage but only exposes a generic command string to the harness; promoting specific actions to dedicated typed tools gives the harness a hook it can gate, render to a user, or log/audit. Hard-to-reverse actions (e.g., external API calls) are good candidates for user-confirmation gating; write tools can include staleness checks. Claude Code's auto-mode (research preview at time of publication) instead uses a second Claude instance to judge whether a bash command is safe — illustrating that this pattern can reduce, but not eliminate, the need for dedicated tools for high-stakes actions.
- **Prune stale harness scaffolding**: in an Anthropic long-horizon agent, Sonnet 4.5 exhibited "context anxiety" (wrapping up prematurely as it sensed the context limit approaching), prompting engineers to add context resets — but the behavior disappeared with Opus 4.5, making the resets dead weight. The article's closing framing: as Claude's frontier intelligence advances, harness assumptions must be continually re-tested, asking "what can I stop doing?"
- **Anomaly**: none of prompt-injection concern — the raw file is a straightforward Anthropic blog post/article (attribution, author bio, and a generic "get the developer newsletter" footer widget), with no embedded instructions attempting to redirect the reading agent.

## Related

- [[Anthropic]] — publisher of the article
- [[CodeExecutionTool]] — central mechanism for the "let Claude orchestrate its own actions" pattern
- [[ClaudeCodeSkills]] — central mechanism for the "let Claude manage its own context" pattern
- [[ContextEditing]] — the inverse of Skills-based context assembly, discussed as removing stale tool results and thinking blocks
- [[ClaudeCodeSubagents]] — context-isolation mechanism, with a new BrowseComp benchmark for Opus 4.6
- [[ContextWindow]] — houses the compaction and memory-folder benchmarks discussed
- [[PromptCaching]] — cache-breakpoint mechanism for stateless Messages API calls
- [[Claude4.6Opus]] — model benchmarked throughout (BrowseComp filtering, subagent spawning)
