---
title: "ClaudeCodeSubagents"
type: concept
tags: [claude-code, subagents, context, delegation]
sources: [raw/03-transcripts/Claude/Claude Code subagents/03 - What are subagents.md, raw/03-transcripts/Claude/Claude Code subagents/01 - Using subagents effectively.md, raw/03-transcripts/Claude/Claude Code subagents/02 - Designing effective subagents.md, raw/03-transcripts/Claude/Claude Code subagents/04 - Creating a subagent.md, raw/01-articles/claude/2025-11-17 - How three YC startups built their companies with Claude Code.md, "raw/01-articles/claude/2026-05-28 - Introducing dynamic workflows in Claude Code.md", "raw/01-articles/claude/2026-06-18 - Steering Claude Code CLAUDE.md files, skills, hooks, rules, subagents and more.md"]
last_updated: 2026-07-07
---

## Definition

Claude Code sub-agents are specialized assistants that run in isolated context windows with custom system prompts. Claude delegates tasks to them, and they return only a summary -- keeping the main context clean by hiding intermediate exploration.

## Key Information

- **Isolation:** each sub-agent runs in its own context window; all intermediate work (file reads, edits, tool calls) stays isolated and is discarded after the summary is returned.
- **Built-in sub-agents:** general-purpose (multi-step exploration + action), explore (fast codebase searching), plan (research and analysis for plan mode).
- **Custom sub-agents:** created via `/agents` command; markdown files with YAML frontmatter (name, description, tools, model, system prompt).

### Subagents vs. Skills (June 2026)

Subagents and skills share the pattern of name/description loading at session start with the body not auto-invoking. The key difference is isolation: a subagent's body and all intermediate results never enter the parent conversation at all — only the final message and metadata return. A skill's body loads into the main thread when invoked, so you can see and steer each step.

- **Use a subagent** when a side task like deep search, log analysis, or a dependency audit would clutter your main conversation with intermediate results you won't reference again.
- **Use a skill** when you want the procedure to play out inside the main thread so you can see and steer each step.
- Subagents can nest up to five levels deep, and [[DynamicWorkflows|dynamic workflows]] orchestrate tens to hundreds of background agents without requiring you to specify each detail of the subagent architecture.

### When to Use

