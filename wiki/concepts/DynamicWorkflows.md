---
title: "DynamicWorkflows"
type: concept
tags: [claude-code, orchestration, parallelism, subagents, automation, workflows]
sources: ["raw/01-articles/claude/2026-05-28 - Introducing dynamic workflows in Claude Code.md", "raw/01-articles/claude/2026-06-02 - A harness for every task dynamic workflows in Claude Code.md"]
last_updated: 2026-07-07
---

## Definition

Dynamic workflows are a [[ClaudeCode]] feature that lets Claude tackle the most challenging engineering tasks end-to-end by dynamically writing orchestration scripts that run tens to hundreds of parallel subagents in a single session, with independent verification and adversarial checking before results reach the user.

## Key Information

### How It Works

When a workflow kicks off, Claude plans dynamically based on the user's prompt, breaks it into subtasks, and fans the work out across subagents running in parallel. Results are checked before they're folded in, and the user receives a single coordinated answer. Agents address the problem from independent angles, other agents try to refute what they found, and the run keeps iterating until answers converge — which is how a workflow reaches results a single pass cannot.

### Coordination

Coordination happens outside the conversation, so the plan stays on track regardless of task size. Progress is saved as the run goes, so an interrupted job picks up where it left off instead of starting over. This enables work that extends into hours and days.

### Invocation Modes

- **Direct request**: Ask Claude to create a dynamic workflow explicitly (e.g., "Create a workflow").
- **Ultracode**: A Claude Code-specific effort setting accessible through the effort menu that sets the effort level to `xhigh` and lets Claude decide automatically when to use a workflow to handle a task.

### Availability

Generally available in Claude Code CLI, Desktop, and the VS Code extension for Pro, Max, Team, and Enterprise plans. Also available on the Claude API, [[AmazonBedrock]], [[VertexAI]], and [[MicrosoftFoundry]]. On by default for Max, Team, and Enterprise plans; Pro plan users enable it in `/config`. Organization admins can optionally disable workflows through managed settings.

### Token Consumption

Dynamic workflows can consume substantially more tokens than a typical Claude Code session. Anthropic recommends starting on a scoped task to get a feel for usage. The first time a workflow triggers, Claude Code shows what's about to run and asks for confirmation.

### Use Cases

- **Codebase-wide bug hunts, profiler-guided optimization audits, and security audits**: Claude searches a service or repo in parallel, then runs independent verification on every finding so the report surfaces real issues. The same pattern works for hardening passes: auth checks, input validation, and unsafe patterns across an entire codebase.
- **Large migrations and modernization efforts**: Framework swaps, API deprecations, language ports spanning thousands of files — handled end-to-end.
- **Critical work needing double-checking**: When the cost of a wrong answer is high, a workflow gives Claude independent attempts at the problem and adversarial agents working to break the result before the user sees it.

### Workflow Patterns (June 2026)

A follow-up article catalogs the common patterns Claude composes when building dynamic workflows:

- **Classifier Routing**: A classifier agent decides the task type, then routes to different agents or behaviors.
- **Fan-out with Synthesis**: Split a task into many smaller steps, run an agent on each, then synthesize results — the synthesis step is a barrier that waits for all fan-out agents.
- **Adversarial Verification**: For each spawned agent, run a separate agent to adversarially verify its output against a rubric.
- **Tournament / Idea Generation**: Generate many ideas, filter by rubric, deduplicate, and return only the highest-quality results.
- **Parallel Competition**: Spawn N agents attempting the same task with different approaches, then judge pairwise until a winner emerges.
- **Agentic Loop**: For tasks with an unknown amount of work, loop spawning agents until a stop condition is met.
- **Quarantine**: Bar agents reading untrusted public content from high-privilege actions — a security pattern for triage workflows.
- **Model Selection Classifier**: A classifier researches the task first, then routes to the appropriate model (Sonnet vs. Opus) based on expected complexity.

### Additional Use Cases (June 2026)

- **Debugging**: Spin up agents to generate hypotheses from disjoint evidence (logs, files, data), with each hypothesis facing verifiers and refuters — prevents self-preferential bias in single-context-window debugging.
- **Research**: Fan-out web searches, fetch sources, adversarially verify claims, and synthesize a cited report. Used by Claude Code's `/deep-research` skill.
- **Triage**: Classify each item in a support queue, dedupe against tracked issues, and take action. Pair with `/loop` for continuous operation.
- **CLAUDE.md Mining**: Mine recent sessions for recurring corrections, cluster with parallel agents, adversarially verify each candidate rule, and distill survivors into `CLAUDE.md`.
- **Sorting/Ranking at Scale**: Sort 1000+ items by qualitative measurement using tournament brackets or pairwise-comparison agents.
- **Design Exploration**: Explore multiple solutions with a rubric, have a review agent evaluate, and select via tournament.
- **Lightweight Evals**: Spin off agents in worktrees to execute tasks, then comparison agents grade outputs against a rubric.

### Flagship Example: Bun Rewrite

[[JarredSumner]] used dynamic workflows to port [[Bun]] from Zig to Rust with 99.8% of the existing test suite passing — roughly 750,000 lines of Rust, completed in eleven days from first commit to merge. One workflow mapped Rust lifetimes for every struct field; the next wrote every `.rs` file as a behavior-identical port using hundreds of agents in parallel with two reviewers per file; a fix loop then drove the build and test suite until both ran clean. An overnight workflow afterward addressed unnecessary data copies and opened a PR for each.

### Best Practices

- Turn on **auto mode** when using dynamic workflows for the best experience.
- Start on a scoped task to understand token usage before tackling larger work.

## Related

- [[summary-2026-05-28 - Introducing dynamic workflows in Claude Code]] — launch announcement source
- [[summary-2026-06-02 - A harness for every task dynamic workflows in Claude Code]] — patterns and use cases deep-dive
- [[ClaudeCode]] — the tool dynamic workflows extend
- [[ClaudeCodeSubagents]] — subagent architecture underlying workflow parallelism
- [[AgentWorkflowPatterns]] — earlier static workflow patterns (sequential, parallel, evaluator-optimizer)
- [[MultiAgentSystem]] — broader multi-agent architecture and coordination patterns
- [[AgenticLoop]] — the loop pattern workflows can implement
- [[ClaudeCodeRoutines]] — scheduled automation that pairs with `/loop` workflows
- [[CodeReview]] — production example of multi-agent review pattern
- [[Debugging]] — debugging enhanced by workflow hypothesis-testing
- [[Research]] — Claude's research capability, powered by workflow fan-out
- [[CLAUDE-md]] — the memory file workflows can mine and update
- [[Ultracode]] — effort setting enabling automatic workflow invocation
- [[Bun]] — flagship example: Zig-to-Rust rewrite
- [[JarredSumner]] — Bun creator who used dynamic workflows
- [[ThariqShihipar]] — co-author of the June 2026 patterns article
- [[AmazonBedrock]] — cloud platform supporting dynamic workflows
- [[VertexAI]] — cloud platform supporting dynamic workflows
- [[MicrosoftFoundry]] — cloud platform supporting dynamic workflows