- **Good for:** research tasks (only the answer matters), code review (fresh eyes, no creation history), tasks needing different system prompts (copywriting tone, design system references).
- **Bad for:** sequential pipelines with conversational-summary handoffs (information loss between steps) — but sequential pipelines become viable when handoffs go through **files** (e.g., `docs/api-spec.md`), which preserve full fidelity that summary-based handoffs would lose; test runners (hide diagnostic output); "expert" claims (Claude already has the knowledge; overhead isn't justified).
- **Key question:** does the intermediate work matter? If not, delegate it.
- **Quantified escalation signal** (April 2026): exploring 10+ files, or 3+ independent pieces of work, is a strong signal to direct Claude toward subagents.
- **Benchmark gain** (April 2026): with Claude Opus 4.6, the ability to spawn subagents to isolate work in a fresh context window improved BrowseComp results by 2.8% over the best single-agent runs. See [[summary-2026-04-02 - Harnessing Claude’s intelligence]].
- **Unbiased review vs. `/clear`** (April 2026): `/clear` also resets context for a fresh perspective, but destroys conversation history entirely; a subagent achieves the same fresh-slate review while the main conversation stays intact.
- **Pre-commit second opinion** (April 2026): an independent subagent verifying an implementation isn't overfitting to tests or missing edge cases, run before finalizing changes.
- **Claude Code Guide** (April 2026): a built-in subagent invoked whenever a user asks about Claude Code itself (e.g., how to add an MCP server, what a slash command does); does doc-searching in its own isolated context per detailed extraction instructions and returns only the answer — added a whole capability (self-knowledge) without adding a new tool or bloating the system prompt with rarely-needed docs. See [[summary-2026-04-10 - Seeing like an agent how we design tools in Claude Code]].
- **Opus 4.7 default behavior** (April 2026): Opus 4.7 is more judicious about delegation and spawns fewer subagents by default than Opus 4.6; users who want parallel subagent fan-out (e.g., across files or independent items) need to explicitly prompt for it. Guidance: don't spawn a subagent for work completable directly in one response; do spawn multiple subagents in the same turn when fanning out. See [[summary-2026-04-16 - Best practices for using Claude Opus 4.7 with Claude Code]].
- **Splitting exploration from editing in large codebases** (May 2026): once the rest of the harness (CLAUDE.md, hooks, skills, plugins, MCP) is in place, a read-only subagent can map a subsystem and write its findings to a file, after which the main agent edits with the full picture — a pattern specifically called out for large, multi-million-line codebases where exploration alone could otherwise consume the main agent's context budget. See [[ContextEngineering]] and [[summary-2026-05-14 - How Claude Code works in large codebases Best practices and where to start]].

### Dynamic Workflows and Massively Parallel Subagents (May 2026)

[[DynamicWorkflows]] extend subagent parallelism to an unprecedented scale: Claude dynamically writes orchestration scripts that fan work out across **tens to hundreds of parallel subagents** in a single session, with independent verification and adversarial checking before results are combined. This is a step change from the typical subagent pattern of spawning a few agents for focused exploration or review:

- **Coordination outside the conversation**: The orchestration layer manages subtask distribution, result verification, and iterative convergence — the plan stays on track regardless of task size, and progress is saved so interrupted jobs resume where they left off.
- **Adversarial verification**: Agents address the problem from independent angles, while other agents try to refute what they found — the run keeps iterating until answers converge.
- **Scale example**: The [[Bun]] Zig-to-Rust rewrite used hundreds of agents working in parallel with two reviewers per file, plus a fix loop driving the build and test suite until both ran clean.
- **Token consumption**: Dynamic workflows consume substantially more tokens than typical sessions, since each subagent incurs its own context cost at scale.

### Design Principles

- **Structured output format:** the most important improvement; creates natural stopping points and prevents over-researching.
- **Obstacle reporting:** explicitly ask for workarounds, environment quirks, special flags so the main thread doesn't rediscover them.
- **Specific descriptions:** guide both when the main agent launches the sub-agent and what input prompt it writes.
- **Limited tool access:** read-only for research, bash for diff, edit/write only for code-changing agents.
- **Model selection:** Haiku (fast), Opus (complex), Sonnet (balanced), or inherit (same as main conversation).
- **Invocation methods** (April 2026): custom subagents are created via the `/agents` command (interactive) or hand-written as markdown files with YAML frontmatter (name, description, tools, model) in `.claude/agents/` (project-level, team-shared) or `~/.claude/agents/` (user-level, cross-project).
- **Background execution** (April 2026): Ctrl+B backgrounds a running subagent so the main conversation continues; results surface automatically on completion; `/tasks` lists background work.
- **Description field as routing key** (April 2026): for custom subagents, the `description` field is what Claude uses to decide when to delegate — specific trigger conditions ("reviews code for security issues before commits") route better than vague capability claims ("security expert").

## Related

- [[summary-03 - What are subagents]] — source summary
- [[summary-01 - Using subagents effectively]] — when to use
- [[summary-02 - Designing effective subagents]] — design patterns
- [[summary-04 - Creating a subagent]] — creation tutorial
- [[ClaudeCode]] — the tool sub-agents extend
- [[ContextWindow]] — the memory constraint sub-agents help manage
- [[ClaudeCodeSkills]] — skills vs. sub-agents comparison
- [[analysis-claude-code-extension-mechanisms]] — decision guide for choosing among extension mechanisms
- [[Ambral]] — startup that mirrored Claude Code's subagent design into its own product, with per-data-type subagents built on the [[ClaudeAgentSDK]]
- [[summary-2025-11-17 - How three YC startups built their companies with Claude Code]] — source article
- [[MultiAgentSystem]] — the general orchestrator-subagent pattern Claude Code's subagents implement
- [[summary-2026-04-07 - How and when to use subagents in Claude Code]] — source summary
- [[summary-2026-04-02 - Harnessing Claude’s intelligence]] — BrowseComp subagent-isolation benchmark gain
- [[summary-2026-04-10 - Seeing like an agent how we design tools in Claude Code]] — Claude Code Guide subagent and Task tool design history
- [[Claude4.7Opus]] — model with reduced default subagent-spawning behavior
- [[summary-2026-04-16 - Best practices for using Claude Opus 4.7 with Claude Code]] — source summary
- [[ContextEngineering]] — large-codebase context budget this exploration/editing split protects
- [[summary-2026-05-14 - How Claude Code works in large codebases Best practices and where to start]] — read-only exploration subagent pattern for large codebases
- [[DynamicWorkflows]] — massively parallel subagent orchestration feature
- [[summary-2026-05-28 - Introducing dynamic workflows in Claude Code]] — dynamic workflows announcement
- [[Bun]] — flagship dynamic workflows example using hundreds of parallel subagents
- [[summary-2026-06-18 - Steering Claude Code CLAUDE.md files, skills, hooks, rules, subagents and more]] — steering framework: subagents vs. skills decision guide
- [[summary-02 - Tool, skill, or subagent Decomposing an agent that outgrew its prompt]] — source summary
